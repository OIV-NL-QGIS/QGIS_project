"""Tool to draw lines and polygons on the map canvas"""
import qgis.PyQt.QtCore as PQtC
import qgis.core as QC
import qgis.gui as QG

import oiv.helpers.rubberband_helper as RH


class PolygonSelectTool(QG.QgsMapTool):
    """QgsMapTool to draw lines and polygons on the map canvas"""
    CAPTURE_POLYGON = 2

    def __init__(self, canvas):
        QG.QgsMapTool.__init__(self, canvas)
        self.canvas = canvas
        self.captureMode = None
        self.onGeometryAdded = None
        self.rubberBand = None
        self.tempRubberBand = None
        self.capturedPoints = []
        self.capturing = False
        self.parent = None
        self.setCursor(PQtC.Qt.CrossCursor)

    def canvasReleaseEvent(self, event):
        """#actie gekoppeld aan the mouse release event"""
        #als er met de linker muis geklikt wordt en er wordt nog niet getekend -> start het tekenen
        #anders voeg het aangeklikte punt toe aan de verzameling
        if event.button() == PQtC.Qt.LeftButton:
            if not self.capturing:
                self.startCapturing()
            self.addVertex(event.pos())
        #indien het de rechter muisknop is -> stop het tekenen en vertaal de punten tot een geometrie
        elif event.button() == PQtC.Qt.RightButton:
            self.getCapturedGeometry()
            self.stopCapturing()

    def canvasMoveEvent(self, event):
        """acties gekoppeld aan het bewegen van de muis"""
        #converteer de muislocatie naar laag en scherm coordinaten
        layerPt = self.toMapCoordinates(event.pos())
        if self.capturing:
            self.tempRubberBand.movePoint(layerPt)

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
        rbType = 'polygon'
        #rubberband voor de al vastgelegde punten
        self.rubberBand = RH.init_rubberband("drawn", self.canvas, rbType)
        self.rubberBand.show()
        #gestippelde rubberband -> voor het tekenen
        self.tempRubberBand = RH.init_rubberband("newpoint", self.canvas, rbType)
        self.tempRubberBandExt = RH.init_rubberband("drawinghelpers", self.canvas, "line")
        self.tempRubberBandExt.show()
        self.tempRubberBand.show()
        self.capturing = True

    def stopCapturing(self):
        """remove rubberbands als er gestopt wordt met tekenen"""
        if self.rubberBand:
            self.canvas.scene().removeItem(self.rubberBand)
            self.rubberBand = None
        if self.tempRubberBand:
            self.canvas.scene().removeItem(self.tempRubberBand)
            self.tempRubberBand = None
        self.capturing = False
        self.capturedPoints = []
        self.canvas.refresh()

    def addVertex(self, canvasPoint):
        """bepaal het daadwerkelijk toe te voegen punt (snappunt of geklikt punt)"""
        layerPt = self.toMapCoordinates(canvasPoint)
        #voeg het nieuwe map punt toe aan de rubberband
        self.rubberBand.addPoint(layerPt)
        #voeg het nieuwe layer punt toe aan de verzamelde punten
        self.capturedPoints.append(layerPt)
        #reset de temprubberband t.b.v. het volgende punt
        self.tempRubberBand.reset(QC.QgsWkbTypes.PolygonGeometry)
        firstPoint = self.rubberBand.getPoint(0, 0)
        self.tempRubberBand.addPoint(firstPoint)
        self.tempRubberBand.movePoint(layerPt)
        self.tempRubberBand.addPoint(layerPt)

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
            self.tempRubberBand.reset(QC.QgsWkbTypes.PolygonGeometry)
        del self.capturedPoints[-1]

    def getCapturedGeometry(self):
        """return captured points"""
        points = self.capturedPoints
        if len(points) >= 3:
            points.append(points[0])
            self.onGeometryAdded(points)
