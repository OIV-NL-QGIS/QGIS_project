# -*- coding: utf-8 -*-
"""
/***************************************************************************
 oivTekenWidget
                                 A QGIS plugin
 place oiv objects
                             -------------------
        begin                : 2017-11-14
        git sha              : $Format:%H$
        copyright            : (C) 2017 by Joost Deen
        email                : jdeen@vrnhn.nl
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

from qgis.PyQt import uic
from qgis.PyQt.QtCore import Qt
from qgis.PyQt.QtWidgets import QDockWidget, QCheckBox, QMessageBox

from qgis.utils import iface
from qgis.core import QgsFeature, QgsGeometry, QgsFeatureRequest

from ..tools.utils_core import getlayer_byname, get_draw_layer_attr, write_layer, set_layer_substring, get_possible_snapFeatures_bouwlaag
from ..tools.utils_gui import set_lengte_oppervlakte_visibility, read_config_file

FORM_CLASS, _ = uic.loadUiType(os.path.join(
    os.path.dirname(__file__), 'oiv_bouwlaag_widget.ui'))

class oivBouwlaagWidget(QDockWidget, FORM_CLASS):
    """create bouwlaag from BAG, copy or draw"""

    canvas = None
    iface = None
    layer = None
    selectTool = None
    drawTool = None
    objectId = None
    objectwidget = None
    bouwlaagList = []
    snapLayerNames = ["Bouwlagen", "BAG panden", "Bouwkundige veiligheidsvoorzieningen", "Ruimten"]

    def __init__(self, parent=None):
        """initialize dockwidget and connect slots and signals"""
        super(oivBouwlaagWidget, self).__init__(parent)
        self.setupUi(self)
        self.iface = iface
        self.configFileBouwlaag = read_config_file("/config_files/csv/config_bouwlaag.csv", None)
        self.bouwlaag_bag.clicked.connect(self.run_bag_overnemen)
        self.bouwlaag_tekenen.clicked.connect(self.run_bouwlaag_tekenen)
        self.bouwlaag_overnemen.clicked.connect(self.run_bouwlaag_overnemen)
        self.terug.clicked.connect(self.close_bouwlaag)
        self.copy.clicked.connect(self.run_select_bouwlaag)

        self.label1.setVisible(False)
        self.label2.setVisible(False)
        self.label3.setVisible(False)
        set_lengte_oppervlakte_visibility(self, False, False, False, False)
        self.bouwlaag_max.setVisible(False)
        self.bouwlaag.setVisible(False)
        self.copy.setVisible(False)

        for var in vars(self):
            typeVar = type(vars(self)[var])
            if typeVar == QCheckBox:
                vars(self)[var].setVisible(False)

    def run_bag_overnemen(self):
        """copy polygon of bag feature"""
        set_lengte_oppervlakte_visibility(self, False, False, False, False)
        layerName = "BAG panden"
        ilayer = getlayer_byname(layerName)
        request = QgsFeatureRequest().setFilterExpression('"identificatie" = ' + str(self.objectId))
        ifeature = next(ilayer.getFeatures(request))
        self.copy_bag_bouwlaag(ilayer, ifeature)

    def run_bouwlaag_overnemen(self):
        """copy floor from another floor"""
        set_lengte_oppervlakte_visibility(self, False, False, False, False)
        self.label1.setVisible(True)
        self.label2.setVisible(True)
        self.label3.setVisible(True)
        self.bouwlaag.setVisible(True)
        for var in vars(self):
            typeVar = type(vars(self)[var])
            if typeVar == QCheckBox:
                vars(self)[var].setVisible(True)
        #append combobox with unique existing floors
        self.bouwlagen_to_combobox()
        self.copy.setVisible(True)
        #connect signal to slot
        self.bouwlaag.currentIndexChanged.connect(self.set_layer_subset_bouwlaag)
        self.selectTool.geomSelected.connect(self.copy_bag_bouwlaag)

    def run_bouwlaag_tekenen(self):
        """draw a floor with the basic functionality of QGIS"""
        possibleSnapFeatures = get_possible_snapFeatures_bouwlaag(self.snapLayerNames, self.objectId)
        layer = getlayer_byname('Bouwlagen')
        self.drawTool.layer = layer
        self.drawTool.possibleSnapFeatures = possibleSnapFeatures
        self.drawTool.canvas = self.canvas
        self.drawTool.onGeometryAdded = self.draw_feature
        self.drawTool.captureMode = 2
        self.canvas.setMapTool(self.drawTool)
        set_lengte_oppervlakte_visibility(self, True, True, True, True)
        self.drawTool.parent = self

    def run_select_bouwlaag(self):
        """set selecttool as maptool"""
        self.canvas.setMapTool(self.selectTool)

    def set_layer_subset_bouwlaag(self):
        """set layers substring which are a childlayer of "bouwlagen"""
        comboboxText = str(self.bouwlaag.currentText())
        if comboboxText != "":
            sub_string = "bouwlaag = " + str(self.bouwlaag.currentText())
            set_layer_substring(self.configFileBouwlaag, sub_string)            

    def copy_layers(self, parentID, newID, layer, bouwlaag):
        """select the features"""
        fields = layer.fields()
        newFeature = QgsFeature()
        newFeature.initAttributes(fields.count())
        newFeature.setFields(fields)
        attrs = {"foreign_key" : '', "identifier" : '', "input_label" : '', "rotatie" : ''}
        attrs = get_draw_layer_attr(attrs, layer.name(), self.configFileBouwlaag)
        #get features by bouwlaag ID
        request = attrs["foreign_key"] + '=' + str(parentID)
        it = layer.getFeatures(QgsFeatureRequest().setFilterExpression(request))
        for feat in it:
            newFeature.setGeometry(feat.geometry())
            if attrs["identifier"] != '':
                if str(feat[attrs["identifier"]]).isdigit():
                    newFeature[attrs["identifier"]] = int(feat[attrs["identifier"]])
                else:
                    newFeature[attrs["identifier"]] = feat[attrs["identifier"]]
            if attrs["input_label"] != '':
                newFeature[attrs["input_label"]] = feat[attrs["input_label"]]
            if attrs["rotatie"] != '':
                newFeature[attrs["rotatie"]] = feat[attrs["rotatie"]]
            newFeature[attrs["foreign_key"]] = int(newID)
            newFeature["bouwlaag"] = bouwlaag
            write_layer(layer, newFeature)

    def copy_selected_layers(self, ifeature, newFeatureId, bouwlaag):
        """copy related selected features"""
        bouwlaagID = ifeature["id"]
        for var in vars(self):
            typeVar = type(vars(self)[var])
            if typeVar == QCheckBox:
                if vars(self)[var].isChecked():
                    copyLayer = getlayer_byname(vars(self)[var].text())
                    self.copy_layers(bouwlaagID, newFeatureId, copyLayer, bouwlaag) 

    def draw_feature(self, points, dummy):
        """create the floor feature and save to the floors layer"""
        minBouwlaag = int(self.bouwlaag_min.text())
        maxBouwlaag = int(self.bouwlaag_max.text())
        childFeature = QgsFeature()
        layerName = 'Bouwlagen'
        layer = getlayer_byname(layerName)
        attrs = {"foreign_key" : ''}
        attrs = get_draw_layer_attr(attrs, layerName, self.configFileBouwlaag)
        self.iface.setActiveLayer(layer)
        #construct QgsFeature to save
        for i in range(minBouwlaag, maxBouwlaag + 1):
            if i != 0:
                childFeature.setGeometry(QgsGeometry.fromPolygonXY([points]))
                fields = layer.fields()
                childFeature.initAttributes(fields.count())
                childFeature.setFields(fields)
                childFeature[attrs["foreign_key"]] = self.objectId
                childFeature["bouwlaag"] = i
                dummy = write_layer(layer, childFeature)
                #block the signals of changing the comboBox to add the new floor
                self.bouwlaag.blockSignals(True)
                self.bouwlaag.clear()
                if i not in self.bouwlaagList:
                    self.bouwlaagList.append(i)
        self.bouwlaagList.sort()
        self.bouwlagen_to_combobox()
        self.bouwlaag.blockSignals(False)
        self.iface.actionPan().trigger()
        #set all layers substring to the right floor
        sub_string = "bouwlaag = " + str(minBouwlaag)
        set_layer_substring(self.configFileBouwlaag, sub_string)
        if maxBouwlaag != minBouwlaag:
            QMessageBox.information(None, "Gereed!", "Alle bouwlagen zijn succesvol aangemaakt!")

    def copy_bag_bouwlaag(self, ilayer, ifeature):
        """copy the floor drom the BAG features"""
        if ilayer.name() == 'Bouwlagen' or ilayer.name() == 'BAG panden':
            childFeature = QgsFeature()
            layerName = 'Bouwlagen'
            #get active floor from dockwidget
            minBouwlaag = int(self.bouwlaag_min.text())
            maxBouwlaag = int(self.bouwlaag_max.text())
            layer = getlayer_byname(layerName)
            #get necessary attributes from config file
            attrs = {"foreign_key" : ''}
            attrs = get_draw_layer_attr(attrs, layerName, self.configFileBouwlaag)
            self.iface.setActiveLayer(layer)
            #construct QgsFeature to save
            for i in range(minBouwlaag, maxBouwlaag + 1):
                if i != 0:
                    childFeature.setGeometry(ifeature.geometry())
                    fields = layer.fields()
                    childFeature.initAttributes(fields.count())
                    childFeature.setFields(fields)
                    childFeature[attrs["foreign_key"]] = self.objectId
                    childFeature["bouwlaag"] = i
                    newFeatureId = write_layer(layer, childFeature)
                    #copy also the selected layers
                    if ilayer.name() == "Bouwlagen":
                        self.copy_selected_layers(ifeature, newFeatureId, i)
                    #block the signals of changing the comboBox to add the new floor
                    self.bouwlaag.blockSignals(True)
                    self.bouwlaag.clear()        
                    if i not in self.bouwlaagList:
                        self.bouwlaagList.append(i)
            self.bouwlaagList.sort()
            self.bouwlagen_to_combobox()           
            self.bouwlaag.blockSignals(False)
            self.iface.actionPan().trigger()
            #set all layers substring to the right floor
            sub_string = "bouwlaag = " + str(minBouwlaag)
            set_layer_substring(self.configFileBouwlaag, sub_string)
            try:
                self.selectTool.geomSelected.disconnect()
            except:  # pylint: disable=bare-except
                pass
            if maxBouwlaag >= minBouwlaag:
                QMessageBox.information(None, "Gereed!", "Alle bouwlagen zijn succesvol aangemaakt!")
        else:
            QMessageBox.information(None, "Oeps:", "U heeft geen bouwlaag aangeklikt, selecteer opnieuw.")
            try:
                self.selectTool.geomSelected.disconnect()
            except:  # pylint: disable=bare-except
                pass
            self.selectTool.geomSelected.connect(self.copy_bag_bouwlaag)

    def bouwlagen_to_combobox(self):
        """add existing floors to the comboBox of the "bouwlaagdockwidget"""
        self.bouwlaag.blockSignals(True)
        self.bouwlaag.clear()
        for i in range(len(self.bouwlaagList) + 1):
            if i == 0:
                self.bouwlaag.addItem("")
            else:
                self.bouwlaag.addItem(str(self.bouwlaagList[i - 1]))
        self.bouwlaag.blockSignals(False)
        index = self.bouwlaag.findText(str(self.bouwlaag_min.text()), Qt.MatchFixedString)
        if index >= 0:
            self.bouwlaag.setCurrentIndex(index)
        else:
            self.bouwlaag.setCurrentIndex(0)

    def close_bouwlaag(self):
        """close floor widget and return to main menu"""
        self.label1.setVisible(False)
        self.label2.setVisible(False)
        self.label3.setVisible(False)
        self.bouwlaag.setVisible(False)
        self.copy.setVisible(False)
        for var in vars(self):
            typeVar = type(vars(self)[var])
            if typeVar == QCheckBox:
                vars(self)[var].setVisible(False)
        self.objectwidget.sortedList = self.bouwlaagList
        self.objectwidget.bouwlagen_to_combobox(self.objectId, int(self.bouwlaag_min.text()))
        self.objectwidget.show()
        self.close()
        try:
            del self.objectwidget
        except:  # pylint: disable=bare-except
            pass
        del self
