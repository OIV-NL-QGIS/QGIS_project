"""main file that's get evrything moving"""
import os

import qgis.PyQt.QtCore as PQtC
import qgis.PyQt.QtGui as PQtG
import qgis.PyQt.QtWidgets as PQtW
import qgis.core as QC
import qgis.gui as QG
import oiv.helpers.qt_helper as QT
import oiv.helpers.messages as MSG
import oiv.helpers.configdb_helper as CH
from .helpers.constants import PLUGIN, PAND
import oiv.helpers.utils_gui as UG
import oiv.helpers.utils_core as UC
import oiv.oiv_base_widget as OB
import oiv.oiv_config as OC
import oiv.tools.identifyTool as IT
import oiv.tools.snappointTool as ST
import oiv.tools.movepointTool as MT
import oiv.tools.selectTool as PS
import oiv.tools.mapTool as CT

# initialize Qt resources from file resources.py
from .resources import qInitResources


class oiv(PQtW.QWidget):
    """initialize class attributes"""

    action = None
    toolbar = None
    projCombo = None
    basewidget = None
    drawLayer = None
    bagNode = None
    projComboAction = None
    checkVisibility = False

    def __init__(self, iface):
        super(oiv, self).__init__()
        self.iface = iface
        self.canvas = self.iface.mapCanvas()
        self.identifyTool = IT.IdentifyGeometryTool(self.canvas)
        self.pinTool = QG.QgsMapToolEmitPoint(self.canvas)
        self.pointTool = ST.SnapPointTool(self.canvas)
        self.selectTool = IT.SelectTool(self.canvas)
        self.polygonSelectTool = PS.PolygonSelectTool(self.canvas)
        self.drawTool = CT.CaptureTool(self.canvas)
        self.moveTool = MT.MovePointTool(self.canvas, self.drawLayer)

    def initGui(self):
        """init actions plugin"""
        self.toolbar = self.iface.addToolBar(PLUGIN["name"])
        self.action = PQtW.QAction(PQtG.QIcon(PLUGIN["icon"]), PLUGIN["name"], self.iface.mainWindow())
        self.action.triggered.connect(self.run)
        self.toolbar.addAction(self.action)
        self.iface.addPluginToMenu(PLUGIN["menulocation"], self.action)
        self.configAction = PQtW.QAction(PQtG.QIcon(PLUGIN["settingsicon"]), PLUGIN["settingsname"], self.iface.mainWindow())
        self.configAction.triggered.connect(self.run_config)
        self.iface.addPluginToMenu(PLUGIN["menusettingslocation"], self.configAction)
        # add label to toolbar
        label = PQtW.QLabel()
        self.toolbar.addWidget(label)
        label.setText(PLUGIN["toolbartext"])
        # init dropdown to switch floors
        self.projCombo = PQtW.QComboBox(self.iface.mainWindow())
        bouwlagen = PAND["bouwlagen"]
        minBouwlaag = bouwlagen["min"]
        maxBouwlaag = bouwlagen["max"]
        for i in range(maxBouwlaag - minBouwlaag + 1):
            if maxBouwlaag - i != 0:
                if maxBouwlaag - i == 1:
                    init_index = i
                self.projCombo.addItem(str(maxBouwlaag - i))
        self.projComboAction = self.toolbar.addWidget(self.projCombo)
        self.projCombo.setFixedWidth(100)
        self.projCombo.setMaxVisibleItems(30)
        # set intial index to floor 1
        self.projCombo.setCurrentIndex(init_index)
        # connect to set layer subset if the index is changed
        self.projCombo.currentIndexChanged.connect(self.set_layer_subset_toolbar)
        # init projectVariable to communicate from plugin to qgis
        QC.QgsExpressionContextUtils.setProjectVariable(QC.QgsProject.instance(), 'actieve_bouwlaag', 1)

    def unload(self):
        """remove the plugin menu item and remove the widgets"""
        try:
            del self.basewidget
        except:  # pylint: disable=bare-except
            pass
        self.iface.removePluginMenu(PLUGIN["menulocation"], self.action)
        self.iface.removePluginMenu(PLUGIN["menusettingslocation"], self.configAction)
        self.projCombo.currentIndexChanged.disconnect()
        self.action.triggered.disconnect()
        self.configAction.triggered.disconnect()
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
        try:
            layer = UC.getlayer_byname('applicatie')
            request = QC.QgsFeatureRequest().setFilterExpression('"id" = 1')
            ifeature = UC.featureRequest(layer, request)
            dbVersion = ifeature["db_versie"]
        except:
            dbVersion = 0
        if 'Objecten' not in projectTest:
            self.toolbar.setEnabled(False)
            self.action.setEnabled(False)
        elif PLUGIN["compatibleDbVersion"]["max"] < dbVersion < PLUGIN["compatibleDbVersion"]["min"]:
            MSG.showMsgBox('invaliddatabaseversion')
            self.toolbar.setEnabled(False)
            self.action.setEnabled(False)
        else:
            # always start from floor 1
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
