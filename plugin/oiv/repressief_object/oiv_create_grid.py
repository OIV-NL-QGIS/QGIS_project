"""init the oiv base widget"""

import os
import math
import uuid

from qgis.PyQt import uic
from qgis.PyQt.QtGui import QColor
from qgis.PyQt.QtCore import Qt
from qgis.PyQt.QtWidgets import QDockWidget, QMessageBox, QProgressDialog, QProgressBar
from qgis.core import QgsGeometry, QgsFeature, QgsPointXY, QgsFeatureRequest, QgsRectangle, QgsPointXY, QgsWkbTypes
from qgis.core import QgsCoordinateReferenceSystem

from ..tools.utils_core import getlayer_byname, write_layer, read_settings
from ..tools.rubberbands import init_rubberband
from ..config_files.papersizesscale import PAPERTOPOLYGONRD, DEFAULTSCALE, PAPERSIZES, SINGLEGRIDSIZE

FORM_CLASS, _ = uic.loadUiType(os.path.join(
    os.path.dirname(__file__), 'oiv_create_grid_widget.ui'))

class oivGridWidget(QDockWidget, FORM_CLASS):
    """create dockwidget as base of the oiv plugin"""

    iface = None
    canvas = None
    objectWidget = None
    rubberBand = None
    xWidth = None
    yWidth = None
    gridUUID = None

    def __init__(self, parent=None):
        """Constructor."""
        super(oivGridWidget, self).__init__(parent)
        self.setupUi(self)
        self.initUI()

    def initUI(self):
        self.object_id.setVisible(False)
        self.kaartblad_frame.setVisible(False)
        self.grid_frame.setVisible(False)
        self.next.clicked.connect(self.run_grid)
        self.closewidget.clicked.connect(self.close_grid_open_repressief_object)
        self.delete_grid.clicked.connect(self.delete_existing_grid)
        self.scale_25000.toggled.connect(self.adjust_kaartblad_settings)
        self.scale_diff.toggled.connect(self.adjust_kaartblad_settings)

    def run_grid(self):
        if self.type_single_grid.isChecked():
            self.kaartblad_frame.setVisible(False)
            self.grid_frame.setVisible(True)
            self.make_grid.clicked.connect(self.create_grid)
        else:
            self.grid_frame.setVisible(False)
            self.kaartblad_frame.setVisible(True)
            self.format_combo.addItems(PAPERSIZES)
            self.preview.clicked.connect(self.create_preview)
            self.make_kaartblad.clicked.connect(lambda: self.create_kaartblad(True))
            self.make_kaartblad_only.clicked.connect(lambda: self.create_kaartblad(False))
            self.rubberBand = init_rubberband(QColor("red"), Qt.SolidLine, 10, 1, QgsWkbTypes.PolygonGeometry, self.canvas)

    def adjust_kaartblad_settings(self):
        if self.scale_25000.isChecked():
            self.distance_grid.setValue(SINGLEGRIDSIZE)
            self.distance_grid.setEnabled(False)
            self.scale_custom.setEnabled(False)
        else:
            self.distance_grid.setEnabled(True)
            self.scale_custom.setEnabled(True)

    def create_preview(self):
        self.canvas.mapCanvasRefreshed.connect(self.refresh_kaartblad)
        paperSize = self.format_combo.currentText()
        if self.scale_25000.isChecked():
            scale = DEFAULTSCALE
        else:
            scale = self.scale_custom.value()
        scaleRatio = scale/DEFAULTSCALE
        if self.orient_landscape.isChecked():
            orienTation = 'landscape'
        else:
            orienTation = 'portrait'
        self.xWidth = PAPERTOPOLYGONRD[paperSize][orienTation]['x_width'] * scaleRatio
        self.yWidth = PAPERTOPOLYGONRD[paperSize][orienTation]['y_width'] * scaleRatio
        self.refresh_kaartblad()

    def refresh_kaartblad(self):
        dist = self.distance_grid.value()
        extent = self.canvas.extent()
        xmin, xmax, ymin, ymax, xIt, yIt = self.calculate_extent(dist, extent)
        xmax = xmin + self.xWidth
        ymax = ymin + self.yWidth
        self.place_rubberband(xmin, xmax, ymin, ymax)

    def place_rubberband(self, xmin, xmax, ymin, ymax):
        try:
            self.rubberBand.reset()
            self.canvas.scene().removeItem(self.rubberBand)
        except:
            pass
        self.rubberBand = init_rubberband(QColor("red"), Qt.SolidLine, 10, 1, QgsWkbTypes.PolygonGeometry, self.canvas)
        tempRect = QgsRectangle(QgsPointXY(xmin, ymin), QgsPointXY(xmax, ymax))
        tempGeom = QgsGeometry.fromRect(tempRect)
        crs = QgsCoordinateReferenceSystem('EPSG:28992')
        self.rubberBand.reset()
        self.rubberBand.setToGeometry(tempGeom, crs)
        self.rubberBand.show()

    def create_kaartblad(self, withGrid):
        geom = self.rubberBand.asGeometry()
        geom.convertToMultiType()
        layerName = 'Grid'
        layer = getlayer_byname(layerName)
        targetFeature = QgsFeature()
        targetFields = layer.fields()
        targetFeature.initAttributes(targetFields.count())
        targetFeature.setFields(targetFields)
        targetFeature.setGeometry(geom)
        targetFeature["type"] = 'Kaartblad'
        if self.scale_25000.isChecked():
            targetFeature["scale"] = DEFAULTSCALE
        else:
            targetFeature["scale"] = self.scale_custom.value()
        targetFeature["papersize"] = self.format_combo.currentText()
        if self.orient_landscape.isChecked():
            targetFeature["orientation"] = 'landscape'
        else:
            targetFeature["orientation"] = 'portrait'
        query = "SELECT foreign_key FROM config_object WHERE child_layer = '{}'".format(layerName)
        foreignKey = read_settings(query, False)[0]
        targetFeature[foreignKey] = self.object_id.text()
        write_layer(layer, targetFeature)
        bbox = geom.boundingBox()
        dist = self.distance_grid.value()
        if withGrid:
            self.create_grid(dist, bbox, 'Kaartblad')
        self.canvas.scene().removeItem(self.rubberBand)

    def calculate_extent(self, dist, extent, gridType='Grid'):
        if gridType == 'Grid':
            xmin = int(extent.xMinimum()) - int(extent.xMinimum()) % SINGLEGRIDSIZE + SINGLEGRIDSIZE
            ymin = int(extent.yMinimum()) - int(extent.yMinimum()) % SINGLEGRIDSIZE + SINGLEGRIDSIZE
            xmax = int(extent.xMaximum()) - int(extent.xMaximum()) % dist
            ymax = int(extent.yMaximum()) - int(extent.yMaximum()) % dist
        else:
            xmin = extent.xMinimum()
            ymin = extent.yMinimum()
            xmax = extent.xMaximum()
            ymax = extent.yMaximum()
        xIt = int((xmax - xmin)/dist)
        yIt = int((ymax - ymin)/dist)
        if gridType == 'Kaartblad':
            if xmin + xIt * dist < extent.xMaximum():
                xIt += 1
            if ymin + yIt * dist < extent.yMaximum():
                yIt += 1
        return xmin, xmax, ymin, ymax, xIt, yIt

    def create_grid(self, dist=None, extent=None, gridType='Grid'):
        if not dist and not extent:
            extent = self.canvas.extent()
            dist = self.distance.value()
        layerName = 'Grid'
        layer = getlayer_byname(layerName)
        targetFeature = QgsFeature()
        targetFields = layer.fields()
        targetFeature.initAttributes(targetFields.count())
        targetFeature.setFields(targetFields)
        query = "SELECT foreign_key FROM config_object WHERE child_layer = '{}'".format(layerName)
        foreignKey = read_settings(query, False)[0]
        xmin, xmax, ymin, ymax, xIt, yIt = self.calculate_extent(dist, extent, gridType)
        objectId = self.object_id.text()
        targetFeature[foreignKey] = objectId
        targetFeature["type"] = 'Grid'
        for x in range(0, xIt):
            for y in range(0, yIt):
                yLabel = str(y + 1)
                if xIt < 26:
                    xLabel = chr(x + 97).upper()
                elif xIt >= 26:
                    xLabel = chr(int(math.floor(x/26)) + 97).upper() + chr(x % 26 + 97).upper()
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
                write_layer(layer, targetFeature)
        message = 'Het grid is succesvol aangemaakt!'
        QMessageBox.information(None, "INFO:", message)

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
        points.append(QgsPointXY(xmin + x * dist, ymin + y * dist))
        points.append(QgsPointXY(xmax, ymin + y * dist))
        points.append(QgsPointXY(xmax, ymax))
        points.append(QgsPointXY(xmin + x * dist, ymax))
        return QgsGeometry.fromMultiPolygonXY([[points]])

    def delete_existing_grid(self):
        layerName = 'Grid'
        layer = getlayer_byname(layerName)        
        objectId = self.object_id.text()
        request = QgsFeatureRequest().setFilterExpression('"object_id" = ' + str(objectId))
        featureIt = layer.getFeatures(request)
        reply = QMessageBox.question(self.iface.mainWindow(), 'Continue?',
                                     "Weet u zeker dat u het bestaande grid wilt weggooien?",
                                     QMessageBox.Yes, QMessageBox.No)
        if reply == QMessageBox.No:
            return "Exit"
        elif reply == QMessageBox.Yes:
            layer.startEditing()
            for feat in featureIt:
                layer.deleteFeature(feat.id())
            layer.commitChanges()
            return "Done"

    def close_grid_open_repressief_object(self):
        """close this gui and return to the main page"""
        try:
            self.closewidget.clicked.disconnect()
        except:
            pass
        try:
            self.make_grid.clicked.disconnect()
        except:
            pass
        try:
            self.next.clicked.disconnect()
        except:
            pass
        try:
            self.canvas.mapCanvasRefreshed.disconnect()
        except:
            pass
        try:
            self.preview.clicked.disconnect()
            self.make_kaartblad.disconnect()
        except:
            pass
        if self.rubberBand:
            self.canvas.scene().removeItem(self.rubberBand)
            self.rubberBand = None
        self.close()
        self.objectWidget.show()
        del self
