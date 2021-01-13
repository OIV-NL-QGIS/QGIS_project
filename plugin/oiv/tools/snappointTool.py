"""snap and place a point feature on the map"""

from qgis.PyQt.QtGui import QColor
from qgis.PyQt.QtCore import Qt, QPoint

from qgis.core import QgsWkbTypes, QgsFeatureRequest, QgsSpatialIndex, QgsRectangle, QgsPointXY
from qgis.gui import QgsRubberBand, QgsMapTool, QgsVertexMarker

class SnapPointTool(QgsMapTool):
    """snap and place a point feature on the map"""
    def __init__(self, canvas):
        self.canvas = canvas
        QgsMapTool.__init__(self, canvas)
        self.layer = None
        self.snapping = False
        self.onGeometryAdded = None
        self.snapPt = None
        self.startRotate = False
        self.tempRubberBand = None
        self.vertexmarker = None
        self.possibleSnapFeatures = []
        self.setCursor(Qt.CrossCursor)

    def canvasReleaseEvent(self, event):
        """handle canvas release event"""
        clickedPt = None
        drawPoint = None
        snapAngle = None
        if event.button() == Qt.LeftButton:
            #als er gesnapt wordt -> bereken rotatie op basis van geklikt punt en snappunt
            if self.snapPt is not None:
                dummy, clickedPt = self.transformCoordinates(event.pos())
                drawPoint = self.toLayerCoordinates(self.layer, self.snapPt)
                snapAngle = clickedPt.azimuth(drawPoint)
                self.stopPointTool()
            #als er niets gesnapt wordt maar geroteerd bereken de rotatie op basis van de 2 punten in temprubberband
            elif self.startRotate:
                dummy, clickedPt = self.transformCoordinates(event.pos())
                tempGeometry = self.tempRubberBand.asGeometry().asPolyline()
                drawPoint = self.toLayerCoordinates(self.layer, tempGeometry[0])
                snapAngle = drawPoint.azimuth(clickedPt)
                self.tempRubberBand.hide()
                self.stopPointTool()
            else:
            #als aan beide bovenstaande voorwaarden niet wordt voldaan wordt het pictogram gewoon geplaatst en is de hoek 0
                dummy, drawPoint = self.transformCoordinates(event.pos())
            self.onGeometryAdded(drawPoint, snapAngle)
            self.snapPt = None
        #als de rechtermuisknop wordt gebruikt (1e keer) start het roteren
        if event.button() == Qt.RightButton:
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
        mapPt, dummy = self.transformCoordinates(event.pos())
        color = QColor("black")
        color.setAlphaF(0.78)
        self.tempRubberBand = QgsRubberBand(self.canvas, QgsWkbTypes.LineGeometry)
        self.tempRubberBand.setWidth(4)
        self.tempRubberBand.setColor(color)
        self.tempRubberBand.setLineStyle(Qt.DotLine)
        self.tempRubberBand.show()
        self.tempRubberBand.addPoint(mapPt) 
        self.startRotate = True

    def canvasMoveEvent(self, event):
        """indien er niet geroteerd wordt kan er worden gesnapt op vooraf gedfinieerde lagen"""
        mapPt, layerPt = self.transformCoordinates(event.pos())
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
        tolerance = pow(self.calcTolerance(pos), 2)
        minDist = tolerance
        snapPoint = None
        if self.vertexmarker is None:
            self.init_vertexmarker()
        for geom in self.possibleSnapFeatures:
            closestSegm = geom.closestSegmentWithContext(layerPt)
            if closestSegm[0] < minDist:
                minDist = closestSegm[0]
                snapPoint = closestSegm[1]
        if snapPoint and snapPoint != QgsPointXY(0, 0):
            return snapPoint

    def init_vertexmarker(self):
        self.vertexmarker = QgsVertexMarker(self.canvas)
        self.vertexmarker.setColor(QColor(255, 0, 255))
        self.vertexmarker.setIconSize(8)
        self.vertexmarker.setIconType(QgsVertexMarker.ICON_X) # or ICON_CROSS, ICON_X
        self.vertexmarker.setPenWidth(5)
        self.vertexmarker.show()

    def calcTolerance(self, pos):
        """calculate snap tolerance"""
        pt1 = QPoint(pos.x(), pos.y())
        pt2 = QPoint(pos.x() + 20, pos.y())
        dummy, layerPt1 = self.transformCoordinates(pt1)
        dummy, layerPt2 = self.transformCoordinates(pt2)
        tolerance = layerPt2.x() - layerPt1.x()
        return tolerance

    def transformCoordinates(self, canvasPt):
        """transormeer de coordinaten naar canvas en laag punten"""
        return (self.toMapCoordinates(canvasPt),
                self.toLayerCoordinates(self.layer, canvasPt))
