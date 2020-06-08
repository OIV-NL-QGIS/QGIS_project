"""
/***************************************************************************
 oiv
                                 A QGIS plugin
 place oiv objects
                              -------------------
        begin                : 2019-08-15
        git sha              : $Format:%H$
        copyright            : (C) 2019 by Joost Deen
        email                : j.deen@safetyct.com
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

from ..tools.utils_core import getlayer_byname, refresh_layers, get_possible_snapFeatures_object, construct_feature, write_layer, get_attributes
from ..tools.utils_gui import set_lengte_oppervlakte_visibility
from ..tools.editFeature import delete_feature
from ..tools.oiv_stackwidget import oivStackWidget
from ..tools.oiv_import_file import oivImportFileWidget
from .oiv_object_tekenen import oivObjectTekenWidget
from .oiv_create_grid import oivGridWidget

FORM_CLASS, _ = uic.loadUiType(os.path.join(
    os.path.dirname(__file__), 'oiv_repressief_object_widget.ui'))

class oivRepressiefObjectWidget(QDockWidget, FORM_CLASS):
    """interactive UI management"""

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
    importwidget = None
    gridWidget = None

    def __init__(self, parent=None):
        super(oivRepressiefObjectWidget, self).__init__(parent)
        self.setupUi(self)
        self.iface = iface
        self.stackwidget = oivStackWidget()
        self.tekensymbolenwidget = oivObjectTekenWidget()
        self.object_id.setVisible(False)
        set_lengte_oppervlakte_visibility(self, False, False, False, False)

    def initActions(self):
        """connect the buttons to their actions"""
        self.identify.setVisible(False)
        self.delete_f.setVisible(False)
        self.pan.setVisible(False)
        self.terrein_tekenen.setVisible(False)
        self.terug.clicked.connect(self.close_repressief_object_show_base)
        self.objectgegevens.clicked.connect(self.run_objectgegevens_bewerken)
        self.terugmelden.clicked.connect(self.open_bgt_viewer)
        self.delete_object.clicked.connect(self.run_delete_object)
        self.terrein_bewerken.clicked.connect(self.object_terrein_bewerken)
        self.object_symbolen.clicked.connect(self.run_object_symbolen_tekenen)
        self.create_grid.clicked.connect(self.run_create_grid)
        self.import_drawing.clicked.connect(self.run_import)

    def close_repressief_object_show_base(self):
        """close this gui and return to the main page"""
        self.delete_object.clicked.disconnect()
        self.terug.clicked.disconnect()
        self.objectgegevens.clicked.disconnect()
        self.terugmelden.clicked.disconnect()
        self.terrein_bewerken.clicked.disconnect()
        try:
            self.terrein_tekenen.clicked.disconnect()
            self.delete_f.clicked.disconnect()
            self.pan.clicked.disconnect()
        except: # pylint: disable=bare-except
            pass
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
        self.edit_attribute(tempLayer, objectFeature)

    def open_bgt_viewer(self):
        """open url based on BGT location, i.v.m. terugmelden"""
        e = iface.mapCanvas().extent()
        gemx = (e.xMaximum() + e.xMinimum())/2
        gemy = (e.yMaximum() + e.yMinimum())/2
        url2 = 'https://verbeterdekaart.kadaster.nl/#?geometry.x=' + str(gemx) + '&geometry.y=' + str(gemy) + '&zoomlevel=12'
        webbrowser.open(url2)

    def run_delete_object(self):
        """delete repressief object"""
        ilayer = self.drawLayer
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
        try:
            self.selectTool.geomSelected.disconnect(self.edit_attribute)
        except: # pylint: disable=bare-except
            pass

    def object_terrein_bewerken(self):
        """draw repressief object terrain"""
        self.identify.setVisible(True)
        self.delete_f.setVisible(True)
        self.pan.setVisible(True)
        self.terrein_tekenen.setVisible(True)
        self.terrein_tekenen.clicked.connect(self.run_terrein_toevoegen)
        self.delete_f.clicked.connect(self.run_delete_terrein)
        self.pan.clicked.connect(self.activatePan)
        self.identify.clicked.connect(self.edit_feature)

    def edit_feature(self):
        self.selectTool.whichConfig = 'config_object'
        self.canvas.setMapTool(self.selectTool)
        self.selectTool.geomSelected.connect(self.edit_attribute)

    def run_create_grid(self):
        self.gridWidget = oivGridWidget()
        self.gridWidget.object_id.setText(self.object_id.text())
        self.gridWidget.canvas = self.canvas
        self.gridWidget.iface = self.iface
        self.gridWidget.objectWidget = self
        self.iface.addDockWidget(Qt.RightDockWidgetArea, self.gridWidget)
        self.gridWidget.show()
        self.close()

    def run_terrein_toevoegen(self):
        objectId = self.object_id.text()
        possibleSnapFeatures = get_possible_snapFeatures_object(self.snapLayerNames, objectId)
        self.drawTool.parent = self
        self.drawTool.layer = getlayer_byname("Object terrein")
        set_lengte_oppervlakte_visibility(self, True, True, True, True)
        self.drawTool.possibleSnapFeatures = possibleSnapFeatures
        self.drawTool.canvas = self.canvas
        self.drawTool.onGeometryAdded = self.place_object_terrein
        self.drawTool.captureMode = 2
        self.canvas.setMapTool(self.drawTool)

    def run_delete_terrein(self):
        self.selectTool.whichConfig = 'config_object'
        self.canvas.setMapTool(self.selectTool)
        self.selectTool.geomSelected.connect(self.delete)

    def delete(self, ilayer, ifeature):
        deleteLayerNames = ['Objecten', 'Object terrein']
        reply = delete_feature(ilayer, ifeature, deleteLayerNames, self.iface)
        if reply == 'Retry':
            self.run_delete_terrein()
        self.selectTool.geomSelected.disconnect(self.delete)

    def place_object_terrein(self, points, dummy):
        """save drawn terrain"""
        layer = getlayer_byname("Object terrein")
        if points:
            parentId, childFeature = construct_feature('Polygon', 'Objecten', points, self.object_id.text(), self.iface)
        if parentId is not None:
            buttonCheck = get_attributes(parentId, childFeature, None, None, layer, 'config_object')
            if buttonCheck != 'Cancel':
                write_layer(layer, childFeature)
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

    def run_import(self):
        """initiate import widget"""
        self.importwidget = oivImportFileWidget()
        self.importwidget.parentWidget = self
        self.importwidget.object_id.setText(self.object_id.text())
        self.importwidget.object.setText(self.formelenaam.text())
        #self.importwidget.selectTool = self.selectTool
        self.importwidget.canvas = self.canvas
        self.iface.addDockWidget(Qt.RightDockWidgetArea, self.importwidget)
        self.close()
        self.importwidget.show()
 