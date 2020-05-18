"""
/***************************************************************************
 oiv
                                 A QGIS plugin
 place oiv objects
                              -------------------
        begin                : 2019-08-15
        git sha              : $Format:%H$
        copyright            : (C) 2019 by Joost Deen
        email                : jdeen@safetyct.com
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
from qgis.PyQt.QtWidgets import QDockWidget, QPushButton, QMessageBox
from qgis.PyQt.QtCore import Qt

from qgis.core import QgsFeature, QgsGeometry, QgsFeatureRequest
from qgis.utils import iface

from ..tools.utils_core import check_layer_type, get_draw_layer_attr, getlayer_byname, write_layer, get_attributes
from ..tools.utils_core import get_possible_snapFeatures_bouwlaag, construct_feature
from ..tools.utils_gui import read_config_file, get_actions, set_lengte_oppervlakte_visibility
from ..tools.oiv_stackwidget import oivStackWidget

FORM_CLASS, _ = uic.loadUiType(os.path.join(
    os.path.dirname(__file__), 'oiv_tekenen_widget.ui'))

class oivTekenWidget(QDockWidget, FORM_CLASS):
    """Organize all draw features on the map"""

    configFileBouwlaag = None
    iface = None
    canvas = None
    pointTool = None
    identifier = None
    parentLayerName = None
    drawLayerType = None
    drawLayer = None
    editableLayerNames = []
    objectwidget = None
    drawTool = None
    moveTool = None
    selectTool = None
    #id van pictogram
    snapPicto = ['1', '10', '32', '47', '148', '149', '150', '151', '152',\
                 '1011', 'Algemeen', 'Voorzichtig', 'Waarschuwing', 'Gevaar']
    moveLayerNames = []
    snapLayerNames = ["BAG panden", "Bouwlagen", \
                        "Bouwkundige veiligheidsvoorzieningen", "Ruimten"]

    def __init__(self, parent=None):
        """Constructor."""
        super(oivTekenWidget, self).__init__(parent)
        self.setupUi(self)
        self.iface = iface
        self.stackwidget = oivStackWidget()
        self.configFileBouwlaag = read_config_file("/config_files/csv/config_bouwlaag.csv", None)
        self.initUI()

    def initUI(self):
        """intitiate the UI elemets on the widget"""
        set_lengte_oppervlakte_visibility(self, False, False, False, False)
        self.pand_id.setVisible(False)
        #connect buttons to the action
        self.move.clicked.connect(self.run_move_point)
        self.identify.clicked.connect(self.run_edit_tool)
        self.select.clicked.connect(self.run_select_tool)
        self.delete_f.clicked.connect(self.run_delete_tool)
        self.pan.clicked.connect(self.activatePan)
        self.terug.clicked.connect(self.close_teken_show_object)
        actionList, self.editableLayerNames, self.moveLayerNames = get_actions(self.configFileBouwlaag)
        self.initActions(actionList)

    def initActions(self, actionList):
        """connect all the buttons to the action"""
        for lyr in actionList:
            for action in lyr:
                runLayerName = action[0]
                buttonNr = action[1]
                buttonName = str(action[2].lower())
                strButton = self.findChild(QPushButton, buttonName)

                if strButton:
                    #set tooltip per buttonn
                    strButton.setToolTip(buttonName)
                    #geef met de signal ook mee welke knop er is geklikt -> nr
                    strButton.clicked.connect(lambda dummy='dummyvar', rlayer=runLayerName, who=buttonNr: self.run_tekenen(dummy, rlayer, who))

    def activatePan(self):
        """trigger pan function to loose other functions"""
        self.iface.actionPan().trigger()

    def run_edit_tool(self):
        """activate the edit feature tool"""
        try:
            self.selectTool.geomSelected.disconnect()
        except: # pylint: disable=bare-except
            pass
        self.selectTool.configFileBouwlaag = self.configFileBouwlaag
        self.canvas.setMapTool(self.selectTool)
        self.selectTool.geomSelected.connect(self.edit_attribute)

    def run_select_tool(self):
        """activate the select feature tool"""
        try:
            self.selectTool.geomSelected.disconnect()
        except: # pylint: disable=bare-except
            pass
        self.canvas.setMapTool(self.selectTool)
        self.selectTool.geomSelected.connect(self.select_feature)

    def select_feature(self, ilayer, ifeature):
        """catch emitted signal from selecttool"""
        self.iface.setActiveLayer(ilayer)
        ids = []
        ids.append(ifeature.id())
        ilayer.selectByIds(ids)
        ilayer.startEditing()
        self.selectTool.geomSelected.disconnect(self.select_feature)

    def run_delete_tool(self):
        """activate delete feature tool"""
        try:
            self.selectTool.geomSelected.disconnect()
        except: # pylint: disable=bare-except
            pass
        self.selectTool.configFileBouwlaag = self.configFileBouwlaag
        self.canvas.setMapTool(self.selectTool)
        self.selectTool.geomSelected.connect(self.delete_feature)

    def delete_feature(self, ilayer, ifeature):
        """controleer of het een feature betreft binnenn de lijst editableLayers"""
        if ilayer.name() in self.editableLayerNames:
            self.iface.setActiveLayer(ilayer)
            ids = []
            ids.append(ifeature.id())
            ilayer.selectByIds(ids)
            ilayer.startEditing()
            reply = QMessageBox.question(self.iface.mainWindow(), 'Continue?',
                                         "Weet u zeker dat u de geselecteerde feature wilt weggooien?", QMessageBox.Yes, QMessageBox.No)
            if reply == QMessageBox.No:
                #als "nee" deselecteer alle geselecteerde features
                self.selectTool.geomSelected.disconnect(self.delete_feature)
                ilayer.selectByIds([])
            elif reply == QMessageBox.Yes:
                #als "ja" -> verwijder de feature op basis van het unieke feature id
                ilayer.deleteFeature(ifeature.id())
                ilayer.commitChanges()
                self.selectTool.geomSelected.disconnect(self.delete_feature)
                self.run_delete_tool()
        #als er een feature is aangeklikt uit een andere laag, geef dan een melding
        else:
            reply = QMessageBox.information(self.iface.mainWindow(), 'Geen tekenlaag!',
                                            "U heeft geen feature op een tekenlaag aangeklikt!\n\n\
                                            Klik a.u.b. op de juiste locatie.\n\n\
                                            Weet u zeker dat u iets wilt weggooien?",\
                                            QMessageBox.Yes, QMessageBox.No)
            if reply == QMessageBox.No:
                self.selectTool.geomSelected.disconnect(self.delete_feature)
                ilayer.selectByIds([])
            else:
                self.selectTool.geomSelected.disconnect(self.delete_feature)
                self.run_delete_tool()

    def edit_attribute(self, ilayer, ifeature):
        """open het formulier van een feature in een dockwidget, zodat de attributen kunnen worden bewerkt"""
        self.iface.addDockWidget(Qt.RightDockWidgetArea, self.stackwidget)
        self.stackwidget.parentWidget = self
        self.stackwidget.open_feature_form(ilayer, ifeature)
        self.close()
        self.stackwidget.show()
        self.selectTool.geomSelected.disconnect(self.edit_attribute)
        self.run_edit_tool()

    def run_move_point(self):
        """om te verschuiven/roteren moeten de betreffende lagen op bewerken worden gezet"""
        for lyrName in self.moveLayerNames:
            moveLayer = getlayer_byname(lyrName)
            moveLayer.startEditing()
        self.moveTool.onMoved = self.stop_moveTool
        self.canvas.setMapTool(self.moveTool)

    def stop_moveTool(self):
        """na de actie verschuiven/bewerken moeten de betreffende lagen opgeslagen worden en bewerken moet worden uitgezet"""
        for lyrName in self.moveLayerNames:
            moveLayer = getlayer_byname(lyrName)
            moveLayer.commitChanges()        
        self.activatePan()

    def run_tekenen(self, dummy, run_layer, feature_id):
        """activate the right draw action"""
        #welke pictogram is aangeklikt en wat is de bijbehorende tekenlaag
        self.identifier = feature_id
        self.drawLayer = getlayer_byname(run_layer)
        self.drawLayerType = check_layer_type(self.drawLayer)
        attrs = {"parent_layer" : ''}
        attrs = get_draw_layer_attr(attrs, run_layer, self.configFileBouwlaag)
        self.parentLayerName = attrs["parent_layer"]
        objectId = self.pand_id.text()
        #aan welke lagen kan worden gesnapt?
        possibleSnapFeatures = get_possible_snapFeatures_bouwlaag(self.snapLayerNames, objectId)

        if self.drawLayerType == "Point":
            self.pointTool.snapPt = None
            self.pointTool.snapping = False
            self.pointTool.startRotate = False
            self.pointTool.possibleSnapFeatures = possibleSnapFeatures
            if self.identifier in self.snapPicto:
                self.pointTool.snapping = True
            self.pointTool.layer = self.drawLayer
            self.canvas.setMapTool(self.pointTool)
            set_lengte_oppervlakte_visibility(self, False, False, False, False)
            self.pointTool.onGeometryAdded = self.place_feature
        else:
            if self.drawLayerType == "Line":
                self.drawTool.captureMode = 1
                set_lengte_oppervlakte_visibility(self, True, True, False, True)
            else:
                self.drawTool.captureMode = 2
                set_lengte_oppervlakte_visibility(self, True, True, True, True)
            self.drawTool.layer = self.drawLayer
            self.drawTool.possibleSnapFeatures = possibleSnapFeatures
            self.drawTool.canvas = self.canvas
            self.drawTool.onGeometryAdded = self.place_feature
            self.canvas.setMapTool(self.drawTool)
            self.drawTool.parent = self

    def place_feature(self, points, snapAngle):
        """Save and place feature on the canvas"""
        parentId = None
        self.iface.setActiveLayer(self.drawLayer)
        if points:
            parentId, childFeature = construct_feature(self.drawLayerType, self.parentLayerName, points, None, self.iface)

        if parentId is not None:
            buttonCheck = get_attributes(parentId, childFeature, snapAngle, self.identifier, self.drawLayer, self.configFileBouwlaag)
            if buttonCheck != 'Cancel':
                write_layer(self.drawLayer, childFeature)

        self.run_tekenen('dummy', self.drawLayer.name(), self.identifier)

    def close_teken_show_object(self):
        """destroy and close self"""
        try:
            self.move.clicked.disconnect()
            self.identify.clicked.disconnect()
            self.select.clicked.disconnect()
            self.delete_f.clicked.disconnect()
            self.pan.clicked.disconnect()
            self.terug.clicked.disconnect()
        except: # pylint: disable=bare-except
            pass
        try:
            del self.stackwidget
        except: # pylint: disable=bare-except
            pass
        for widget in self.children():
            if isinstance(widget, QPushButton):
                try:
                    widget.clicked.disconnect()
                except: # pylint: disable=bare-except
                    pass
        self.close()
        self.objectwidget.show()
        del self
