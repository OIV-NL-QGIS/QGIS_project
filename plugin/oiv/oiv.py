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
#compile resources: pyrcc4 -o C:\Users\oiv\.qgis2\python\plugins\oiv_imroi\resources.py C:\Users\oiv\.qgis2\python\plugins\oiv_imroi\resources.qrc
#pyrcc4 -o C:\Users\joost\.qgis2\python\plugins\oiv_imroi_v2\resources.py C:\Users\joost\.qgis2\python\plugins\oiv_imroi_v2\resources.qrc

#Import the PyQt and QGIS libraries
import os

from qgis.PyQt.QtCore import Qt
from qgis.PyQt.QtGui import QIcon
from qgis.PyQt.QtWidgets import QAction, QLabel, QComboBox, QMessageBox
from qgis.core import QgsProject, QgsExpressionContextUtils, QgsFeatureRequest
from qgis.gui import QgsMapToolEmitPoint

#initialize Qt resources from file resources.py
from .resources import *

#import plugin widget and tools
from .tools.identifyTool import IdentifyGeometryTool, SelectTool
from .tools.utils_core import getlayer_byname
from .tools.utils_gui import read_settings, set_layer_substring
from .tools.mapTool import CaptureTool
from .tools.movepointTool import MovePointTool
from .tools.snappointTool import SnapPointTool
from .tools.update_dimension_tables import run_update_dimension_tables
from .tools.filter_object import init_filter_section, set_object_filter
from .oiv_base_widget import oivBaseWidget
from .bag_pand.oiv_pandgegevens import oivPandWidget
from .repressief_object.oiv_repressief_object import oivRepressiefObjectWidget
from .repressief_object.oiv_objectnieuw import oivObjectNieuwWidget

class oiv:
    """initialize class attributes"""

    compatibleVersion = [315, 319]
    pluginVersion = '3.1.9'
    minBouwlaag = -10
    maxBouwlaag = 30
    checkVisibility = False
    drawLayer = None

    # Save reference to the QGIS interface
    def __init__(self, iface):
        self.iface = iface
        self.canvas = self.iface.mapCanvas()
        self.identifyTool = IdentifyGeometryTool(self.canvas)
        self.pinTool = QgsMapToolEmitPoint(self.canvas)
        self.pointTool = SnapPointTool(self.canvas)
        self.selectTool = SelectTool(self.canvas)
        self.basewidget = oivBaseWidget()
        self.drawTool = CaptureTool(self.canvas)
        self.moveTool = MovePointTool(self.canvas, self.drawLayer)

    def initGui(self):
        """init actions plugin"""
        self.toolbar = self.iface.addToolBar("OIV Objecten")
        self.action = QAction(QIcon(":/plugins/oiv/config_files/png/oiv_plugin.png"), "OIV Objecten", self.iface.mainWindow())
        self.action.triggered.connect(self.run)
        self.toolbar.addAction(self.action)
        self.iface.addPluginToMenu('&OIV Objecten', self.action)
        #add label to toolbar
        self.label = QLabel(self.iface.mainWindow())
        self.labelAction = self.toolbar.addWidget(self.label)
        self.label.setText("OIV " + self.pluginVersion + " | Actieve bouwlaag: ")
        #init dropdown to switch floors
        self.projCombo = QComboBox(self.iface.mainWindow())
        for i in range(self.maxBouwlaag - self.minBouwlaag + 1):
            if self.maxBouwlaag - i != 0:
                if self.maxBouwlaag - i == 1:
                    init_index = i
                self.projCombo.addItem(str(self.maxBouwlaag - i))
        self.projComboAction = self.toolbar.addWidget(self.projCombo)
        self.projCombo.setFixedWidth(100)
        self.projCombo.setMaxVisibleItems(30)
        #set intial index to floor 1
        self.projCombo.setCurrentIndex(init_index)
        #connect to set layer subset if the index is changed
        self.projCombo.currentIndexChanged.connect(self.set_layer_subset_toolbar)
        #init projectVariable to communicate from plugin to original drawing possibilities
        QgsExpressionContextUtils.setProjectVariable(QgsProject.instance(), 'actieve_bouwlaag', 1)
        self.action2 = QAction(QIcon(":/plugins/oiv/config_files/png/oiv_update.png"), "Update dimension tables", self.iface.mainWindow())
        self.action2.triggered.connect(self.update_dimension_tables_project)
        self.iface.addPluginToMenu('&OIV Objecten', self.action2)
        self.action2.setEnabled(False)
        self.update_dimension_tables()

    def close_basewidget(self):
        """close plugin and re-activate toolbar combobox"""
        self.basewidget.close()
        self.toolbar.setEnabled(True)
        self.projCombo.setEnabled(True)
        self.action2.setEnabled(False)
        self.checkVisibility = False

    def unload(self):
        """remove the plugin menu item and remove the widgets"""
        try:
            del self.basewidget
        except: # pylint: disable=bare-except
            pass
        try:
            del self.objectwidget
        except: # pylint: disable=bare-except
            pass
        try:
            del self.objectnieuwwidget
        except: # pylint: disable=bare-except
            pass
        self.iface.removePluginMenu("&OIV Objecten", self.action)
        self.iface.removePluginMenu("&OIV Objecten", self.action2)
        self.projCombo.currentIndexChanged.disconnect()
        self.action.triggered.disconnect()
        self.action2.triggered.disconnect()
        del self.toolbar
        self.checkVisibility = None
        self.iface.removeToolBarIcon(self.action)

    def update_dimension_tables(self):
        run_update_dimension_tables('..\\config_files\\geoserver.conf', '..\\config_files\\dimension_tables.db', False)

    def update_dimension_tables_project(self):
        project = QgsProject.instance()
        projectConn = str(QgsExpressionContextUtils.projectScope(project).variable('connection'))
        if projectConn == 'WFS':
            projPath = QgsProject.instance().readPath("./")
            dbPath = projPath + '/db/dimension_tables.db'
            run_update_dimension_tables('..\\config_files\\geoserver.conf', dbPath, True)

    def run_identify_pand(self):
        """get the identification of a building from the user"""
        self.canvas.setMapTool(self.identifyTool)
        try:
            self.identifyTool.geomIdentified.disconnect()
        except: # pylint: disable=bare-except
            pass
        self.identifyTool.geomIdentified.connect(self.get_identified_pand)

    def run_identify_terrein(self):
        """get the identification of a building from the user"""
        self.canvas.setMapTool(self.identifyTool)
        try:
            self.identifyTool.geomIdentified.disconnect()
        except: # pylint: disable=bare-except
            pass
        self.identifyTool.geomIdentified.connect(self.get_identified_terrein)

    def get_identified_pand(self, ilayer, ifeature):
        """Return of identified layer and feature and get related object"""
        #the identified layer must be "Bouwlagen" or "BAG panden"
        if ilayer.name() == "Bouwlagen":
            objectId = str(ifeature["pand_id"])
            self.run_bouwlagen(objectId)
        elif ilayer.name() == "BAG panden":
            objectId = str(ifeature["identificatie"])
            self.run_bouwlagen(objectId)
        #if another layer is identified there is no object that can be determined, so a message is send to the user
        else:
            QMessageBox.information(None, "Oeps:", "Geen pand gevonden! Klik boven op een pand.")
        self.identifyTool.geomIdentified.disconnect()

    def get_identified_terrein(self, ilayer, ifeature):
        """Return of identified layer and feature and get related object"""
        #the identified layer must be "Object" or "Object terrein"
        self.drawLayer = getlayer_byname("Objecten")
        if ilayer is None:
            self.run_new_object('wordt gekoppeld in de database', 'BGT', 'wordt gekoppeld in de database')
        elif ilayer.name() == "BAG panden":
            objectId   = str(ifeature["identificatie"])
            bron       = ifeature["bron"]
            bron_tabel = ifeature["bron_tbl"]
            self.run_new_object(objectId, bron, bron_tabel) 
        elif ilayer.name() == "Objecten":
            objectId = ifeature["id"]
            self.run_object(ifeature, objectId)
        elif ilayer.name() == "Object terrein":
            objectId = ifeature["object_id"]
            request = QgsFeatureRequest().setFilterExpression('"id" = ' + str(objectId))
            ifeature = next(self.drawLayer.getFeatures(request))
            self.run_object(ifeature, objectId)
        #if another layer is identified there is no object that can be determined, so a message is send to the user
        else:
            QMessageBox.information(None, "Oeps:", "Geen repressief object gevonden!\
                Heeft u op een terrein of een object geklikt?\
                Selecteer opnieuw.")
        self.identifyTool.geomIdentified.disconnect()

    def set_layer_subset_toolbar(self):
        """laag filter aanpassen naar de geselecteerd bouwlaag"""
        QgsExpressionContextUtils.setProjectVariable(QgsProject.instance(), 'actieve_bouwlaag', int(self.projCombo.currentText()))
        subString = "bouwlaag = " + str(self.projCombo.currentText())
        set_layer_substring(subString)

    def init_object_widget(self, objectId):
        """pass on the tools to objectgegevens widget, intitializing the tools in the sub widget, draws an error"""
        #Load configuration file
        self.objectwidget = oivPandWidget()
        self.objectwidget.pand_id.setText(str(objectId))
        self.objectwidget.canvas = self.canvas
        self.objectwidget.selectTool = self.selectTool
        self.objectwidget.basewidget = self.basewidget
        self.objectwidget.pointTool = self.pointTool
        self.objectwidget.drawTool = self.drawTool
        self.objectwidget.moveTool = self.moveTool
        self.objectwidget.identifyTool = self.identifyTool

    def init_repressief_object_widget(self, ifeature, objectId):
        """pass on the tools to objectgegevens widget, intitializing the tools in the sub widget, draws an error"""
        self.repressiefobjectwidget = oivRepressiefObjectWidget()
        if ifeature:
            self.repressiefobjectwidget.object_id.setText(str(objectId))
            self.repressiefobjectwidget.formelenaam.setText(ifeature["formelenaam"])
        self.repressiefobjectwidget.canvas = self.canvas
        self.repressiefobjectwidget.drawLayer = self.drawLayer
        self.repressiefobjectwidget.selectTool = self.selectTool
        self.repressiefobjectwidget.basewidget = self.basewidget
        self.repressiefobjectwidget.pointTool = self.pointTool
        self.repressiefobjectwidget.drawTool = self.drawTool
        self.repressiefobjectwidget.moveTool = self.moveTool
        self.repressiefobjectwidget.identifyTool = self.identifyTool

    def run_bouwlagen(self, objectId):
        """start objectgegevens widget"""
        self.init_object_widget(objectId)
        self.iface.addDockWidget(Qt.RightDockWidgetArea, self.objectwidget)
        self.iface.actionPan().trigger()
        self.objectwidget.show()
        self.basewidget.close()
        self.objectwidget.initUI()
        self.objectwidget.initActions()

    def run_object(self, ifeature, objectId):
        """start repressief object widget"""
        self.init_repressief_object_widget(ifeature, objectId)
        self.iface.addDockWidget(Qt.RightDockWidgetArea, self.repressiefobjectwidget)
        self.iface.actionPan().trigger()
        self.repressiefobjectwidget.show()
        self.basewidget.close()
        self.repressiefobjectwidget.initActions()

    def run_new_object(self, objectId, bron, bron_tbl):
        """tart new object widget, eventhough passing trough the tools to objectgegevens widget"""
        self.objectnieuwwidget = oivObjectNieuwWidget()
        self.init_repressief_object_widget(None, None)
        self.objectnieuwwidget.basewidget = self.basewidget
        self.objectnieuwwidget.objectwidget = self.repressiefobjectwidget
        self.iface.addDockWidget(Qt.RightDockWidgetArea, self.objectnieuwwidget)
        self.objectnieuwwidget.canvas = self.canvas
        self.objectnieuwwidget.mapTool = self.pinTool
        self.objectnieuwwidget.identificatienummer.setText(str(objectId))
        self.objectnieuwwidget.bron.setText(str(bron))
        self.objectnieuwwidget.bron_table.setText(str(bron_tbl))
        self.iface.actionPan().trigger()
        self.objectnieuwwidget.show()
        self.basewidget.close()

    def run(self):
        """run the plugin, if project is not OIV object, deactivate plugin when clicked on icon"""
        project = QgsProject.instance()
        projectTest = str(QgsExpressionContextUtils.projectScope(project).variable('project_title'))
        dbVersion = read_settings("SELECT db_versie FROM applicatie;", False)[0]
        if 'Objecten' not in projectTest:
            self.toolbar.setEnabled(False)
            self.action.setEnabled(False)
            self.action2.setEnabled(False)
        elif dbVersion < self.compatibleVersion[0] or dbVersion > self.compatibleVersion[1]:
            QMessageBox.critical(None, "Database versie klopt niet",
                                 "De plugin of het project komt niet overeen met database versie!\
                                 Vraag aan uw regionaal beheerder om een database update!\
                                 Excuses voor het ongemak.")
            self.toolbar.setEnabled(False)
            self.action.setEnabled(False)
            self.action2.setEnabled(False)
        else:
            #always start from floor 1
            subString = "bouwlaag = 1"
            set_layer_substring(subString)
            self.basewidget.filterframe.setVisible(False)
            index = self.projCombo.findText('1', Qt.MatchFixedString)
            if index >= 0:
                self.projCombo.setCurrentIndex(index)
            self.iface.addDockWidget(Qt.RightDockWidgetArea, self.basewidget)
            self.basewidget.identify_pand.clicked.connect(self.run_identify_pand)
            self.basewidget.identify_gebouw.clicked.connect(self.run_identify_terrein)
            self.basewidget.filter_objecten.clicked.connect(lambda: init_filter_section(self.basewidget))
            self.basewidget.filterBtn.clicked.connect(lambda: set_object_filter(self.basewidget))
            self.basewidget.closewidget.clicked.connect(self.close_basewidget)
            self.action2.setEnabled(True)
            self.basewidget.show()
            self.toolbar.setEnabled(False)
            self.projCombo.setEnabled(False)
            self.checkVisibility = True
