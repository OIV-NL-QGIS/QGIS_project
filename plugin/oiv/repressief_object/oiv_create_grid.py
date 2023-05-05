"""creating grid and/or kaartblad"""
import os
import math
import uuid

from qgis.PyQt import uic
import qgis.PyQt.QtWidgets as PQtW
import qgis.core as QC

import oiv.helpers.grid_helpers as GH
import oiv.helpers.rubberband_helper as RH
import oiv.helpers.messages as MSG
import oiv.helpers.configdb_helper as CH
import oiv.helpers.constants as PC
import oiv.helpers.qt_helper as QT
import oiv.helpers.utils_core as UC

FORM_CLASS, _ = uic.loadUiType(os.path.join(
    os.path.dirname(__file__), PC.OBJECT["gridwidgetui"]))


class oivGridWidget(PQtW.QDockWidget, FORM_CLASS):
    """create dockwidget for creating grid and/or kaartblad"""

    rubberBand = None
    xWidth = 0
    yWidth = 0
    parent = None
    objectId = None

    def __init__(self, parent=None):
        """Constructor."""
        super(oivGridWidget, self).__init__(parent)
        self.setupUi(self)
        self.parent = parent
        self.canvas = parent.canvas
        self.iface = parent.iface
        self.objectId = self.parent.object_id.text()
        self.initUI()

    def initUI(self):
        """setup initial GUI fow widget"""
        self.object_id.setVisible(False)
        self.kaartblad_frame.setVisible(False)
        self.grid_frame.setVisible(False)
        self.next.clicked.connect(self.run_grid)
        self.closewidget.clicked.connect(self.close_grid_open_repressief_object)
        self.delete_grid.clicked.connect(self.run_delete_tool)
        self.scale_25000.toggled.connect(self.adjust_kaartblad_settings)
        self.scale_diff.toggled.connect(self.adjust_kaartblad_settings)

    def run_grid(self):
        """after choosing single grid or kaartblad set things in motion"""
        self.next.setEnabled(False)
        if self.type_single_grid.isChecked():
            self.kaartblad_frame.setVisible(False)
            self.grid_frame.setVisible(True)
            self.make_grid.clicked.connect(self.create_grid)
        else:
            self.grid_frame.setVisible(False)
            self.kaartblad_frame.setVisible(True)
            self.format_combo.addItems(GH.PAPERSIZES)
            self.preview.clicked.connect(self.create_preview)
            self.make_kaartblad.clicked.connect(lambda: self.create_kaartblad(True))
            self.make_kaartblad_only.clicked.connect(lambda: self.create_kaartblad(False))
            self.rubberBand = RH.init_rubberband('grid', self.canvas, 'polygon')

    def adjust_kaartblad_settings(self):
        """adjust GUI based on users choice"""
        if self.scale_25000.isChecked():
            self.distance_grid.setValue(GH.SINGLEGRIDSIZE)
            self.distance_grid.setEnabled(False)
            self.scale_custom.setEnabled(False)
        else:
            self.distance_grid.setEnabled(True)
            self.scale_custom.setEnabled(True)

    def create_preview(self):
        """create kaartblad preview on the canvas"""
        self.canvas.mapCanvasRefreshed.connect(self.refresh_kaartblad)
        paperSize = self.format_combo.currentText()
        if self.scale_25000.isChecked():
            scale = GH.DEFAULTSCALE
        else:
            scale = self.scale_custom.value()
        scaleRatio = scale/GH.DEFAULTSCALE
        if self.orient_landscape.isChecked():
            orienTation = 'landscape'
        else:
            orienTation = 'portrait'
        self.xWidth = GH.PAPERTOPOLYGONRD[paperSize][orienTation]['x_width'] * scaleRatio
        self.yWidth = GH.PAPERTOPOLYGONRD[paperSize][orienTation]['y_width'] * scaleRatio
        self.refresh_kaartblad()

    def refresh_kaartblad(self):
        """replace rubberband when user pans or zooms canvas"""
        dist = self.distance_grid.value()
        extent = self.canvas.extent()
        xmin, xmax, ymin, ymax, dummy, dummy = self.calculate_extent(dist, extent)
        xmax = xmin + self.xWidth
        ymax = ymin + self.yWidth
        self.place_rubberband(xmin, xmax, ymin, ymax)

    def place_rubberband(self, xmin, xmax, ymin, ymax):
        """place rubberband on the canvas"""
        try:
            self.rubberBand.reset()
            self.canvas.scene().removeItem(self.rubberBand)
        except: #pylint: disable=bare-except
            pass
        self.rubberBand = RH.init_rubberband('grid', self.canvas, 'polygon')
        tempRect = QC.QgsRectangle(QC.QgsPointXY(xmin, ymin), QC.QgsPointXY(xmax, ymax))
        tempGeom = QC.QgsGeometry.fromRect(tempRect)
        crs = QC.QgsCoordinateReferenceSystem(GH.PROJECTCRS)
        self.rubberBand.reset()
        self.rubberBand.setToGeometry(tempGeom, crs)
        self.rubberBand.show()

    def create_kaartblad(self, withGrid):
        gridUUID = uuid.uuid4()
        geom = self.rubberBand.asGeometry()
        geom.convertToMultiType()
        layerName = PC.OBJECT["gridlayername"]
        layer = UC.getlayer_byname(layerName)
        targetFeature = QC.QgsFeature()
        targetFields = layer.fields()
        targetFeature.initAttributes(targetFields.count())
        targetFeature.setFields(targetFields)
        targetFeature.setGeometry(geom)
        targetFeature["type"] = 'Kaartblad'
        if self.scale_25000.isChecked():
            targetFeature["scale"] = GH.DEFAULTSCALE
        else:
            targetFeature["scale"] = self.scale_custom.value()
        targetFeature["papersize"] = self.format_combo.currentText()
        if self.orient_landscape.isChecked():
            targetFeature["orientation"] = 'landscape'
        else:
            targetFeature["orientation"] = 'portrait'
        targetFeature["uuid"] = str(gridUUID)
        foreignKey = CH.get_foreign_key_ob(layerName)
        targetFeature[foreignKey] = self.objectId
        UC.write_layer(layer, targetFeature)
        bbox = geom.boundingBox()
        dist = self.distance_grid.value()
        if withGrid:
            self.create_grid(gridUUID, dist, bbox, 'Kaartblad')
        self.canvas.scene().removeItem(self.rubberBand)

    def calculate_extent(self, dist, extent, gridType='Grid'):
        if gridType == 'Grid':
            xmin = int(extent.xMinimum()) - int(extent.xMinimum()) % dist + dist
            ymin = int(extent.yMinimum()) - int(extent.yMinimum()) % dist + dist
            xmax = int(extent.xMaximum()) - int(extent.xMaximum()) % dist
            ymax = int(extent.yMaximum()) - int(extent.yMaximum()) % dist
        else:
            xmin = extent.xMinimum()
            ymin = extent.yMinimum()
            xmax = extent.xMaximum()
            ymax = extent.yMaximum()
        xIt = int((xmax - xmin) / dist)
        yIt = int((ymax - ymin) / dist)
        if gridType == 'Kaartblad':
            if xmin + xIt * dist < extent.xMaximum():
                xIt += 1
            if ymin + yIt * dist < extent.yMaximum():
                yIt += 1
        return xmin, xmax, ymin, ymax, xIt, yIt

    def create_grid(self, gridUUID=None, dist=None, extent=None, gridType='Grid'):
        if not gridUUID:
            gridUUID = uuid.uuid4()
        if not dist and not extent:
            extent = self.canvas.extent()
            dist = self.distance.value()
        layerName = PC.OBJECT["gridlayername"]
        layer = UC.getlayer_byname(layerName)
        targetFeature = QC.QgsFeature()
        targetFields = layer.fields()
        targetFeature.initAttributes(targetFields.count())
        targetFeature.setFields(targetFields)
        foreignKey = CH.get_foreign_key_ob(layerName)
        xmin, dummy, ymin, dummy, xIt, yIt = self.calculate_extent(dist, extent, gridType)
        objectId = self.objectId
        targetFeature[foreignKey] = objectId
        targetFeature["type"] = 'Grid'
        for x in range(0, xIt):
            for y in range(0, yIt):
                yLabel = str(y + 1)
                if xIt < 26:
                    xLabel = chr(x + 97).upper()
                elif xIt >= 26:
                    xLabel = chr(int(math.floor(x / 26)) + 97).upper() + chr(x % 26 + 97).upper()
                geom = self.calculate_geometry(dist, xmin, ymin, x, y, gridType)
                targetFeature['vaknummer'] = xLabel + yLabel
                if x != 0:
                    yLabel = ''
                if y != 0:
                    xLabel = ''
                targetFeature.setGeometry(geom)
                targetFeature['y_as_label'] = yLabel
                targetFeature['x_as_label'] = xLabel
                targetFeature['afstand'] = dist
                targetFeature["uuid"] = str(gridUUID)
                UC.write_layer(layer, targetFeature)
        MSG.showMsgBox('gridcreated')

    def calculate_geometry(self, dist, xmin, ymin, x, y, gridType):
        """calculate grid polygons"""
        points = []
        if (x + 1) * dist > self.xWidth and gridType == 'Kaartblad':
            xmax = xmin + x * dist + (self.xWidth - x * dist)
        else:
            xmax = xmin + (x + 1) * dist
        if (y + 1) * dist > self.yWidth and gridType == 'Kaartblad':
            ymax = ymin + y * dist + (self.yWidth - y * dist)
        else:
            ymax = ymin + (y + 1) * dist
        points.append(QC.QgsPointXY(xmin + x * dist, ymin + y * dist))
        points.append(QC.QgsPointXY(xmax, ymin + y * dist))
        points.append(QC.QgsPointXY(xmax, ymax))
        points.append(QC.QgsPointXY(xmin + x * dist, ymax))
        return QC.QgsGeometry.fromMultiPolygonXY([[points]])

    def delete_existing_grid(self, gridUUID, layer):
        request = QC.QgsFeatureRequest().setFilterExpression('"uuid" = ' + "'{}'".format(gridUUID))
        featureIt = layer.getFeatures(request)
        reply = MSG.showMsgBox('deletegrid')
        if reply:
            layer.startEditing()
            for feat in featureIt:
                layer.deleteFeature(feat.id())
            layer.commitChanges()
            return "Done"
        return "Exit"

    def run_delete_tool(self):
        MSG.showMsgBox('selectgrid')
        self.canvas.setMapTool(self.parent.identifyTool)
        self.parent.identifyTool.geomIdentified.connect(self.delete)

    def delete(self, ilayer, ifeature):
        """delete a feature"""
        if ilayer:
            if ilayer.name() == PC.OBJECT["gridlayername"]:
                gridUUID = ifeature["uuid"]
                self.delete_existing_grid(gridUUID, ilayer)
            else:
                MSG.showMsgBox('nogridselected')
                self.run_delete_tool()
        self.parent.identifyTool.geomIdentified.disconnect(self.delete)
        self.iface.actionPan().trigger()

    def close_grid_open_repressief_object(self):
        """close this gui and return to the main page"""
        try:
            self.closewidget.clicked.disconnect()
        except: #pylint: disable=bare-except
            pass
        try:
            self.make_grid.clicked.disconnect()
        except: #pylint: disable=bare-except
            pass
        try:
            self.next.clicked.disconnect()
        except: #pylint: disable=bare-except
            pass
        try:
            self.canvas.mapCanvasRefreshed.disconnect()
        except: #pylint: disable=bare-except
            pass
        try:
            self.preview.clicked.disconnect()
            self.make_kaartblad.disconnect()
        except: #pylint: disable=bare-except
            pass
        if self.rubberBand:
            self.canvas.scene().removeItem(self.rubberBand)
            self.rubberBand = None
        self.close()
        self.parent.show_subwidget(False)
        del self
