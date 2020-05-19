"""extension to plugin to import AutoCad or Shape files"""
import os
from qgis.PyQt import uic
from qgis.PyQt.QtCore import Qt
from qgis.PyQt.QtWidgets import QDockWidget, QFileDialog, QMessageBox, QProgressDialog, QProgressBar, QDialog, QComboBox, QGridLayout, QLabel, QDialogButtonBox, QVBoxLayout, QCheckBox

from qgis.core import QgsVectorLayer, QgsFeature, QgsGeometry, QgsProject, QgsFeatureRequest, QgsWkbTypes
from qgis.utils import iface

#from ..tools.identifyTool import IdentifyGeometryTool
from ..tools.utils_core import getlayer_byname, get_draw_layer_attr, write_layer, read_settings

FORM_CLASS, _ = uic.loadUiType(os.path.join(
    os.path.dirname(__file__), 'oiv_import_file_widget.ui'))

class oivImportFileWidget(QDockWidget, FORM_CLASS):
    """the actions class for the import"""

    parentWidget = None
    canvas = None
    selectTool = None
    importLayer = None
    read_config = None
    mappingDict = {}
    importlagen = ["Bouwkundige veiligheidsvoorzieningen", "Ruimten"]
    importlagen_types = {"Bouwkundige veiligheidsvoorzieningen": "veiligh_bouwk_types", "Ruimten" : "ruimten_type"}

    def __init__(self, parent=None):
        """Constructor."""
        super(oivImportFileWidget, self).__init__(parent)
        self.iface = iface
        self.setupUi(self)
        self.selectId.clicked.connect(self.run_select_bouwlaag)
        self.select_file.clicked.connect(self.selectfile)
        self.terug.clicked.connect(self.close_import)
        self.check.clicked.connect(self.check_importlayer)
        self.mapping.clicked.connect(self.run_mapping)
        self.import_laag.currentIndexChanged.connect(self.hide_import)
        self.type.currentIndexChanged.connect(self.hide_import)
        self.import_file.clicked.connect(self.inlezen)
        for laag in self.importlagen:
            self.import_laag.addItem(laag)
        self.hide_all()

    def selectfile(self):
        """select the import shap or dxf file"""
        dxf_info = None
        importFile = QFileDialog.getOpenFileName(None, "Selecteer bestand:", None, "AutoCad (*.dxf);;Shape (*.shp)")[0]
        self.bestandsnaam.setText(importFile)
        checkBouwlaag = False
        if importFile.endswith('.dxf'):
            checkBouwlaag, layerImportType, importBouwlaag, dummy = DxfDialog.getGeometryType()
            if layerImportType == 'lijn':
                layerType = 'LineString'
            else:
                layerType = 'Polygon'
            dxf_info = "|layername = entities|geometrytype=" + layerType
            importFileFeat = importFile + dxf_info
            if checkBouwlaag:
                importFilePolygon = importFile + "|layername = entities|geometrytype=Polygon"
                self.importPolygonLayer = QgsVectorLayer(importFilePolygon, "import", "ogr")
                it = self.importPolygonLayer.getFeatures()
                bouwlaagFeature = next(it)
                self.bouwlaag.setText(str(importBouwlaag))
                self.import_bouwlaag(bouwlaagFeature)
        else:
            importFileFeat = importFile
        self.importLayer = QgsVectorLayer(importFileFeat, "import", "ogr")
        QgsProject.instance().addMapLayer(self.importLayer, False)
        fields = self.importLayer.fields()
        for field in fields:
            self.type.addItem(field.name())
        if not checkBouwlaag:
            self.label2.setVisible(True)
            self.selectId.setVisible(True)

    def import_bouwlaag(self, bouwlaagFeature):
        """after the checks the import of the floor can start"""
        childFeature = QgsFeature()
        layerName = 'Bouwlagen'
        layer = getlayer_byname(layerName)
        #get necessary attributes from config file
        query = "SELECT foreign_key FROM config_bouwlaag WHERE child_layer = '{}'".format(layerName)
        foreignKey = read_settings(query, False)[0]
        #construct QgsFeature to save
        childFeature.setGeometry(bouwlaagFeature.geometry())
        fields = layer.fields()
        childFeature.initAttributes(fields.count())
        childFeature.setFields(fields)
        childFeature[foreignKey] = str(self.object_id.text())
        childFeature["bouwlaag"] = int(self.bouwlaag.text())
        newFeatureId = write_layer(layer, childFeature)
        self.bouwlaag_id.setText(str(newFeatureId))
        self.iface.actionPan().trigger()
        self.label2.setVisible(False)
        self.selectId.setVisible(False)
        self.label3.setVisible(True)
        self.label4.setVisible(True)
        self.label5a.setVisible(True)
        self.label5b.setVisible(True)
        self.import_laag.setVisible(True)
        self.check.setVisible(True)
        self.type.setVisible(True)

    def hide_import(self):
        """hide import button"""
        self.label6.setVisible(False)
        self.import_file.setVisible(False)

    def check_importlayer(self):
        """perform geometric checks on importlayer"""
        checks = [None ,None]
        message = ''
        crsCheck = self.importLayer.crs().authid()
        if crsCheck == 'EPSG:28992':
            checks[0] = 'RD'
        if self.import_laag.currentText() == "Bouwkundige veiligheidsvoorzieningen":
            if self.importLayer.geometryType() == QgsWkbTypes.LineGeometry:
                checks[1] = 'passed'
            else:
                checks[1] = None
        elif self.import_laag.currentText() == "Ruimten":
            if self.importLayer.geometryType() == QgsWkbTypes.PolygonGeometry:
                checks[1] = 'passed'
            else:
                checks[1] = None
        if checks[0] is not None and checks[1] is not None:
            message = 'Alle checks uitgevoerd u kunt doorgaan met importeren!'
            QMessageBox.information(None, "INFO:", message)
            self.label6.setVisible(True)
            self.mapping.setVisible(True)
        else:
            if checks[0] != 'RD':
                message = 'Het coordinatenstelsel is geen RD!<br><br>'
            if checks[1] is None:
                message = message + 'De geometrie in het bestand komt niet overeen met de geselecteerde laag!<br><br>'
            message = message + '<br>Pas dit aan voordat je verder gaat met inlezen!'
            QMessageBox.information(None, "ERROR:", message)

    def read_types(self, layername):
        types = []
        layer = getlayer_byname(layername)
        for feat in layer.getFeatures():
            types.append(feat[1])
        return types

    def progressdialog(self, progress):
        pdialog = QProgressDialog()
        pdialog.setWindowTitle("Progress")
        pdialog.setLabelText("Voortgang van importeren:")
        pbar = QProgressBar(pdialog)
        pbar.setTextVisible(True)
        pbar.setValue(progress)
        pdialog.setBar(pbar)
        pdialog.setMinimumWidth(300)
        pdialog.show()
        return pdialog, pbar

    def inlezen(self):
        """import the file after all settings wehere made"""
        targetLayerName = self.import_laag.currentText()
        if targetLayerName == "Ruimten":
            typeLayer = getlayer_byname('ruimten_type')
        targetFeature = QgsFeature()
        targetLayer = getlayer_byname(targetLayerName)
        targetFields = targetLayer.fields()
        targetFeature.initAttributes(targetFields.count())
        query = "SELECT identifier FROM config_bouwlaag WHERE child_layer = '{}'".format(targetLayerName)
        identifier = read_settings(query, False)[0]        
        targetFeature.setFields(targetFields)
        self.iface.setActiveLayer(self.importLayer)
        dummy, progressBar = self.progressdialog(0)
        progressBar.setValue(0)
        progressBar.setMaximum(100)
        count = 0
        cntFeat = self.importLayer.featureCount()
        for feature in self.importLayer.getFeatures():
            count += 1
            if self.mappingDict[feature[self.type.currentText()]] != 'niet importeren':
                if self.importLayer.geometryType() == QgsWkbTypes.PolygonGeometry:
                    geom = QgsGeometry.fromPolygonXY(feature.geometry().asPolygon())
                elif self.importLayer.wkbType() == QgsWkbTypes.MultiLineString:
                    geom = QgsGeometry.fromMultiPolylineXY(feature.geometry().asMultiPolyline())
                else:
                    geom = QgsGeometry.fromPolylineXY(feature.geometry().asPolyline())

                targetFeature.setGeometry(geom)
                targetFeature["bouwlaag_id"] = int(self.bouwlaag_id.text())
                if targetLayerName == "Ruimten":
                    request = QgsFeatureRequest().setFilterExpression('"naam" = ' + "'" + self.mappingDict[feature[self.type.currentText()]] + "'")
                    tempFeature = next(typeLayer.getFeatures(request))
                    targetFeature[identifier] = tempFeature["id"]
                else:
                    targetFeature[identifier] = self.mappingDict[feature[self.type.currentText()]]
                write_layer(targetLayer, targetFeature)
            progress = (float(count)/float(cntFeat)) * 100
            progressBar.setValue(progress)
        message = 'Alle feature zijn succesvol geimporteerd!'
        QMessageBox.information(None, "INFO:", message)
        QgsProject.instance().removeMapLayers([self.importLayer.id()])

    def run_select_bouwlaag(self):
        """activate the selection tool"""
        try:
            self.selectTool.geomSelected.disconnect()
        except: # pylint: disable=bare-except
            pass
        self.canvas.setMapTool(self.selectTool)
        self.selectTool.geomSelected.connect(self.set_parent_id)

    def run_mapping(self):
        """get attribute mapping from the user"""
        typeLayerName = self.importlagen_types[self.import_laag.currentText()]
        targetTypes = self.read_types(typeLayerName)
        targetTypes.append("niet importeren")
        importTypes = []
        importAttribute = self.type.currentText()
        for feat in self.importLayer.getFeatures():
            if feat[importAttribute] not in importTypes:
                importTypes.append(feat[importAttribute])
        MappingDialog.targetTypes = targetTypes
        MappingDialog.importTypes = importTypes
        self.mappingDict, dummy = MappingDialog.getMapping()
        self.label7.setVisible(True)
        self.import_file.setVisible(True)

    def set_parent_id(self, ilayer, ifeature):
        """let user select the floor which to link to"""
        if ilayer.name() == 'Bouwlagen':
            self.bouwlaag_id.setText(str(ifeature["id"]))
            self.selectTool.geomSelected.disconnect(self.set_parent_id)
            self.label3.setVisible(True)
            self.label4.setVisible(True)
            self.label5a.setVisible(True)
            self.label5b.setVisible(True)
            self.import_laag.setVisible(True)
            self.check.setVisible(True)
            self.type.setVisible(True)
        else:
            self.run_select_bouwlaag()

    def hide_all(self):
        """when the import start hide all on the UI"""
        self.check.setVisible(False)
        self.bouwlaag_id.setVisible(False)
        self.label1.setVisible(True)
        self.label2.setVisible(False)
        self.label3.setVisible(False)
        self.label4.setVisible(False)
        self.label5a.setVisible(False)
        self.label5b.setVisible(False)
        self.label6.setVisible(False)
        self.label7.setVisible(False)
        self.mapping.setVisible(False)
        self.selectId.setVisible(False)
        self.type.setVisible(False)
        self.select_file.setVisible(True)
        self.bestandsnaam.setVisible(True)
        self.import_file.setVisible(False)
        self.import_laag.setVisible(False)

    def close_import(self):
        """close feature form and save changes"""
        self.hide_all()
        self.close()
        self.parentWidget.bouwlagen_to_combobox(str(self.object_id.text()), int(self.bouwlaag.text()))
        try:
            self.parentWidget.show()
            del self.parentWidget
        except: # pylint: disable=bare-except
            pass
        try:
            QgsProject.instance().removeMapLayers([self.importLayer.id()])
        except: # pylint: disable=bare-except
            pass
        del self

class MappingDialog(QDialog):
    """construct the mapping GUI"""

    targetTypes = []
    importTypes = []
    labels = {}
    comboBoxes = {}

    def __init__(self, parent=None):
        super(MappingDialog, self).__init__(parent)
        self.setWindowTitle("Maak een mapping t.b.v. het importeren")
        qlayout = QGridLayout(self)
        i = 0
        for importType in self.importTypes:
            self.labels[i] = QLabel(self)
            self.labels[i].setText(importType)
            self.comboBoxes[i] = QComboBox(self)
            self.comboBoxes[i].addItems(self.targetTypes)
            qlayout.addWidget(self.labels[i],i,0)
            qlayout.addWidget(self.comboBoxes[i], i, 1)
            i += 1
        buttons = QDialogButtonBox(
            QDialogButtonBox.Ok | QDialogButtonBox.Cancel,
            Qt.Horizontal, self)
        buttons.accepted.connect(self.accept)
        buttons.rejected.connect(self.reject)
        qlayout.addWidget(buttons)

    @staticmethod
    def getMapping(parent=None):
        """initiate the GUI and redirect the input"""
        mapping = {}
        dialog = MappingDialog(parent)
        result = dialog.exec_()
        for i in range(len(dialog.importTypes)):
            mapping.update({dialog.labels[i].text(): dialog.comboBoxes[i].currentText()})
        return (mapping, result == QDialog.Accepted)

class DxfDialog(QDialog):
    """construct the import GUI"""

    def __init__(self, parent=None):
        super(DxfDialog, self).__init__(parent)
        self.setWindowTitle("Type geometrie")
        max_bouwlaag = 30
        min_bouwlaag = -10
        qlayout = QVBoxLayout(self)
        self.label1 = QLabel(self)
        self.label1.setText("Welke type geometrie wilt u importeren?")
        qlayout.addWidget(self.label1)
        self.inputGeometry = QComboBox(self)
        self.inputGeometry.addItems(['lijn', 'vlak'])
        qlayout.addWidget(self.inputGeometry)
        self.label2 = QLabel(self)
        self.label2.setText("Wilt u de polygoon importeren als Bouwlaag?")
        qlayout.addWidget(self.label2)
        self.checkBouwlaag = QCheckBox(self)
        qlayout.addWidget(self.checkBouwlaag)
        self.checkBouwlaag.stateChanged.connect(self.addBouwlaagQuestion)
        self.qComboA = QComboBox(self)
        for i in range(max_bouwlaag - min_bouwlaag + 1):
            if max_bouwlaag - i != 0:
                self.qComboA.addItem(str(max_bouwlaag - i))
                if max_bouwlaag - i == 1:
                    init_index = i
        self.qComboA.setCurrentIndex(init_index) 
        self.qComboA.setFixedWidth(100)
        self.qComboA.setMaxVisibleItems(30)
        self.label3 = QLabel(self)
        self.label3.setText("Geef de bouwlaag op waarvoor u de polygoon wilt inlezen.")
        self.qComboA.setVisible(False)
        self.label3.setVisible(False)
        qlayout.addWidget(self.label3)
        qlayout.addWidget(self.qComboA)
        buttons = QDialogButtonBox(
            QDialogButtonBox.Ok | QDialogButtonBox.Cancel,
            Qt.Horizontal, self)
        buttons.accepted.connect(self.accept)
        buttons.rejected.connect(self.reject)
        qlayout.addWidget(buttons)

    def addBouwlaagQuestion(self):
        """ask user if they want to import for multiple floors"""
        if self.qComboA.isVisible():
            self.qComboA.setVisible(False)
            self.label3.setVisible(False)
        else:
            self.qComboA.setVisible(True)
            self.label3.setVisible(True)

    @staticmethod
    def getGeometryType(parent = None):
        """Contains DXF line or polygon geometrie"""
        dialog = DxfDialog(parent)
        result = dialog.exec_()
        return (dialog.checkBouwlaag.isChecked(), dialog.inputGeometry.currentText(), dialog.qComboA.currentText(), result == QDialog.Accepted)
