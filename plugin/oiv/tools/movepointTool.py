"""Move or rotate a point feature on the map canvas"""
import qgis.PyQt.QtCore as PQtC
import qgis.core as QC
import qgis.gui as QG

import oiv.helpers.rubberband_helper as RH
import oiv.helpers.utils_core as UC
import oiv.helpers.drawing_helper as DH


class MovePointTool(QG.QgsMapToolIdentify):
    """identify the clicked point from the user and proces"""

    def __init__(self, canvas):
        QG.QgsMapToolIdentify.__init__(self, canvas)
        self.canvas = canvas
        self.setCursor(PQtC.Qt.CrossCursor)
        self.layer = None
        self.dragging = False
        self.fields = None
        self.onMoved = None
        self.point = None
        self.fid = None
        self.idlayer = None
        self.startRotate = False
        self.tempRubberBand = None
        self.vertexmarker = None
        self.vertexMovemarker = None
        self.multi = False
        self.possibleSnapFeatures = []

    def canvasPressEvent(self, event):
        """op welke feature wordt er geklikt"""
        found_features = self.identify(event.x(), event.y(), self.TopDownStopAtFirst, self.VectorLayer)
        #check type van de laag, het werkt alleen voor point layers
        type_check = UC.check_layer_type(found_features[0].mLayer)
        self.idlayer = found_features[0].mLayer
        feature = found_features[0].mFeature
        self.fid = feature.id()
        #indien de linkesmuisnop wordt geklikt, het betreft een point layer en er is een feature gevonden -> verslepen
        if event.button() == PQtC.Qt.LeftButton:
            if found_features is not None and type_check == "Point":
                self.dragging = True
                #init drag point
                self.vertexMovemarker = RH.init_vertexmarker("movepoint", self.canvas)
                self.vertexMovemarker.show()
            #anders doe niets
            else:
                self.dragging = False
                self.fid = None
        #indien de rechtermuisknop wordt geklikt -> roteren
        if event.button() == PQtC.Qt.RightButton:
            if found_features is not None and type_check == "Point":
                if not self.startRotate:
                    self.start_to_rotate(event)
            else:
                self.startRotate = False
                self.fid = None

    def start_to_rotate(self, event):
        """init tempRubberband indicating rotation"""
        layerPt = self.toMapCoordinates(event.pos())
        self.tempRubberBand = RH.init_rubberband("moveandrotatepoint", self.canvas, 'line')
        self.tempRubberBand.show()
        self.tempRubberBand.addPoint(layerPt)
        self.startRotate = True

    def canvasMoveEvent(self, event):
        """als verslepen -> verplaats de indicatieve marker"""
        layerPt = self.toMapCoordinates(event.pos())
        self.point = None
        if self.tempRubberBand is None:
            self.tempRubberBand = RH.init_rubberband("moveandrotatepoint", self.canvas, 'line')
        if self.dragging:
            self.point = layerPt
            self.vertexMovemarker.setCenter(layerPt)
        #als roteren -> teken de tempRubberband als lijn
        elif self.startRotate:
            self.tempRubberBand.movePoint(layerPt)
        else:
            layerPt = self.toLayerCoordinates(self.layer, event.pos())
            self.snapPt = DH.snap_to_point(self, event.pos(), layerPt)
            if self.vertexmarker is not None:
                self.vertexmarker.hide()
            if self.snapPt is not None:
                self.vertexmarker.setCenter(self.snapPt)
                self.vertexmarker.show()

    def canvasReleaseEvent(self, event):
        """als verslepen -> pas de geometry van de betreffende feature aan"""
        if self.dragging and self.point:
            self.vertexmarker.hide()
            geom_new = QC.QgsGeometry.fromPointXY(self.point)
            geom_old = self.idlayer.getFeature(self.fid).geometry()
            if not self.multi:
                self.idlayer.changeGeometry(self.fid, geom_new)
            field_idx = self.idlayer.fields().indexOf('applicatie')
            if field_idx != -1:
                self.idlayer.changeAttributeValue(self.fid, field_idx, 'OIV')
            self.idlayer.commitChanges()
            self.idlayer.triggerRepaint()
            self.stop_moveTool(None, geom_old, geom_new)
        #als roteren -> pas de rotatie van de betreffende feature aan op basis van de loodrechte lijn tussen muisklik en bestaand punt
        if self.startRotate:
            self.tempRubberBand.hide()
            clickedPt = self.toMapCoordinates(event.pos())
            tempGeometry = self.tempRubberBand.asGeometry().asPolyline()
            drawPoint = self.toLayerCoordinates(self.layer, tempGeometry[0])
            field_idx = self.idlayer.fields().indexOf("rotatie")
            rotation = int(drawPoint.azimuth(clickedPt))
            if field_idx != -1:
                self.idlayer.changeAttributeValue(self.fid, field_idx, rotation)
            field_idx = self.idlayer.fields().indexOf('applicatie')
            if field_idx != -1:
                self.idlayer.changeAttributeValue(self.fid, field_idx, 'OIV')
            self.idlayer.commitChanges()
            self.idlayer.triggerRepaint()
            self.stop_moveTool(rotation, None, None)

    def stop_moveTool(self, rotation, geom_old, geom_new):
        """reset rubberbands"""
        if self.tempRubberBand is not None:
            self.canvas.scene().removeItem(self.tempRubberBand)
            self.tempRubberBand = None
        if self.vertexmarker is not None:
            self.canvas.scene().removeItem(self.vertexmarker)
            self.vertexmarker = None
        if self.vertexMovemarker is not None:
            self.canvas.scene().removeItem(self.vertexMovemarker)
            self.vertexMovemarker = None
        self.fid = None
        self.point = None
        self.startRotate = False
        self.dragging = False
        self.onMoved(rotation, geom_old, geom_new, self.multi)
        self.canvas.refresh()
