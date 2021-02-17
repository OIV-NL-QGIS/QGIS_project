"""main file that's get evrything moving"""
import os #pylint: disable=unused-import

import qgis.PyQt.QtCore as PQtC #pylint: disable=import-error
import qgis.PyQt.QtGui as PQtG #pylint: disable=import-error
import qgis.PyQt.QtWidgets as PQtW #pylint: disable=import-error
import qgis.core as QC #pylint: disable=import-error
import qgis.gui as QG #pylint: disable=import-error

import oiv.plugin_helpers.qt_helper as QT
import oiv.plugin_helpers.messages as MSG
import oiv.plugin_helpers.configdb_helper as CH
import oiv.plugin_helpers.plugin_constants as PC
import oiv.tools.utils_gui as UG
import oiv.oiv_base_widget as OB
import oiv.oiv_config as OC
import oiv.tools.identifyTool as IT
import oiv.tools.snappointTool as ST
import oiv.tools.movepointTool as MT
import oiv.tools.mapTool as CT

#initialize Qt resources from file resources.py
from .resources import qInitResources #pylint: disable=unused-import

class oiv(PQtW.QWidget):
    """initialize class attributes"""

    action = None
    toolbar = None
    projCombo = None
    basewidget = None
    drawLayer = None
    projComboAction = None
    checkVisibility = False

    # Save reference to the QGIS interface
    def __init__(self, iface):
        super(oiv, self).__init__()
        self.iface = iface
        self.canvas = self.iface.mapCanvas()
        self.identifyTool = IT.IdentifyGeometryTool(self.canvas)
        self.pinTool = QG.QgsMapToolEmitPoint(self.canvas)
        self.pointTool = ST.SnapPointTool(self.canvas)
        self.selectTool = IT.SelectTool(self.canvas)
        self.drawTool = CT.CaptureTool(self.canvas)
        self.moveTool = MT.MovePointTool(self.canvas, self.drawLayer)

    def initGui(self):
        """init actions plugin"""
        self.toolbar = self.iface.addToolBar(PC.PLUGIN["name"])
        self.action = PQtW.QAction(PQtG.QIcon(PC.PLUGIN["icon"]), PC.PLUGIN["name"], self.iface.mainWindow())
        self.action.triggered.connect(self.run)
        self.toolbar.addAction(self.action)
        self.iface.addPluginToMenu(PC.PLUGIN["menulocation"], self.action)
        self.settings = PQtW.QAction(PQtG.QIcon(PC.PLUGIN["settingsicon"]), PC.PLUGIN["settingsname"], self.iface.mainWindow())
        self.settings.triggered.connect(self.run_config)
        self.iface.addPluginToMenu(PC.PLUGIN["menusettingslocation"], self.settings)
        #add label to toolbar
        label = PQtW.QLabel()
        self.toolbar.addWidget(label)
        label.setText(PC.PLUGIN["toolbartext"])
        #init dropdown to switch floors
        self.projCombo = PQtW.QComboBox(self.iface.mainWindow())
        minBouwlaag = PC.PAND["minbouwlaag"]
        maxBouwlaag = PC.PAND["maxbouwlaag"]
        for i in range(maxBouwlaag - minBouwlaag + 1):
            if maxBouwlaag - i != 0:
                if maxBouwlaag - i == 1:
                    init_index = i
                self.projCombo.addItem(str(maxBouwlaag - i))
        self.projComboAction = self.toolbar.addWidget(self.projCombo)
        self.projCombo.setFixedWidth(100)
        self.projCombo.setMaxVisibleItems(30)
        #set intial index to floor 1
        self.projCombo.setCurrentIndex(init_index)
        #connect to set layer subset if the index is changed
        self.projCombo.currentIndexChanged.connect(self.set_layer_subset_toolbar)
        #init projectVariable to communicate from plugin to original drawing possibilities
        QC.QgsExpressionContextUtils.setProjectVariable(QC.QgsProject.instance(), 'actieve_bouwlaag', 1)

    def unload(self):
        """remove the plugin menu item and remove the widgets"""
        try:
            del self.basewidget
        except: # pylint: disable=bare-except
            pass
        self.iface.removePluginMenu(PC.PLUGIN["menulocation"], self.action)
        self.iface.removePluginMenu(PC.PLUGIN["menusettingslocation"], self.settings)
        self.projCombo.currentIndexChanged.disconnect()
        self.action.triggered.disconnect()
        self.settings.triggered.disconnect()
        del self.toolbar
        self.checkVisibility = None
        self.iface.removeToolBarIcon(self.action)

    def set_layer_subset_toolbar(self):
        """laag filter aanpassen naar de geselecteerd bouwlaag"""
        subString = "bouwlaag = " + str(self.projCombo.currentText())
        UG.set_layer_substring(subString)
        project = QC.QgsProject.instance()
        QC.QgsExpressionContextUtils.setProjectVariable(project, 'actieve_bouwlaag', int(self.projCombo.currentText()))

    def run_config(self):
        configWidget = OC.oivConfigWidget(self)
        self.iface.addDockWidget(QT.getWidgetType(), configWidget)
        configWidget.show()

    def run(self):
        """run the plugin, if project is not OIV object, deactivate plugin when clicked on icon"""
        project = QC.QgsProject.instance()
        projectTest = str(QC.QgsExpressionContextUtils.projectScope(project).variable('project_title'))
        dbVersion = CH.get_app_version()
        if 'Objecten' not in projectTest:
            self.toolbar.setEnabled(False)
            self.action.setEnabled(False)
        elif PC.PLUGIN["compatibleDbVersion"][1] > dbVersion < PC.PLUGIN["compatibleDbVersion"][0]:
            MSG.showMsgBox('invaliddatabaseversion')
            self.toolbar.setEnabled(False)
            self.action.setEnabled(False)
        else:
            #always start from floor 1
            self.basewidget = OB.oivBaseWidget(self)
            subString = "bouwlaag = 1"
            UG.set_layer_substring(subString)
            index = self.projCombo.findText('1', PQtC.Qt.MatchFixedString)
            if index >= 0:
                self.projCombo.setCurrentIndex(index)
            self.iface.addDockWidget(QT.getWidgetType(), self.basewidget)
            self.basewidget.show()
            self.toolbar.setEnabled(False)
            self.projCombo.setEnabled(False)
            self.checkVisibility = True
