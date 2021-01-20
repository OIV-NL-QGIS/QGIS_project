"""extension to plugin to import AutoCad or Shape files"""
import os
from osgeo import ogr
from qgis.PyQt import uic
from qgis.PyQt.QtCore import Qt
from qgis.PyQt.QtWidgets import QDockWidget, QPushButton, QFileDialog, QMessageBox, QDialog, QComboBox, QGridLayout, QLabel, QDialogButtonBox, QVBoxLayout, QCheckBox

from qgis.core import QgsVectorLayer, QgsFeature, QgsProject, QgsFeatureRequest, QgsExpression
from qgis.utils import iface

from .utils_core import getlayer_byname, write_layer, check_layer_type, read_settings
from .utils_gui import get_actions
from .editFeature import getfeature_geometry

FORM_CLASS, _ = uic.loadUiType(os.path.join(
    os.path.dirname(__file__), 'oiv_import_filewidget.ui'))

class oivImportFileWidget(QDockWidget, FORM_CLASS):
    """the actions class for the import"""

    parentWidget = None
    canvas = None
    selectTool = None
    importLayer = None
    layerImportType = None
    mappingDict = {}
    layerTypes = ['Point', 'LineString', 'Polygon']

    def __init__(self, parent=None):
        """Constructor."""
        super(oivImportFileWidget, self).__init__(parent)
        self.iface = iface
        self.setupUi(self)
        self.select_file.clicked.connect(self.selectfile)
        self.terug.clicked.connect(self.close_import)
        self.mapping.clicked.connect(self.run_mapping)
        self.import_file.clicked.connect(self.inlezen)
        self.hide_all()

    def selectfile(self):
        """select the import shape or dxf file"""
        dxfInfo = None
        importFile = QFileDialog.getOpenFileName(None, "Selecteer bestand:", None, "AutoCad (*.dxf);;Shape (*.shp);;GeoPackage (*.gpkg)")[0]
        self.bestandsnaam.setText(importFile)
        if importFile:
            if importFile.endswith('.dxf'):
                self.layerImportType, ok = DxfDialogObject.getGeometryType()
                dxfInfo = "|layername=entities|geometrytype=" + self.layerImportType
                importFileFeat = importFile + dxfInfo
                if not self.layerImportType or not ok:
                    return
                self.importLayer = QgsVectorLayer(importFileFeat, "import", "ogr")
            elif importFile.endswith('.gpkg'):
                layerNames = [l.GetName() for l in ogr.Open(importFile)]
                GpkgDialog.layerNames = layerNames
                layerName, dummy = GpkgDialog.getLayerName()
                gpkgInfo = "|layername={}".format(layerName)
                importFileFeat = importFile + gpkgInfo
                self.importLayer = QgsVectorLayer(importFileFeat, "import", "ogr")
            else:
                importFileFeat = importFile
                self.importLayer = QgsVectorLayer(importFileFeat, "import", "ogr")
                if self.importLayer.geometryType() < 3:
                    self.layerImportType = self.layerTypes[self.importLayer.geometryType()]
                else:
                    return
        else:
            return
        crs = self.importLayer.crs()
        crs.createFromId(28992)
        self.importLayer.setCrs(crs)
        QgsProject.instance().addMapLayer(self.importLayer, True)
        fields = self.importLayer.fields()
        for field in fields:
            self.type.addItem(field.name())
        self.label3.setVisible(True)
        self.type.setVisible(True)
        self.label6.setVisible(True)
        self.mapping.setVisible(True)

    def read_types(self):
        types = {}
        actionList, dummy, dummy = get_actions('config_object')
        for lst in actionList:
            tempList = []
            for action in lst:
                layerName = action[0]
                layer = getlayer_byname(layerName)
                layerType = check_layer_type(layer)
                tempList.append(action[1])
            tempList.append("niet importeren")
            if layerType in types:
                types[layerType].update({layerName : tempList})
            else:
                types.update({layerType : {layerName : tempList}})
        return types

    def inlezen(self):
        """import the file after all settings wehere made"""
        importAttr = self.type.currentText()
        invalidCount = 0
        for importType in self.mappingDict:
            if self.mappingDict[importType]["targetType"] != 'niet importeren':
                checkConv = False
                expr = QgsExpression('"{}"= \'{}\''.format(importAttr, importType))
                featureIt = self.importLayer.getFeatures(QgsFeatureRequest(expr))
                targetFeature = QgsFeature()
                targetLayerName = self.mappingDict[importType]["layerName"]
                if 'Labels' in targetLayerName:
                    LabelDialog.attributes = [self.type.itemText(i) for i in range(self.type.count())]
                    LabelDialog.importType = importType
                    labelField, dummy = LabelDialog.getLabelAtrribute()
                targetLayer = getlayer_byname(targetLayerName)
                targetFields = targetLayer.fields()
                targetFeature.initAttributes(targetFields.count())
                targetFeature.setFields(targetFields)
                if self.mappingDict[importType]["convType"] != self.layerImportType:
                    checkConv = True
                query = "SELECT foreign_key, identifier, input_label FROM config_object WHERE child_layer = '{}'".format(targetLayerName)
                attrs = read_settings(query, False)[0]
                targetFeature[attrs[1]] = self.mappingDict[importType]["targetType"]
                targetFeature[attrs[0]] = self.object_id.text()
                targetLayer.startEditing()

                for feat in featureIt:
                    geom = None
                    if not checkConv:
                        geom = getfeature_geometry(feat.geometry(), self.layerImportType)
                        if 'Labels' in targetLayerName:
                            if feat[labelField]:
                                targetFeature[attrs[2]] = feat[labelField]
                            else:
                                targetFeature[attrs[2]] = 'geen label'
                    if geom:
                        targetFeature.setGeometry(geom)
                        invalidCheck = write_layer(targetLayer, targetFeature, True)
                        if invalidCheck == 'invalid':
                            invalidCount += 1
                targetLayer.commitChanges()
        if invalidCount > 0:
            message = ('Features zijn geimporteerd.\n'
                       '{} features zijn niet geimporteerd vanwege ongeldige geometrie!'.format(invalidCount))
        else:
            message = 'Alle feature zijn succesvol geimporteerd!'
        QMessageBox.information(None, "INFO:", message)
        QgsProject.instance().removeMapLayers([self.importLayer.id()])

    def run_mapping(self):
        """get attribute mapping from the user"""
        targetTypes = self.read_types()
        importTypes = []
        importAttribute = self.type.currentText()
        for feat in self.importLayer.getFeatures():
            if feat[importAttribute] not in importTypes:
                importTypes.append(feat[importAttribute])
        if self.layerImportType == 'Point':
            MappingDialog.layerType = ['Point']
        else:
            MappingDialog.layerType = ['LineString', 'Polygon']
        MappingDialog.targetTypes = targetTypes
        MappingDialog.importTypes = importTypes
        self.mappingDict, ok = MappingDialog.getMapping()
        if ok:
            self.label7.setVisible(True)
            self.import_file.setVisible(True)

    def hide_all(self):
        """when the import start hide all on the UI"""
        self.bouwlaag_id.setVisible(False)
        self.label1.setVisible(True)
        self.label3.setVisible(False)
        self.label6.setVisible(False)
        self.label7.setVisible(False)
        self.mapping.setVisible(False)
        self.type.setVisible(False)
        self.select_file.setVisible(True)
        self.bestandsnaam.setVisible(True)
        self.import_file.setVisible(False)

    def close_import(self):
        """close feature form and save changes"""
        try:
            QgsProject.instance().removeMapLayers([self.importLayer.id()])
        except: # pylint: disable=bare-except
            pass
        self.hide_all()
        self.close()
        try:
            self.parentWidget.show()
            del self.parentWidget
        except: # pylint: disable=bare-except
            pass
        del self

class MappingDialog(QDialog):
    """construct the mapping GUI"""

    targetTypes = []
    importTypes = []
    layerType = []
    labels = {}
    comboBoxesType = {}
    comboBoxesLayer = {}
    comboBoxesLayerType = {}
    nextButton = None
    prevButton = None

    def __init__(self, parent=None):
        super(MappingDialog, self).__init__(parent)
        self.setWindowTitle("Maak een mapping t.b.v. het importeren")
        self.qlayout = QGridLayout(self)
        self.setWindowFlag(Qt.WindowCloseButtonHint, False)
        self.buttons = QDialogButtonBox(
            QDialogButtonBox.Ok | QDialogButtonBox.Cancel,
            Qt.Horizontal, self)
        self.buttons.accepted.connect(self.accept)
        self.buttons.rejected.connect(self.reject)
        self.nextButton = QPushButton()
        self.nextButton.setText("Volgende")
        self.prevButton = QPushButton()
        self.prevButton.setText("Vorige")
        self.label_laag = QLabel(self)
        self.label_laag.setText("Importeer in laag")
        self.label_types = QLabel(self)
        self.label_types.setText("Import types in bestand")
        self.label_conversie = QLabel(self)
        self.label_conversie.setText("Conversie naar type laag")
        self.label_target = QLabel(self)
        self.label_target.setText("Converteer naar type")
        self.qlayout.addWidget(self.label_types, 0, 0)
        self.qlayout.addWidget(self.label_conversie, 0, 1)
        self.qlayout.addWidget(self.label_laag, 0, 2)
        self.qlayout.addWidget(self.label_target, 0, 3)
        self.load_types()

    def load_types(self):
        i = 1
        for importType in self.importTypes:
            try:
                self.comboBoxesLayer[importType].setEnabled(False)
            except: # pylint: disable=bare-except
                pass
            self.labels[i] = QLabel(self)
            self.labels[i].setText(importType)
            self.comboBoxesLayerType[importType] = QComboBox(self)
            self.comboBoxesLayerType[importType].addItems(self.layerType)
            self.qlayout.addWidget(self.labels[i], i, 0)
            self.qlayout.addWidget(self.comboBoxesLayerType[importType], i, 1)
            self.comboBoxesLayerType[importType].setEnabled(False)
            i += 1
        self.qlayout.addWidget(self.nextButton, i, 1)
        self.qlayout.addWidget(self.prevButton, i, 0)
        self.qlayout.addWidget(self.buttons, i + 1, 0)
        self.set_buttons(False, True, None, self.load_layertype, False)

    def load_layertype(self):
        i = 1
        for importType in self.comboBoxesLayerType:
            try:
                self.comboBoxesType[importType].setEnabled(False)
            except: # pylint: disable=bare-except
                pass
            self.comboBoxesLayerType[importType].setEnabled(False)
            self.comboBoxesLayer[importType] = QComboBox(self)
            layerType = self.comboBoxesLayerType[importType].currentText()
            layerNames = self.targetTypes[layerType].keys()
            self.comboBoxesLayer[importType].addItems(layerNames)
            self.qlayout.addWidget(self.comboBoxesLayer[importType], i, 2)
            i += 1
        self.set_buttons(True, True, self.load_types, self.load_targettypes, False)

    def load_targettypes(self):
        i = 1
        for importType in self.comboBoxesLayer:
            self.comboBoxesLayer[importType].setEnabled(False)
            self.comboBoxesType[importType] = QComboBox(self)
            layerType = self.comboBoxesLayerType[importType].currentText()
            layerName = self.comboBoxesLayer[importType].currentText()
            types = self.targetTypes[layerType][layerName]
            self.comboBoxesType[importType].addItems(types)
            self.qlayout.addWidget(self.comboBoxesType[importType], i, 3)
            i += 1
        self.set_buttons(True, False, self.load_layertype, None, True)

    def set_buttons(self, prev, nxt, conPrev, conNext, okBtn):
        try:
            self.prevButton.clicked.disconnect()
        except: # pylint: disable=bare-except
            pass
        try:
            self.nextButton.clicked.disconnect()
        except: # pylint: disable=bare-except
            pass
        self.prevButton.setEnabled(prev)
        self.nextButton.setEnabled(nxt)
        if conPrev:
            self.prevButton.clicked.connect(conPrev)
        if conNext:
            self.nextButton.clicked.connect(conNext)
        self.buttons.button(QDialogButtonBox.Ok).setEnabled(okBtn)

    @staticmethod
    def getMapping(parent=None):
        """initiate the GUI and redirect the input"""
        mapping = {}
        dialog = MappingDialog(parent)
        result = dialog.exec_()
        for importType in dialog.importTypes:
            try:
                convType = dialog.comboBoxesLayerType[importType].currentText()
            except: # pylint: disable=bare-except
                convType = None
            try:
                convLayer = dialog.comboBoxesLayer[importType].currentText()
            except: # pylint: disable=bare-except
                convLayer = None
            try:
                convTargetType = dialog.comboBoxesType[importType].currentText()
            except: # pylint: disable=bare-except
                convTargetType = None
            mapping.update({importType : {"convType" : convType, "layerName" : convLayer, "targetType" : convTargetType}})
        return (mapping, result == QDialog.Accepted)

class DxfDialogObject(QDialog):
    """construct the import GUI"""

    def __init__(self, parent=None):
        super(DxfDialogObject, self).__init__(parent)
        self.setWindowTitle("Type geometrie")
        qlayout = QVBoxLayout(self)
        self.label1 = QLabel(self)
        self.label1.setText("Welke type geometrie wilt u importeren?")
        qlayout.addWidget(self.label1)
        self.inputGeometry = QComboBox(self)
        self.inputGeometry.addItems(['punt', 'lijn', 'vlak'])
        qlayout.addWidget(self.inputGeometry)
        buttons = QDialogButtonBox(
            QDialogButtonBox.Ok,
            Qt.Horizontal, self)
        buttons.accepted.connect(self.accept)
        buttons.rejected.connect(self.reject)
        qlayout.addWidget(buttons)

    @staticmethod
    def getGeometryType(parent = None):
        """Contains DXF line or polygon geometrie"""
        dialog = DxfDialogObject(parent)
        result = dialog.exec_()
        layerImportType = dialog.inputGeometry.currentText()
        if layerImportType == 'punt':
            layerType = 'Point'
        elif layerImportType == 'lijn':
            layerType = 'LineString'
        elif layerImportType == 'vlak':
            layerType = 'Polygon'
        else:
            layerType = None
        return (layerType, result == QDialog.Accepted)

class LabelDialog(QDialog):
    """construct the import GUI"""

    attributes = []
    importType = ''

    def __init__(self, parent=None):
        super(LabelDialog, self).__init__(parent)
        self.setWindowTitle(self.importType)
        qlayout = QVBoxLayout(self)
        self.label1 = QLabel(self)
        self.label1.setText("Welke attribute bevat de label waarde?")
        qlayout.addWidget(self.label1)
        self.labelAtrribute = QComboBox(self)
        self.labelAtrribute.addItems(self.attributes)
        qlayout.addWidget(self.labelAtrribute)
        buttons = QDialogButtonBox(
            QDialogButtonBox.Ok | QDialogButtonBox.Cancel,
            Qt.Horizontal, self)
        buttons.accepted.connect(self.accept)
        buttons.rejected.connect(self.reject)
        qlayout.addWidget(buttons)

    @staticmethod
    def getLabelAtrribute(parent = None):
        """Contains DXF line or polygon geometrie"""
        dialog = LabelDialog(parent)
        result = dialog.exec_()
        labelAtrribute = dialog.labelAtrribute.currentText()
        return (labelAtrribute, result == QDialog.Accepted)

class GpkgDialog(QDialog):
    """construct the import GUI"""
    layerNames = []

    def __init__(self, parent=None):
        super(GpkgDialog, self).__init__(parent)
        self.setWindowTitle("Kies de laag die u wilt importeren")
        qlayout = QVBoxLayout(self)
        self.qComboA = QComboBox(self)
        self.qComboA.addItems(self.layerNames)
        self.qComboA.setFixedWidth(300)
        self.qComboA.setMaxVisibleItems(30)
        self.label3 = QLabel(self)
        qlayout.addWidget(self.qComboA)
        buttons = QDialogButtonBox(
            QDialogButtonBox.Ok | QDialogButtonBox.Cancel,
            Qt.Horizontal, self)
        buttons.accepted.connect(self.accept)
        buttons.rejected.connect(self.reject)
        qlayout.addWidget(buttons)

    @staticmethod
    def getLayerName(parent = None):
        """Contains GeoPackage layername"""
        dialog = GpkgDialog(parent)
        result = dialog.exec_()
        return (dialog.qComboA.currentText(), result == QDialog.Accepted)
