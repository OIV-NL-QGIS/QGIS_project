"""Move or rotate a point feature on the map canvas"""
from qgis.PyQt.QtCore import Qt #pylint: disable=import-error
from qgis.core import QgsGeometry #pylint: disable=import-error
from qgis.gui import QgsMapToolIdentify #pylint: disable=import-error

from ..plugin_helpers.rubberband_helper import init_rubberband, init_vertexmarker
from .utils_core import check_layer_type

class MovePointTool(QgsMapToolIdentify):
    """identify the clicked point from the user and proces"""

    def __init__(self, canvas, layer):
        QgsMapToolIdentify.__init__(self, canvas)
        self.canvas = canvas
        self.setCursor(Qt.CrossCursor)
        self.layer = layer
        self.dragging = False
        self.fields = None
        self.onMoved = None
        self.point = None
        self.fid = None
        self.idlayer = None
        self.startRotate = False
        self.tempRubberBand = None
        self.vertexMarker = None

    def canvasPressEvent(self, event):
        """op welke feature wordt er geklikt"""
        found_features = self.identify(event.x(), event.y(), self.TopDownStopAtFirst, self.VectorLayer)
        #check type van de laag, het werkt alleen voor point layers
        type_check = check_layer_type(found_features[0].mLayer)
        self.idlayer = found_features[0].mLayer
        feature = found_features[0].mFeature
        self.fid = feature.id()
        #indien de linkesmuisnop wordt geklikt, het betreft een point layer en er is een feature gevonden -> verslepen
        if event.button() == Qt.LeftButton:
            if found_features is not None and type_check == "Point":
                self.dragging = True
                #init drag point
                self.vertexMarker = init_vertexmarker("movepoint", self.canvas)
                self.vertexMarker.show()
            #anders doe niets
            else:
                self.dragging = False
                self.fid = None
        #indien de rechtermuisknop wordt geklikt -> roteren
        if event.button() == Qt.RightButton:
            if found_features is not None and type_check == "Point":
                if not self.startRotate:
                    self.start_to_rotate(event)
            else:
                self.startRotate = False
                self.fid = None

    def start_to_rotate(self, event):
        """init tempRubberband indicating rotation"""
        layerPt = self.toMapCoordinates(event.pos())
        self.tempRubberBand = init_rubberband("moveandrotatepoint", self.canvas, 'line')
        self.tempRubberBand.show()
        self.tempRubberBand.addPoint(layerPt)
        self.startRotate = True

    def canvasMoveEvent(self, event):
        """als verslepen -> verplaats de indicatieve marker"""
        layerPt = self.toMapCoordinates(event.pos())
        if self.tempRubberBand is None:
            self.tempRubberBand = init_rubberband("moveandrotatepoint", self.canvas, 'line')
        if self.dragging:
            self.point = layerPt
            self.vertexMarker.setCenter(layerPt)
        #als roteren -> teken de tempRubberband als lijn
        if self.startRotate:
            self.tempRubberBand.movePoint(layerPt)

    def canvasReleaseEvent(self, event):
        """als verslepen -> pas de geometry van de betreffende feature aan"""
        if self.dragging:
            self.vertexMarker.hide()
            geom = QgsGeometry.fromPointXY(self.point)
            self.idlayer.dataProvider().changeGeometryValues({self.fid : geom})
            self.idlayer.commitChanges()
            self.idlayer.triggerRepaint()
            self.stop_moveTool()
        #als roteren -> pas de rotatie van de betreffende feature aan op basis van de loodrechte lijn tussen muisklik en bestaand punt
        if self.startRotate:
            self.tempRubberBand.hide()
            clickedPt = self.toMapCoordinates(event.pos())
            tempGeometry = self.tempRubberBand.asGeometry().asPolyline()
            drawPoint = self.toLayerCoordinates(self.layer, tempGeometry[0])
            field = self.idlayer.fields().indexOf("rotatie")
            rotation = drawPoint.azimuth(clickedPt)
            attrs = {field : rotation}
            self.idlayer.dataProvider().changeAttributeValues({self.fid : attrs})
            self.idlayer.commitChanges()
            self.idlayer.triggerRepaint()
            self.stop_moveTool()

    def stop_moveTool(self):
        """reset rubberbands"""
        if self.tempRubberBand is not None:
            self.canvas.scene().removeItem(self.tempRubberBand)
            self.tempRubberBand = None
        if self.vertexMarker is not None:
            self.canvas.scene().removeItem(self.vertexMarker)
            self.vertexMarker = None
        self.fid = None
        self.startRotate = False
        self.dragging = False
        self.onMoved()
        self.canvas.refresh()
