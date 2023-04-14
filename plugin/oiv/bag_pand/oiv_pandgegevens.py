"""control pand to draw upon"""
import os

from qgis.PyQt import uic
import qgis.PyQt.QtCore as PQtC
import qgis.PyQt.QtWidgets as PQtW
import qgis.core as QC

import oiv.helpers.utils_core as UC
import oiv.helpers.utils_gui as UG
import oiv.tools.query_bag as QB
import oiv.tools.stackwidget as SW
import oiv.tools.print as PR
import oiv.helpers.messages as MSG
import oiv.helpers.configdb_helper as CH
import oiv.helpers.qt_helper as QT
import oiv.helpers.constants as PC
import oiv.werkvoorraad.oiv_werkvoorraad as OWW

from .oiv_bouwlaag import oivBouwlaagWidget
from .oiv_tekenen import oivTekenWidget
from .oiv_import_file import oivImportFileWidget

FORM_CLASS, _ = uic.loadUiType(os.path.join(
    os.path.dirname(__file__), PC.PAND["pandui"]))


class oivPandWidget(PQtW.QDockWidget, FORM_CLASS):

    sortedList = []

    def __init__(self, parent=None, objectId=None):
        super(oivPandWidget, self).__init__(parent)
        self.setupUi(self)
        self.baseWidget = parent
        self.iface = parent.iface
        self.canvas = parent.canvas
        self.selectTool = parent.selectTool
        self.polygonSelectTool = parent.polygonSelectTool
        self.pointTool = parent.pointTool
        self.drawTool = parent.drawTool
        self.moveTool = parent.moveTool
        self.identifyTool = parent.identifyTool
        self.initActions()

    def initUI(self):
        """fill the lineedits with values"""
        objectId = self.pand_id.text()
        self.baseobjectFrame.setVisible(True)
        self.addobjectFrame.setVisible(False)  
        self.bouwlagen_to_combobox(objectId, None)

    def initActions(self):
        """connect the buttons to their actions"""     
        self.bouwlaag_draw.clicked.connect(self.run_tekenen)
        self.addbutton.clicked.connect(self.bouwlaag_toevoegen)
        self.comboBox.currentIndexChanged.connect(self.set_layer_subset_bouwlaag)
        self.bouwlaag_info.clicked.connect(self.run_bouwlaag_bewerken)
        self.bouwlaag_bag.clicked.connect(self.openBagviewer)
        self.bouwlaag_delete.clicked.connect(self.run_delete)
        self.bouwlaag_inventory.clicked.connect(self.run_werkvoorraad)
        self.bouwlaag_print.clicked.connect(self.run_print)

    def bouwlaag_toevoegen(self):
        self.baseWidget.done.setEnabled(False)
        self.baseWidget.done_png.setEnabled(False)
        self.baseobjectFrame.setVisible(False)
        self.addobjectFrame.setVisible(True)
        self.bouwlaag_add.clicked.connect(self.run_bouwlaag)
        self.import_drawing.clicked.connect(self.run_import)
        self.georeferencer.clicked.connect(self.open_georeferencer)
        self.terug_add.clicked.connect(self.bouwlaag_toevoegen_sluiten)

    def bouwlaag_toevoegen_sluiten(self):
        self.baseWidget.done.setEnabled(True)
        self.baseWidget.done_png.setEnabled(True)
        self.baseobjectFrame.setVisible(True)
        self.addobjectFrame.setVisible(False)
        self.bouwlaag_add.clicked.disconnect(self.run_bouwlaag)
        self.import_drawing.clicked.disconnect(self.run_import)
        self.georeferencer.clicked.disconnect(self.open_georeferencer)
        self.terug_add.clicked.disconnect(self.bouwlaag_toevoegen_sluiten)

    def open_georeferencer(self):
        self.iface.mainWindow().findChildren(PQtW.QAction, 'mActionShowGeoreferencer')[0].trigger()

    def show_subwidget(self, show, widget=None):
        if show:
            self.baseWidget.tabWidget.setTabVisible(1, False)
            self.baseWidget.tabWidget.addTab(widget, '')
            self.baseWidget.tabWidget.setCurrentIndex(3)
        else:
            self.baseWidget.tabWidget.setTabVisible(1, True)
            self.baseWidget.tabWidget.setCurrentIndex(1)
            self.baseWidget.tabWidget.removeTab(3)

    def run_edit_bouwlagen(self, ilayer, ifeature):
        """edit attribute form of floor feature"""
        stackWidget = SW.oivStackWidget(self)
        self.show_subwidget(True, stackWidget)
        #stackWidget.parentWidget = self
        stackWidget.parentWidth = self.width()
        stackWidget.open_feature_form(ilayer, ifeature)

    def bouwlagen_to_combobox(self, objectId, actieveBouwlaag):
        """fill combobox with existing floors"""
        runLayer = PC.PAND["bouwlaaglayername"]
        tempLayer = UC.getlayer_byname(runLayer)
        objectId = self.pand_id.text()
        foreignKey = CH.get_foreign_key_bl(runLayer)
        tempLayer.setSubsetString('')
        #request all existing floors of object feature
        request = QC.QgsFeatureRequest().setFilterExpression(foreignKey + " = '" + str(objectId) + "'")
        tempFeatureIt = tempLayer.getFeatures(request)
        #create unique list of existing floors and sort it from small to big
        bouwlaagList = [it["bouwlaag"] for it in tempFeatureIt]
        self.sortedList = UC.create_unique_sorted_list(bouwlaagList)
        #block signal of combobox to add existing floors
        self.comboBox.blockSignals(True)
        self.comboBox.clear()
        for bouwlaag in reversed(self.sortedList):
            self.comboBox.addItem(str(bouwlaag))
        #if there are existing floors "tekenen" can be enabled
        if self.sortedList:
            self.existing_bouwlagen(True)
            if actieveBouwlaag is None:
                actieveBouwlaag = min(reversed(self.sortedList), key=abs)
        else:
            self.existing_bouwlagen(False)
            actieveBouwlaag = 1
        self.comboBox.blockSignals(False)
        #set substring of childlayers
        subString = "bouwlaag = " + str(actieveBouwlaag)
        UG.set_layer_substring(subString)
        index = self.comboBox.findText(str(actieveBouwlaag), PQtC.Qt.MatchFixedString)
        if index >= 0:
            self.comboBox.setCurrentIndex(index)
        self.baseWidget.statusregelBouwlaag.setText('U tekent op Bouwlaag: ' + self.comboBox.currentText())
        self.iface.actionPan().trigger()

    def existing_bouwlagen(self, existing):
        self.bouwlaag_info.setEnabled(existing)
        self.bouwlaag_delete.setEnabled(existing)
        self.bouwlaag_draw.setEnabled(existing)
        self.bouwlaag_inventory.setEnabled(existing)
        self.bouwlaag_print.setEnabled(existing)

    def set_layer_subset_bouwlaag(self):
        """if index of combobox has changed set cql filter of childlayers"""
        subString = "bouwlaag = " + str(self.comboBox.currentText())
        self.baseWidget.statusregelBouwlaag.setText('U tekent op Bouwlaag: ' + str(self.comboBox.currentText()))
        UG.set_layer_substring(subString)

    #select bouwlaag on canvas to edit the atrribute form
    def run_bouwlaag_bewerken(self):
        runLayer = PC.PAND["bouwlaaglayername"]
        iLayer = UC.getlayer_byname(runLayer)
        objectId = self.pand_id.text()
        foreignKey = CH.get_foreign_key_bl(runLayer)
        request = QC.QgsFeatureRequest().setFilterExpression(foreignKey + " = '" + str(objectId) + "'")
        ifeature = UC.featureRequest(iLayer, request)
        if ifeature:
            self.run_edit_bouwlagen(iLayer, ifeature)

    #add new floor
    def run_bouwlaag(self):
        while True:
            bouwlaag, bouwlaagMax, ok = BouwlaagDialog.getBouwlagen()
            if (bouwlaag != 0 and bouwlaagMax >= bouwlaag and ok is True):
                bouwlaagwidget = oivBouwlaagWidget(self, bouwlaag, bouwlaagMax)
                subString = "bouwlaag = " + str(bouwlaag)
                UG.set_layer_substring(subString)
                self.show_subwidget(True, bouwlaagwidget)
                break
            elif bouwlaagMax < bouwlaag:
                MSG.showMsgBox('bouwlaagvolgorde')
            elif ok is False:
                break

    def run_tekenen(self):
        """init teken widget"""
        tekenWidget = oivTekenWidget(self)
        subString = "bouwlaag = " + str(self.comboBox.currentText())
        UG.set_layer_substring(subString)
        self.show_subwidget(True, tekenWidget)

    def openBagviewer(self):
        """open url based on BAG pand_id, i.v.m. terugmelden"""
        url = PC.PAND["bagviewerurl"] + str(self.pand_id.text())
        UC.open_url(url)

    def run_delete(self):
        layerName = PC.PAND["bouwlaaglayername"]
        ilayer = UC.getlayer_byname(layerName)
        objectId = self.pand_id.text()
        request = QC.QgsFeatureRequest().setFilterExpression('"pand_id" = ' + "'{}'".format(objectId))
        ifeature = UC.featureRequest(ilayer, request)
        if ifeature:
            ilayer.selectByIds([ifeature.id()])
        reply = MSG.showMsgBox('deleteobject')
        if not reply:
            #als "nee" deselecteer alle geselecteerde features
            ilayer.deselect(ifeature.id())
        elif reply:
            #als "ja" -> verwijder de feature op basis van het unieke feature id
            ilayer.startEditing()
            ilayer.deleteFeature(ifeature.id())
            ilayer.commitChanges()
            reply = MSG.showMsgBox('deletedobject')
            UC.refresh_layers(self.iface)
            #set actieve bouwlaag to 1 and fill combobox
            self.bouwlagen_to_combobox(ifeature.id(), 1)
            
    def run_print(self):
        arrBouwlagen = [self.comboBox.itemText(i) for i in range(self.comboBox.count())]
        directory = PQtW.QFileDialog().getExistingDirectory()
        if directory != '':
            bouwlaagOrg = self.comboBox.currentText()
            for bouwlaag in arrBouwlagen:
                subString = "bouwlaag = {}".format(bouwlaag)
                UG.set_layer_substring(subString)
                fileName = '{}_bouwlaag_{}'.format(self.pand_id.text(), bouwlaag)
                filterString = '"identificatie"={}'.format(self.pand_id.text())
                PR.load_composer(directory, 'bouwlaag', filterString, fileName)
            MSG.showMsgBox('print_finished', directory)
            subString = "bouwlaag = {}".format(bouwlaagOrg)
            UG.set_layer_substring(subString)

    def run_werkvoorraad(self):
        werkvoorraadWidget = OWW.oivWerkvoorraadWidget(self)
        werkvoorraadWidget.bouwlaagOfObject = 'Bouwlaag'
        werkvoorraadWidget.initUI()
        self.show_subwidget(True, werkvoorraadWidget)
        
    def run_import(self):
        """initiate import widget"""
        importwidget = oivImportFileWidget(self)
        self.show_subwidget(True, importwidget)

class BouwlaagDialog(PQtW.QDialog):
    def __init__(self, parent=None):
        super(BouwlaagDialog, self).__init__(parent)
        bouwlagen = PC.PAND["bouwlagen"]
        minBouwlaag = bouwlagen["min"]
        maxBouwlaag = bouwlagen["max"]
        self.setWindowTitle("Bouwlagen toevoegen")
        qlayout = PQtW.QVBoxLayout(self)
        self.qlineA = PQtW.QLabel(self)
        self.qlineB = PQtW.QLabel(self)
        self.qlineC = PQtW.QLabel(self)
        self.qComboA = PQtW.QComboBox(self)
        self.qComboB = PQtW.QComboBox(self)
        self.qlineA.setText("U kunt meerdere bouwlagenlagen in 1x creeren, door van en t/m in te vullen!")
        self.qlineB.setText("Van:")
        self.qlineC.setText("Tot en met:")
        for i in range(maxBouwlaag - minBouwlaag + 1):
            if maxBouwlaag - i != 0:
                self.qComboA.addItem(str(maxBouwlaag - i))
                self.qComboB.addItem(str(maxBouwlaag - i))
                if maxBouwlaag - i == 1:
                    init_index = i
        self.qComboA.setCurrentIndex(init_index)
        self.qComboB.setCurrentIndex(init_index)
        self.qComboA.setFixedWidth(100)
        self.qComboA.setMaxVisibleItems(30)
        self.qComboB.setFixedWidth(100)
        self.qComboB.setMaxVisibleItems(30)
        self.qComboA.currentIndexChanged.connect(self.set_comboboxB)
        qlayout.addWidget(self.qlineA)
        qlayout.addWidget(self.qlineB)
        qlayout.addWidget(self.qComboA)
        qlayout.addWidget(self.qlineC)
        qlayout.addWidget(self.qComboB)
        buttons = PQtW.QDialogButtonBox(
            PQtW.QDialogButtonBox.Ok | PQtW.QDialogButtonBox.Cancel,
            PQtC.Qt.Horizontal, self)
        buttons.accepted.connect(self.accept)
        buttons.rejected.connect(self.reject)
        qlayout.addWidget(buttons)

    def set_comboboxB(self):
        ind = self.qComboA.currentIndex()
        self.qComboB.setCurrentIndex(ind)

    @staticmethod
    def getBouwlagen(parent=None):
        dialog = BouwlaagDialog(parent)
        result = dialog.exec_()
        return (int(dialog.qComboA.currentText()), int(dialog.qComboB.currentText()), result == PQtW.QDialog.Accepted)
