"""init the oiv base widget"""
import os
import qgis.PyQt as PQt #pylint: disable=import-error
import qgis.PyQt.QtWidgets as PQtW #pylint: disable=import-error
import qgis.core as QC #pylint: disable=import-error

import oiv.tools.filter_object as FO
import oiv.plugin_helpers.qt_helper as QT
import oiv.plugin_helpers.messages as MSG
import oiv.tools.utils_core as UC
import oiv.bag_pand.oiv_pandgegevens as OPG
import oiv.repressief_object.oiv_repressief_object as ORO
import oiv.repressief_object.oiv_objectnieuw as OON

FORM_CLASS, _ = PQt.uic.loadUiType(os.path.join(
    os.path.dirname(__file__), 'oiv_base_widget.ui'))

class oivBaseWidget(PQtW.QDockWidget, FORM_CLASS):
    """create dockwidget as base of the oiv plugin"""

    oiv = None
    iface = None
    canvas = None
    drawLayer = None
    pinTool = None
    pointTool = None
    selectTool = None
    drawTool = None
    moveTool = None
    objectwidget = None
    repressiefobjectwidget = None
    objectnieuwwidget = None

    def __init__(self, parent=None):
        """Constructor."""
        super(oivBaseWidget, self).__init__(parent)
        self.setupUi(self)
        self.identify_pand.clicked.connect(self.run_identify_pand)
        self.identify_gebouw.clicked.connect(self.run_identify_terrein)
        self.filter_objecten.clicked.connect(lambda: FO.init_filter_section(self))
        self.filterBtn.clicked.connect(lambda: FO.set_object_filter(self))
        self.closewidget.clicked.connect(self.close_basewidget)
        self.filterframe.setVisible(False)

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
        if isinstance(ilayer, QC.QgsVectorLayer):
            if ilayer.name() == "Bouwlagen":
                objectId = str(ifeature["pand_id"])
                self.run_bouwlagen(objectId)
            elif ilayer.name() == "BAG panden":
                objectId = str(ifeature["identificatie"])
                self.run_bouwlagen(objectId)
        #if another layer is identified there is no object that can be determined, so a message is send to the user
        else:
            MSG.showMsgBox('noidentifiedobject')
        self.identifyTool.geomIdentified.disconnect()

    def get_identified_terrein(self, ilayer, ifeature):
        """Return of identified layer and feature and get related object"""
        #the identified layer must be "Object" or "Object terrein"
        self.drawLayer = UC.getlayer_byname("Objecten")
        if ilayer is None:
            self.run_new_object('wordt gekoppeld in de database', 'BGT', 'wordt gekoppeld in de database')
        elif ilayer.name() == "BAG panden":
            objectId = str(ifeature["identificatie"])
            bron = ifeature["bron"]
            bron_tabel = ifeature["bron_tbl"]
            self.run_new_object(objectId, bron, bron_tabel)
        elif ilayer.name() == "Objecten":
            objectId = ifeature["id"]
            self.run_object(ifeature, objectId)
        elif ilayer.name() == "Object terrein":
            objectId = ifeature["object_id"]
            request = QC.QgsFeatureRequest().setFilterExpression('"id" = ' + str(objectId))
            ifeature = next(self.drawLayer.getFeatures(request))
            self.run_object(ifeature, objectId)
        #if another layer is identified there is no object that can be determined, so a message is send to the user
        else:
            MSG.showMsgBox('noidentifiedobject')
        self.identifyTool.geomIdentified.disconnect()

    def run_bouwlagen(self, objectId):
        """start objectgegevens widget"""
        self.init_object_widget(objectId)
        self.iface.addDockWidget(QT.getWidgetType(), self.objectwidget)
        self.iface.actionPan().trigger()
        self.objectwidget.show()
        self.close()
        self.objectwidget.initUI()
        self.objectwidget.initActions()

    def run_object(self, ifeature, objectId):
        """start repressief object widget"""
        self.init_repressief_object_widget(ifeature, objectId)
        self.iface.addDockWidget(QT.getWidgetType(), self.repressiefobjectwidget)
        self.iface.actionPan().trigger()
        self.repressiefobjectwidget.show()
        self.close()
        self.repressiefobjectwidget.initActions()

    def init_object_widget(self, objectId):
        """pass on the tools to objectgegevens widget, intitializing the tools in the sub widget, draws an error"""
        #Load configuration file
        self.objectwidget = OPG.oivPandWidget(self)
        self.objectwidget.pand_id.setText(str(objectId))
        self.objectwidget.iface = self.iface
        self.objectwidget.canvas = self.canvas
        self.objectwidget.selectTool = self.selectTool
        self.objectwidget.basewidget = self
        self.objectwidget.pointTool = self.pointTool
        self.objectwidget.drawTool = self.drawTool
        self.objectwidget.moveTool = self.moveTool
        self.objectwidget.identifyTool = self.identifyTool

    def init_repressief_object_widget(self, ifeature, objectId):
        """pass on the tools to objectgegevens widget, intitializing the tools in the sub widget, draws an error"""
        self.repressiefobjectwidget = ORO.oivRepressiefObjectWidget()
        if ifeature:
            self.repressiefobjectwidget.object_id.setText(str(objectId))
            self.repressiefobjectwidget.formelenaam.setText(ifeature["formelenaam"])
        self.repressiefobjectwidget.canvas = self.canvas
        self.repressiefobjectwidget.drawLayer = self.drawLayer
        self.repressiefobjectwidget.selectTool = self.selectTool
        self.repressiefobjectwidget.basewidget = self
        self.repressiefobjectwidget.pointTool = self.pointTool
        self.repressiefobjectwidget.drawTool = self.drawTool
        self.repressiefobjectwidget.moveTool = self.moveTool
        self.repressiefobjectwidget.identifyTool = self.identifyTool

    def run_new_object(self, objectId, bron, bron_tbl):
        """tart new object widget, eventhough passing trough the tools to objectgegevens widget"""
        self.objectnieuwwidget = OON.oivObjectNieuwWidget()
        self.init_repressief_object_widget(None, None)
        self.objectnieuwwidget.basewidget = self
        self.objectnieuwwidget.objectwidget = self.repressiefobjectwidget
        self.iface.addDockWidget(QT.getWidgetType(), self.objectnieuwwidget)
        self.objectnieuwwidget.canvas = self.canvas
        self.objectnieuwwidget.mapTool = self.pinTool
        self.objectnieuwwidget.identificatienummer.setText(str(objectId))
        self.objectnieuwwidget.bron.setText(str(bron))
        self.objectnieuwwidget.bron_table.setText(str(bron_tbl))
        self.iface.actionPan().trigger()
        self.objectnieuwwidget.show()
        self.close()

    def close_basewidget(self):
        """close plugin and re-activate toolbar combobox"""
        try:
            del self.objectwidget
        except: # pylint: disable=bare-except
            pass
        try:
            del self.objectnieuwwidget
        except: # pylint: disable=bare-except
            pass
        self.close()
        self.oiv.toolbar.setEnabled(True)
        self.oiv.projCombo.setEnabled(True)
        self.oiv.checkVisibility = False
