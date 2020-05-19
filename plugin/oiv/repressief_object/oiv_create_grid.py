"""init the oiv base widget"""

import os
import math

from qgis.PyQt import uic
from qgis.PyQt.QtWidgets import QDockWidget, QMessageBox, QProgressDialog, QProgressBar
from qgis.core import QgsGeometry, QgsFeature, QgsPointXY, QgsFeatureRequest

from ..tools.utils_core import getlayer_byname, write_layer, read_settings

FORM_CLASS, _ = uic.loadUiType(os.path.join(
    os.path.dirname(__file__), 'oiv_create_grid_widget.ui'))

class oivGridWidget(QDockWidget, FORM_CLASS):
    """create dockwidget as base of the oiv plugin"""

    iface = None
    canvas = None
    objectWidget = None

    def __init__(self, parent=None):
        """Constructor."""
        super(oivGridWidget, self).__init__(parent)
        self.setupUi(self)
        self.closewidget.clicked.connect(self.close_grid_open_repressief_object)
        self.make_grid.clicked.connect(self.create_grid)
        self.delete_grid.clicked.connect(self.delete_existing_grid)
        self.object_id.setVisible(False)

    def calculate_extent(self):
        dist = self.distance.value()
        extent = self.canvas.extent()
        xmin = int(extent.xMinimum()) - int(extent.xMinimum()) % dist + dist
        xmax = int(extent.xMaximum()) - int(extent.xMaximum()) % dist
        ymin = int(extent.yMinimum()) - int(extent.yMinimum()) % dist + dist
        ymax = int(extent.yMaximum()) - int(extent.yMaximum()) % dist
        xIt = int((xmax - xmin)/dist)
        yIt = int((ymax - ymin)/dist)
        return xmin, ymax, xIt, yIt

    def create_grid(self):
        dist = self.distance.value()
        layerName = 'Grid'
        layer = getlayer_byname(layerName)
        targetFeature = QgsFeature()        
        targetFields = layer.fields()
        targetFeature.initAttributes(targetFields.count())
        targetFeature.setFields(targetFields)      
        query = "SELECT foreign_key FROM config_object WHERE child_layer = '{}'".format(layerName)
        foreignKey = read_settings(query, False)[0]
        xmin, ymax, xIt, yIt = self.calculate_extent()
        objectId = self.object_id.text()
        targetFeature[foreignKey] = objectId
        for x in range(0, xIt):
            for y in range(0, yIt):
                yLabel = str(yIt - y)
                if xIt < 26:
                    xLabel = chr(x + 97).upper()
                elif xIt >= 26:
                    xLabel = chr(int(math.floor(x/26)) + 97).upper() + chr(x % 26 + 97).upper()
                geom = self.calculate_geometry(dist, xmin, ymax, x, y)
                targetFeature['vaknummer'] = xLabel + yLabel
                if x != 0:
                    yLabel = ''
                if y != yIt - 1:
                    xLabel = ''
                targetFeature.setGeometry(geom)
                targetFeature['y_as_label'] = yLabel
                targetFeature['x_as_label'] = xLabel
                targetFeature['afstand'] = dist
                write_layer(layer, targetFeature)
        message = 'Het grid is succesvol aangemaakt!'
        QMessageBox.information(None, "INFO:", message)

    def calculate_geometry(self, dist, xmin, ymax, x, y):
        """calculate grid polygons"""
        points = []
        points.append(QgsPointXY(xmin + x * dist, ymax - y * dist))
        points.append(QgsPointXY(xmin + (x + 1) * dist, ymax - y * dist))
        points.append(QgsPointXY(xmin + (x + 1) * dist, ymax - (y + 1) * dist))
        points.append(QgsPointXY(xmin + x * dist, ymax - (y + 1) * dist))
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
        self.closewidget.clicked.disconnect()
        self.make_grid.clicked.disconnect()
        self.close()
        self.objectWidget.show()
        del self
