"""
/***************************************************************************
 oiv
                                 A QGIS plugin
 place oiv objects
                              -------------------
        begin                : 2019-08-15
        git sha              : $Format:%H$
        copyright            : (C) 2019 by Joost Deen
        email                : jdeen@vrnhn.nl
        versie               : 2.9.93
 ***************************************************************************/
/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""

import os
import webbrowser

from qgis.PyQt import uic
from qgis.PyQt.QtCore import Qt
from qgis.PyQt.QtWidgets import QDockWidget, QMessageBox

from qgis.core import QgsGeometry, QgsFeatureRequest
from qgis.utils import iface

from ..tools.utils_core import getlayer_byname, refresh_layers, get_possible_snapFeatures_object
from ..tools.utils_gui import set_lengte_oppervlakte_visibility, read_config_file
from ..tools.oiv_stackwidget import oivStackWidget
#from .tools.mapTool import CaptureTool
from .oiv_object_tekenen import oivObjectTekenWidget

FORM_CLASS, _ = uic.loadUiType(os.path.join(
    os.path.dirname(__file__), 'oiv_repressief_object_widget.ui'))

class oivRepressiefObjectWidget(QDockWidget, FORM_CLASS):
    """interactive UI management"""

    configFileObject = None
    iface = None
    canvas = None
    basewidget = None
    selectTool = None
    pointTool = None
    attributeform = None
    drawLayer = None
    identifier = None
    drawTool = None
    moveTool = None
    snapLayerNames = ["Object terrein", "Isolijnen", "Bereikbaarheid", "Sectoren"]
    tekensymbolenwidget = None

    def __init__(self, parent=None):
        super(oivRepressiefObjectWidget, self).__init__(parent)
        self.setupUi(self)
        self.iface = iface
        self.configFileObject = read_config_file("/config_files/csv/config_object.csv", None)
        self.stackwidget = oivStackWidget()
        self.tekensymbolenwidget = oivObjectTekenWidget()
        set_lengte_oppervlakte_visibility(self, False, False, False, False)

    def initActions(self):
        """connect the buttons to their actions"""
        self.terug.clicked.connect(self.close_repressief_object_show_base)
        self.objectgegevens.clicked.connect(self.run_objectgegevens_bewerken)
        self.terugmelden.clicked.connect(self.open_bgt_viewer)
        self.delete_f.clicked.connect(self.run_delete)
        self.object_tekenen.clicked.connect(self.object_terrein_tekenen)
        self.object_symbolen.clicked.connect(self.run_object_symbolen_tekenen)

    def close_repressief_object_show_base(self):
        """close this gui and return to the main page"""
        self.delete_f.clicked.disconnect()
        self.terug.clicked.disconnect()
        self.objectgegevens.clicked.disconnect()
        self.terugmelden.clicked.disconnect()
        self.object_tekenen.clicked.disconnect()
        try:
            del self.stackwidget
        except: # pylint: disable=bare-except
            pass
        self.close()
        self.basewidget.show()
        del self

    def activatePan(self):
        """activate pan to lose other draw features"""
        self.iface.actionPan().trigger()

    def run_objectgegevens_bewerken(self):
        """select bouwlaag on canvas to edit the atrribute form"""
        objectId = self.object_id.text()
        request = QgsFeatureRequest().setFilterExpression('"id" = ' + str(objectId))
        tempLayer = self.drawLayer
        objectFeature = next(tempLayer.getFeatures(request))
        self.iface.addDockWidget(Qt.RightDockWidgetArea, self.stackwidget)
        self.stackwidget.parentWidget = self
        self.stackwidget.open_feature_form(tempLayer, objectFeature)
        self.close()
        self.stackwidget.show()

    def open_bgt_viewer(self):
        """open url based on BGT location, i.v.m. terugmelden"""
        e = iface.mapCanvas().extent()
        gemx = (e.xMaximum() + e.xMinimum())/2
        gemy = (e.yMaximum() + e.yMinimum())/2
        url2 = 'https://verbeterdekaart.kadaster.nl/#?geometry.x=' + str(gemx) + '&geometry.y=' + str(gemy) + '&zoomlevel=12'
        webbrowser.open(url2)

    def run_delete(self):
        """delete repressief object"""
        ilayer = self.drawLayer
        self.iface.setActiveLayer(ilayer)
        objectId = self.object_id.text()
        request = QgsFeatureRequest().setFilterExpression('"id" = ' + str(objectId))
        ifeature = next(ilayer.getFeatures(request))
        ilayer.startEditing()
        ilayer.selectByIds([ifeature.id()])
        reply = QMessageBox.question(self.iface.mainWindow(), 'Continue?',
                                     "Weet u zeker dat u de geselecteerde feature wilt weggooien?",\
                                     QMessageBox.Yes, QMessageBox.No)
        if reply == QMessageBox.No:
            #als "nee" deselecteer alle geselecteerde features
            ilayer.selectByIds([])
        elif reply == QMessageBox.Yes:
            #als "ja" -> verwijder de feature op basis van het unieke feature id
            ilayer.deleteFeature(ifeature.id())
            ilayer.commitChanges()
            reply = QMessageBox.information(self.iface.mainWindow(), 'Succesvol!', "Het object is succesvol verwijderd.")
        refresh_layers(self.iface)
        self.close_repressief_object_show_base()

    def edit_attribute(self, ilayer, ifeature):
        """open het formulier van een feature in een dockwidget, zodat de attributen kunnen worden bewerkt"""
        self.iface.addDockWidget(Qt.RightDockWidgetArea, self.stackwidget)
        self.stackwidget.parentWidget = self
        self.stackwidget.open_feature_form(ilayer, ifeature)
        self.close()
        self.stackwidget.show()
        self.selectTool.geomSelected.disconnect(self.edit_attribute)

    def object_terrein_tekenen(self):
        """draw repressief object terrain"""
        objectId = self.object_id.text()
        possibleSnapFeatures = get_possible_snapFeatures_object(self.snapLayerNames, objectId)
        self.drawTool.parent = self
        self.drawTool.layer = self.drawLayer
        set_lengte_oppervlakte_visibility(self, True, True, True, True)
        self.drawTool.possibleSnapFeatures = possibleSnapFeatures
        self.drawTool.canvas = self.canvas
        self.drawTool.onGeometryAdded = self.place_object_terrein
        self.drawTool.captureMode = 2
        self.canvas.setMapTool(self.drawTool)

    def place_object_terrein(self, point, dummy):
        """save drawn terrain"""
        layer = getlayer_byname("Object terrein")
        self.iface.setActiveLayer(layer)
        objectId = int(self.object_id.text())
        iterator = self.drawLayer.getFeatures(QgsFeatureRequest().setFilterFid(objectId))
        feature = next(iterator)
        layer.dataProvider().changeGeometryValues({feature.id(): QgsGeometry.fromPolygonXY([point])})
        layer.commitChanges()
        layer.triggerRepaint()
        self.activatePan()

    def run_object_symbolen_tekenen(self):
        self.tekensymbolenwidget.canvas = self.canvas
        self.tekensymbolenwidget.selectTool = self.selectTool
        self.tekensymbolenwidget.pointTool = self.pointTool
        self.tekensymbolenwidget.drawTool = self.drawTool
        self.tekensymbolenwidget.moveTool = self.moveTool
        self.tekensymbolenwidget.repressiefobjectwidget = self
        self.tekensymbolenwidget.formelenaam.setText(self.formelenaam.text())
        self.tekensymbolenwidget.object_id.setText(self.object_id.text())
        self.iface.addDockWidget(Qt.RightDockWidgetArea, self.tekensymbolenwidget)
        self.tekensymbolenwidget.show()
        self.close()
