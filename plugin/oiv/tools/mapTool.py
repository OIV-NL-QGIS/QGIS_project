"""Tool to draw lines and polygons on the map canvas"""
import qgis.PyQt.QtCore as PQtC
import qgis.core as QC
import qgis.gui as QG

import oiv.helpers.rubberband_helper as RH


class CaptureTool(QG.QgsMapTool):
    """QgsMapTool to draw lines and polygons on the map canvas"""
    CAPTURE_LINE = 1
    CAPTURE_POLYGON = 2
    snapRubberBand = []

    def __init__(self, canvas):
        QG.QgsMapTool.__init__(self, canvas)
        self.canvas = canvas
        self.captureMode = None
        self.onGeometryAdded = None
        self.rubberBand = None
        self.tempRubberBand = None
        self.tempRubberBandExt = None
        self.perpRubberBand = None
        self.perpRubberBand2 = None
        self.parallelRubberBand = None
        self.roundRubberBand = None
        self.capturedPoints = []
        self.capturing = False
        self.snapPt = None
        self.snapFeature = []
        self.possibleSnapFeatures = []
        self.vertexmarker = None
        self.parent = None
        self.setCursor(PQtC.Qt.CrossCursor)

    def canvasReleaseEvent(self, event):
        """#actie gekoppeld aan the mouse release event"""
        #als the perpendicular rubberbands bestaan reset zodat ze opnieuw kunnen worden getekend
        if self.perpRubberBand is not None:
            self.perpRubberBand.reset()
        if self.perpRubberBand2 is not None:
            self.perpRubberBand2.reset()
        if self.parallelRubberBand is not None:
            self.parallelRubberBand.reset()
        if self.roundRubberBand is not None:
            self.roundRubberBand.reset()
        #als er met de linker muis geklikt wordt en er wordt nog niet getekend -> start het tekenen
        #anders voeg het aangeklikte punt toe aan de verzameling
        if event.button() == PQtC.Qt.LeftButton:
            if not self.capturing:
                self.startCapturing()
            if self.parent.offset_button.isChecked():
                self.drawParallel(event.pos())
            else:
                self.addVertex(event.pos())
        #indien het de rechter muisknop is -> stop het tekenen en vertaal de punten tot een geometrie
        elif event.button() == PQtC.Qt.RightButton:
            self.getCapturedGeometry()
            self.stopCapturing()

    def canvasMoveEvent(self, event):
        """acties gekoppeld aan het bewegen van de muis"""
        #converteer de muislocatie naar laag en scherm coordinaten
        layerPt = self.toMapCoordinates(event.pos())
        #kijk of er mogelijk gesnapt kan worden
        self.snapPt = self.snap_to_point(event.pos(), layerPt)
        if self.capturing:
            self.tempRubberBand.movePoint(layerPt)
            tempBandSize = self.tempRubberBand.numberOfVertices()
            #pas de "gestippelde" rubberband aan aan de muispositie
            if tempBandSize > 0 and self.capturing:
                if self.captureMode == CaptureTool.CAPTURE_LINE:
                    self.tempRubberBandExt.setToGeometry(self.tempRubberBand.asGeometry().extendLine(0, 50))
                    try:
                        distance = QC.QgsDistanceArea()
                        m = distance.measureLine(self.tempRubberBand.getPoint(0, 0), layerPt)
                        self.parent.lengte.setValue(round(m, 2))
                    except: # pylint: disable=bare-except
                        pass
                else:
                    geom = QC.QgsGeometry.fromPolylineXY([self.tempRubberBand.getPoint(0, tempBandSize - 2), layerPt]).extendLine(0, 50)
                    self.tempRubberBandExt.setToGeometry(geom)
            if self.captureMode == CaptureTool.CAPTURE_POLYGON and len(self.capturedPoints) >= 1 and self.capturing:
                distance = QC.QgsDistanceArea()
                m = distance.measureLine(self.tempRubberBand.getPoint(0, tempBandSize - 2), layerPt)
                self.parent.lengte.setValue(round(m, 2))
                try:
                    polygon = self.rubberBand.asGeometry().asPolygon()[0]
                    temppolygon = self.tempRubberBand.asGeometry().asPolygon()[0]
                    area = QC.QgsDistanceArea()
                    a = area.measurePolygon(polygon)
                    b = area.measurePolygon(temppolygon)
                    self.parent.oppervlakte.setValue(round(a + b, 2))
                except: # pylint: disable=bare-except
                    pass
        #laat standaard het snappunt niet zien tenzij er gesnapt kan worden
        self.vertexmarker.hide()
        if self.snapPt is not None:
            self.vertexmarker.setCenter(self.snapPt)
            self.vertexmarker.show()

    def snap_to_point(self, pos, layerPt):
        """calculate if there is a point to snap to within the tolerance"""
        tolerance = pow(self.calcTolerance(pos), 2)
        self.snapPt = None
        self.snapFeature = []
        minDist = tolerance
        snapPoints = []
        counter = 0
        #add rubberbands as possible snapfeatures
        snappableFeatures = self.possibleSnapFeatures + self.snapRubberBand
        if self.vertexmarker is None:
            self.vertexmarker = RH.init_vertexmarker("snappoint", self.canvas)
        for geom in snappableFeatures:
            closestSegm = geom.closestSegmentWithContext(layerPt)
            vertexCoord, vertex, prevVertex, dummy, distSquared = geom.closestVertex(layerPt)
            if distSquared < minDist:
                minDist = distSquared
                snapPoints = []
                snapPoints.extend([vertexCoord, vertex, prevVertex, counter, geom])
            elif closestSegm[0] < minDist - 1/2 * tolerance and closestSegm[0] >= 0:
                minDist = closestSegm[0]
                snapPoints = []
                snapPoints.extend([closestSegm[1], None, None, counter, geom])
            counter += 1
        if snapPoints:
            snapPoint = snapPoints[0]
            igeometry = snapPoints[4]
            if igeometry.wkbType() == QC.QgsWkbTypes.LineString:
                polygon = igeometry.asPolyline()
            elif igeometry.wkbType() == QC.QgsWkbTypes.MultiLineString:
                polygon = igeometry.asMultiPolyline()[0]
            elif igeometry.wkbType() == 1003 or igeometry.wkbType() == 6:
                polygon = igeometry.asMultiPolygon()[0][0]
            else:
                polygon = igeometry.asPolygon()[0]
            if snapPoints[1] is not None:
                self.snapFeature.extend((snapPoints[1], snapPoints[2], polygon))
            else:
                self.snapFeature.extend((None, None, None))
            return snapPoint

    def calcTolerance(self, pos):
        """calculate the tolerance of snapping"""
        pt1 = PQtC.QPoint(pos.x(), pos.y())
        pt2 = PQtC.QPoint(pos.x() + 20, pos.y())
        layerPt1 = self.toMapCoordinates(pt1)
        layerPt2 = self.toMapCoordinates(pt2)
        tolerance = layerPt2.x() - layerPt1.x()
        return tolerance

    def keyPressEvent(self, event):
        """handle keypress events"""
        if event.key() == PQtC.Qt.Key_Backspace or \
           event.key() == PQtC.Qt.Key_Delete:
            self.removeLastVertex()
            event.ignore()
        if event.key() == PQtC.Qt.Key_Return or event.key() == PQtC.Qt.Key_Enter:
            self.getCapturedGeometry()
            self.stopCapturing()

    def startCapturing(self):
        """bij starten van het tekenen intialiseer de rubberbands"""
        if self.bandType() == QC.QgsWkbTypes.PolygonGeometry:
            rbType = 'polygon'
        else:
            rbType = 'line'
        #rubberband voor de al vastgelegde punten
        self.rubberBand = RH.init_rubberband("drawn", self.canvas, rbType)
        self.rubberBand.show()
        #gestippelde rubberband -> voor het tekenen
        self.tempRubberBand = RH.init_rubberband("newpoint", self.canvas, rbType)
        self.tempRubberBandExt = RH.init_rubberband("drawinghelpers", self.canvas, "line")
        self.tempRubberBandExt.show()
        self.tempRubberBand.show()
        #2x loodrechte hulp tekenlijnen
        self.perpRubberBand = RH.init_rubberband("drawinghelpers", self.canvas, "line")
        self.perpRubberBand2 = RH.init_rubberband("drawinghelpers", self.canvas, "line")
        self.perpRubberBand.show()
        self.perpRubberBand2.show()
        self.parallelRubberBand = RH.init_rubberband("drawinghelpers", self.canvas, "line")
        self.parallelRubberBand.show()
        #round distance rubberband
        self.roundRubberBand = RH.init_rubberband("drawinghelpers", self.canvas, "line")
        self.roundRubberBand.show()
        self.parent.straal.valueChanged.connect(self.draw_help_circle)
        self.parent.straal_button.clicked.connect(self.enable_roundrubberband)
        self.capturing = True

    def bandType(self):
        """bepaal het type rubberband (polygoon of line)"""
        if self.captureMode == CaptureTool.CAPTURE_POLYGON:
            return QC.QgsWkbTypes.PolygonGeometry
        else:
            return QC.QgsWkbTypes.LineGeometry

    def enable_roundrubberband(self):
        """hide/show the help circle"""
        if self.roundRubberBand:
            if self.parent.straal_button.isChecked():
                self.roundRubberBand.show()
            else:
                self.roundRubberBand.hide()

    def stopCapturing(self):
        """remove rubberbands als er gestopt wordt met tekenen"""
        if self.rubberBand:
            RH.resetRB(self.rubberBand, self.bandType())
            self.rubberBand = None
        if self.tempRubberBand:
            RH.resetRB(self.tempRubberBand, self.bandType())
            self.tempRubberBand = None
        if self.tempRubberBandExt:
            RH.resetRB(self.tempRubberBandExt, QC.QgsWkbTypes.LineGeometry)
            self.tempRubberBandExt = None
        if self.roundRubberBand:
            RH.resetRB(self.roundRubberBand, QC.QgsWkbTypes.LineGeometry)
            self.roundRubberBand = None
        if self.perpRubberBand:
            RH.resetRB(self.perpRubberBand, QC.QgsWkbTypes.LineGeometry)
            self.perpRubberBand = None
        if self.perpRubberBand2:
            RH.resetRB(self.perpRubberBand2, QC.QgsWkbTypes.LineGeometry)
            self.perpRubberBand2 = None
        if self.parallelRubberBand:
            RH.resetRB(self.parallelRubberBand, QC.QgsWkbTypes.LineGeometry)
            self.parallelRubberBand = None
        self.vertexmarker.hide()
        self.capturing = False
        self.capturedPoints = []
        self.canvas.refresh()

    def addVertex(self, canvasPoint):
        """bepaal het daadwerkelijk toe te voegen punt (snappunt of geklikt punt)"""
        self.snapRubberBand = []
        snapAngle = None
        polygon = None
        clickedPt = None
        if self.snapPt is not None:
            if self.snapFeature[2] is not None and self.snapFeature[1] is not None:
                polygon = self.snapFeature[2]
                clickedPt = polygon[self.snapFeature[1]] #vertexnr.
            else:
                clickedPt = self.toMapCoordinates(canvasPoint)
            layerPt = self.snapPt
            #bereken de snaphoek van het geklikte punt ten opzichte van het snappunt
            snapAngle = clickedPt.azimuth(layerPt)
        else:
            layerPt = self.toMapCoordinates(canvasPoint)
            if self.capturedPoints:
                perpPt = self.capturedPoints[-1]
                snapAngle = layerPt.azimuth(perpPt) + 90
        #voeg het nieuwe map punt toe aan de rubberband
        self.rubberBand.addPoint(layerPt)
        #voeg het nieuwe layer punt toe aan de verzamelde punten
        self.capturedPoints.append(layerPt)
        self.draw_help_circle()
        if snapAngle:
            self.draw_helplines(layerPt, snapAngle)
        #reset de temprubberband t.b.v. het volgende punt
        self.tempRubberBand.reset(self.bandType())
        self.tempRubberBandExt.reset(QC.QgsWkbTypes.LineGeometry)
        if self.captureMode == CaptureTool.CAPTURE_LINE:
            self.tempRubberBand.addPoint(layerPt)
        elif self.captureMode == CaptureTool.CAPTURE_POLYGON:
            firstPoint = self.rubberBand.getPoint(0, 0)
            self.tempRubberBand.addPoint(firstPoint)
            self.tempRubberBand.movePoint(layerPt)
            self.tempRubberBand.addPoint(layerPt)

    def drawParallel(self, canvasPoint):
        """bepaal het daadwerkelijk toe te voegen punt (snappunt of geklikt punt)"""
        self.snapRubberBand = []
        clickedPt = None
        if self.snapPt is not None and self.snapFeature[2] is None:
            clickedPt = self.toMapCoordinates(canvasPoint)
            layerPt = self.snapPt
            #bereken de snaphoek van het geklikte punt ten opzichte van het snappunt
            snapAngle = clickedPt.azimuth(layerPt) + 90
            offset = self.parent.offset.value()
            distance = QC.QgsDistanceArea()
            m = distance.measureLine(layerPt, clickedPt)
            geom = QC.QgsGeometry.fromPolylineXY([layerPt, clickedPt])
            if offset > m:
                geom = geom.extendLine(0, offset - m)
                offsetPt = geom.asPolyline()[-1]
            else:
                offsetPt = geom.interpolate(offset).asPoint()
            point1, point2, dummy, dummy = RH.calculate_perpendicularbands(offsetPt, snapAngle)
            self.parallelRubberBand.addPoint(point1)
            self.parallelRubberBand.addPoint(point2, True)
            self.snapRubberBand.append(self.parallelRubberBand.asGeometry())
            if self.capturedPoints:
                bandSize = self.rubberBand.numberOfVertices()
                lastPt = self.rubberBand.getPoint(0, bandSize-1)
                self.draw_helplines(lastPt, snapAngle)
            self.parent.offset_button.toggle()

    def draw_help_circle(self):
        """change diameter of circular rubberband"""
        if self.parent.straal_button.isChecked() and self.capturing:
            straal = self.parent.straal.value()
            startPt = self.capturedPoints[-1]
            circle = QC.QgsCircle(QC.QgsPoint(startPt), straal)
            cString = circle.toCircularString()
            geom_from_curve = QC.QgsGeometry(cString)
            self.roundRubberBand.setToGeometry(geom_from_curve)
            self.snapRubberBand.append(self.roundRubberBand.asGeometry())

    def draw_helplines(self, startPt, angle):
        """bereken de haakse lijnen op basis van de gesnapte feature"""
        point1, point2, point3, point4 = RH.calculate_perpendicularbands(startPt, angle)
        self.perpRubberBand.addPoint(point1)
        self.perpRubberBand.addPoint(point2, True)
        self.snapRubberBand.append(self.perpRubberBand.asGeometry())
        self.perpRubberBand2.addPoint(point3)
        self.perpRubberBand2.addPoint(point4, True)
        self.snapRubberBand.append(self.perpRubberBand2.asGeometry())

    def removeLastVertex(self):
        """verwijder het laatste punt (backspace of delete)"""
        if not self.capturing:
            return
        bandSize = self.rubberBand.numberOfVertices()
        tempBandSize = self.tempRubberBand.numberOfVertices()
        numPoints = len(self.capturedPoints)
        if bandSize < 1 or numPoints < 1:
            return
        self.rubberBand.removePoint(-1)
        if bandSize > 1:
            if tempBandSize > 1:
                point = self.rubberBand.getPoint(0, bandSize-2)
                self.tempRubberBand.movePoint(tempBandSize-2, point)
        else:
            self.tempRubberBand.reset(self.bandType())
        del self.capturedPoints[-1]

    def getCapturedGeometry(self):
        """return captured points"""
        snapAngle = None
        points = self.capturedPoints
        #voor lijn -> minimaal 2 punten
        if self.captureMode == CaptureTool.CAPTURE_LINE:
            if len(points) >= 2:
                self.vertexmarker.hide()
                self.onGeometryAdded(points, snapAngle)
        #voor polygoon -> minimaal 3 punten
        if self.captureMode == CaptureTool.CAPTURE_POLYGON:
            if len(points) >= 3:
                points.append(points[0])
                self.onGeometryAdded(points, snapAngle)
        self.vertexmarker.hide()
