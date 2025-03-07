"""snap and place a point feature on the map"""
import qgis.PyQt.QtCore as PQtC
import qgis.core as QC
import qgis.gui as QG

import oiv.helpers.rubberband_helper as RH
import oiv.helpers.drawing_helper as DH


class SnapPointTool(QG.QgsMapTool):
    """snap and place a point feature on the map"""
    def __init__(self, canvas):
        self.canvas = canvas
        QG.QgsMapTool.__init__(self, canvas)
        self.layer = None
        self.snapping = False
        self.onGeometryAdded = None
        self.snapPt = None
        self.startRotate = False
        self.tempRubberBand = None
        self.vertexmarker = None
        self.possibleSnapFeatures = []
        self.setCursor(PQtC.Qt.CrossCursor)

    def canvasReleaseEvent(self, event):
        """handle canvas release event"""
        clickedPt = None
        drawPoint = None
        snapAngle = None
        if event.button() == PQtC.Qt.LeftButton:
            #als er gesnapt wordt -> bereken rotatie op basis van geklikt punt en snappunt
            if self.snapPt is not None:
                clickedPt = self.toLayerCoordinates(self.layer, event.pos())
                drawPoint = self.toLayerCoordinates(self.layer, self.snapPt)
                snapAngle = clickedPt.azimuth(drawPoint)
                self.stopPointTool()
            #als er niets gesnapt wordt maar geroteerd bereken de rotatie op basis van de 2 punten in temprubberband
            elif self.startRotate:
                clickedPt = self.toLayerCoordinates(self.layer, event.pos())
                tempGeometry = self.tempRubberBand.asGeometry().asPolyline()
                drawPoint = self.toLayerCoordinates(self.layer, tempGeometry[0])
                snapAngle = drawPoint.azimuth(clickedPt)
                self.tempRubberBand.hide()
                self.stopPointTool()
            else:
            #als aan beide bovenstaande voorwaarden niet wordt voldaan wordt het pictogram gewoon geplaatst en is de hoek 0
                drawPoint = self.toLayerCoordinates(self.layer, event.pos())
            self.onGeometryAdded(drawPoint, snapAngle)
            self.snapPt = None
        #als de rechtermuisknop wordt gebruikt (1e keer) start het roteren
        if event.button() == PQtC.Qt.RightButton:
            if not self.startRotate:
                self.start_to_rotate(event)

    def stopPointTool(self):
        """reset everything"""
        if self.tempRubberBand:
            self.canvas.scene().removeItem(self.tempRubberBand)
            self.tempRubberBand = None
        if self.vertexmarker:
            self.canvas.scene().removeItem(self.vertexmarker)
            self.vertexmarker = None
        self.startRotate = False
        self.canvas.refresh()

    def start_to_rotate(self, event):
        """indien roteren -> init temprubberband"""
        mapPt = self.toMapCoordinates(event.pos())
        self.tempRubberBand = RH.init_rubberband("moveandrotatepoint", self.canvas, 'line')
        self.tempRubberBand.show()
        self.tempRubberBand.addPoint(mapPt)
        self.startRotate = True

    def canvasMoveEvent(self, event):
        """indien er niet geroteerd wordt kan er worden gesnapt op vooraf gedfinieerde lagen"""
        mapPt = self.toMapCoordinates(event.pos())
        layerPt = self.toLayerCoordinates(self.layer, event.pos())
        if not self.startRotate:
            if self.snapping:
                self.snapPt = self.snap_to_point(event.pos(), layerPt)
                if self.vertexmarker is not None:
                    self.vertexmarker.hide()
                if self.snapPt is not None:
                    self.vertexmarker.setCenter(self.snapPt)
                    self.vertexmarker.show()
        else:
        #indien geroteerd wordt - teken de rubberband
            self.tempRubberBand.movePoint(mapPt)

    def snap_to_point(self, pos, layerPt):
        """calculat if there is a point to snap to within the tolerance"""
        tolerance = pow(DH.calcTolerance(self, pos), 2)
        minDist = tolerance
        snapPoint = None
        if self.vertexmarker is None:
            self.vertexmarker = RH.init_vertexmarker("snappoint", self.canvas)
        for geom in self.possibleSnapFeatures:
            closestSegm = geom.closestSegmentWithContext(layerPt)
            if closestSegm[0] < minDist and closestSegm[0] >= 0:
                minDist = closestSegm[0]
                snapPoint = closestSegm[1]
        if snapPoint and snapPoint != QC.QgsPointXY(0, 0):
            return snapPoint
