"""init the oiv base widget"""
import os
import qgis.PyQt as PQt #pylint: disable=import-error
import qgis.PyQt.QtWidgets as PQtW #pylint: disable=import-error
import qgis.core as QC #pylint: disable=import-error

import oiv.tools.filter_object as FO
import oiv.plugin_helpers.qt_helper as QT
import oiv.plugin_helpers.messages as MSG
import oiv.plugin_helpers.plugin_constants as PC
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
    pinTool = None
    pointTool = None
    selectTool = None
    drawTool = None
    moveTool = None

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
            if ilayer.name() == PC.PAND["bouwlaaglayername"]:
                objectId = str(ifeature["pand_id"])
                self.run_bouwlagen(objectId)
            elif ilayer.name() == PC.PAND["bagpandlayername"]:
                objectId = str(ifeature["identificatie"])
                self.run_bouwlagen(objectId)
        #if another layer is identified there is no object that can be determined, so a message is send to the user
        else:
            MSG.showMsgBox('noidentifiedobject')
        self.identifyTool.geomIdentified.disconnect()

    def get_identified_terrein(self, ilayer, ifeature):
        """Return of identified layer and feature and get related object"""
        #the identified layer must be "Object" or "Object terrein"
        drawLayer = UC.getlayer_byname("Objecten")
        if ilayer is None:
            self.run_new_object('wordt gekoppeld in de database', 'BGT', 'wordt gekoppeld in de database')
        elif ilayer.name() == PC.PAND["bagpandlayername"]:
            objectId = str(ifeature["identificatie"])
            bron = ifeature["bron"]
            bron_tabel = ifeature["bron_tbl"]
            self.run_new_object(objectId, bron, bron_tabel)
        elif ilayer.name() == PC.OBJECT["objectlayername"]:
            objectId = ifeature["id"]
            formeleNaam = ifeature["formelenaam"]
            self.run_object(formeleNaam, objectId)
        elif ilayer.name() == PC.OBJECT["terreinlayername"]:
            objectId = ifeature["object_id"]
            request = QC.QgsFeatureRequest().setFilterExpression('"id" = ' + str(objectId))
            ifeature = next(drawLayer.getFeatures(request))
            formeleNaam = ifeature["formelenaam"]
            self.run_object(formeleNaam, objectId)
        #if another layer is identified there is no object that can be determined, so a message is send to the user
        else:
            MSG.showMsgBox('noidentifiedobject')
        self.identifyTool.geomIdentified.disconnect()

    def run_bouwlagen(self, objectId):
        """start objectgegevens widget"""
        pandwidget = OPG.oivPandWidget(self, objectId)
        self.iface.addDockWidget(QT.getWidgetType(), pandwidget)
        self.iface.actionPan().trigger()
        pandwidget.show()
        self.close()

    def run_object(self, formeleNaam, objectId):
        """start repressief object widget"""
        repressiefObjectWidget = ORO.oivRepressiefObjectWidget(self, objectId, formeleNaam)
        self.iface.addDockWidget(QT.getWidgetType(), repressiefObjectWidget)
        self.iface.actionPan().trigger()
        repressiefObjectWidget.show()
        self.close()

    def run_new_object(self, objectId, bron, bron_tbl):
        """start new object widget, eventhough passing trough the tools to objectgegevens widget"""
        objectNieuwWidget = OON.oivObjectNieuwWidget(self, objectId, bron, bron_tbl)
        self.iface.addDockWidget(QT.getWidgetType(), objectNieuwWidget)
        self.iface.actionPan().trigger()
        self.objectNieuwWidget.show()
        self.close()

    def close_basewidget(self):
        """close plugin and re-activate toolbar combobox"""
        self.close()
        self.oiv.toolbar.setEnabled(True)
        self.oiv.projCombo.setEnabled(True)
        self.oiv.checkVisibility = False
