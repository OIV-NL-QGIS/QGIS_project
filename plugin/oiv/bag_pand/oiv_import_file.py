"""extension to plugin to import AutoCad or Shape files"""
import os
from osgeo import ogr
from qgis.PyQt import uic
import qgis.PyQt.QtCore as PQtC
import qgis.PyQt.QtWidgets as PQtW
import qgis.core as QC

import oiv.helpers.utils_core as UC
import oiv.helpers.messages as MSG
import oiv.helpers.configdb_helper as CH
import oiv.helpers.constants as PC
import oiv.helpers.qt_helper as QT

FORM_CLASS, _ = uic.loadUiType(os.path.join(
    os.path.dirname(__file__), 'oiv_import_file_widget.ui'))


class oivImportFileWidget(PQtW.QDockWidget, FORM_CLASS):
    """the actions class for the import"""

    selectTool = None
    importLayer = None
    importTypeFile = None
    importPolygonLayer = None
    mappingDict = {}
    importlagen = ["Bouwkundige veiligheidsvoorzieningen", "Ruimten"]
    importlagen_types = {"Bouwkundige veiligheidsvoorzieningen": "veiligh_bouwk_type", "Ruimten": "ruimten_type"}

    def __init__(self, parent=None):
        """Constructor."""
        super(oivImportFileWidget, self).__init__(parent)
        self.setupUi(self)
        self.parent = parent
        self.iface = parent.iface
        self.canvas = parent.canvas
        self.object_id.setText(parent.pand_id.text())
        self.bouwlaag.setText(parent.comboBox.currentText())
        self.selectTool = parent.selectTool
        self.initUI()

    def initUI(self):
        self.selectId.clicked.connect(self.run_select_bouwlaag)
        self.select_file.clicked.connect(self.selectfile)
        self.terug.clicked.connect(self.close_import)
        self.check.clicked.connect(self.check_importlayer)
        self.mapping.clicked.connect(self.run_mapping)
        self.import_laag.currentIndexChanged.connect(self.hide_import)
        self.type.currentIndexChanged.connect(self.hide_import)
        self.validatie_import.clicked.connect(self.inlezen_validatie)
        self.import_file.clicked.connect(self.inlezen)
        self.helpBtn, self.floatBtn, titleBar = QT.getTitleBar()
        self.setTitleBarWidget(titleBar)
        self.helpBtn.clicked.connect(lambda: UC.open_url(PC.HELPURL["bouwlaagimporthelp"]))
        self.floatBtn.clicked.connect(lambda: self.setFloating(True))
        for laag in self.importlagen:
            self.import_laag.addItem(laag)
        self.hide_all()

    def selectfile(self):
        """select the import shap or dxf file"""
        dxfInfo = None
        importFile = PQtW.QFileDialog.getOpenFileName(None, "Selecteer bestand:", None,
                                                      "AutoCad (*.dxf);;Shape (*.shp);;GeoPackage (*.gpkg)")[0]
        self.bestandsnaam.setText(importFile)
        if importFile.endswith('.dxf'):
            layerImportType, dummy = DxfDialog.getGeometryType()
            if layerImportType == 'lijn':
                layerType = 'LineString'
            else:
                layerType = 'Polygon'
            dxfInfo = "|layername=entities|geometrytype=" + layerType
            importFileFeat = importFile + dxfInfo
            self.importTypeFile = 'DXF'
        elif importFile.endswith('.gpkg'):
            layerNames = [lyr.GetName() for lyr in ogr.Open(importFile)]
            GpkgDialog.layerNames = layerNames
            layerName, dummy = GpkgDialog.getLayerName()
            gpkgInfo = "|layername={}".format(layerName)
            importFileFeat = importFile + gpkgInfo
            self.importTypeFile = 'GPKG'
        else:
            importFileFeat = importFile
            self.importTypeFile = 'SHP'
        self.importLayer = QC.QgsVectorLayer(importFileFeat, "import", "ogr")
        QC.QgsProject.instance().addMapLayer(self.importLayer, True)
        fields = self.importLayer.fields()
        for field in fields:
            self.type.addItem(field.name())
        self.label2.setVisible(True)
        self.selectId.setVisible(True)

    def hide_import(self):
        """hide import button"""
        self.label6.setVisible(False)
        self.import_file.setVisible(False)

    def check_importlayer(self):
        """perform geometric checks on importlayer"""
        checks = [None, None]
        crsCheck = self.importLayer.crs().authid()
        if crsCheck == 'EPSG:28992':
            checks[0] = 'RD'
        if self.import_laag.currentText() == "Bouwkundige veiligheidsvoorzieningen":
            if self.importLayer.geometryType() == QC.QgsWkbTypes.LineGeometry:
                checks[1] = 'passed'
            else:
                checks[1] = None
        elif self.import_laag.currentText() == "Ruimten":
            if self.importLayer.geometryType() == QC.QgsWkbTypes.PolygonGeometry:
                checks[1] = 'passed'
            else:
                checks[1] = None
        if checks[0] is not None and checks[1] is not None:
            MSG.showMsgBox('importchecksok')
            self.label6.setVisible(True)
            self.mapping.setVisible(True)
        else:
            if checks[0] != 'RD':
                MSG.showMsgBox('importerrorrdstelsel')
            if checks[1] is None:
                MSG.showMsgBox('importerrorgeometrie')

    def read_types(self, layername):
        types = []
        layer = UC.getlayer_byname(layername)
        for feat in layer.getFeatures():
            types.append(feat["naam"])
        return types

    def progressdialog(self, progress):
        pdialog = PQtW.QProgressDialog()
        pdialog.setWindowTitle("Progress")
        pdialog.setLabelText("Voortgang van importeren:")
        pbar = PQtW.QProgressBar(pdialog)
        pbar.setTextVisible(True)
        pbar.setValue(progress)
        pdialog.setBar(pbar)
        pdialog.setMinimumWidth(300)
        pdialog.show()
        pbar.setValue(0)
        pbar.setMaximum(100)
        return pdialog, pbar

    def init_layer_fields(self, fields, params):
        layer = QC.QgsVectorLayer(params[0], params[1], params[2])
        pr = layer.dataProvider()
        pr.addAttributes(fields)
        layer.updateFields()
        return layer

    def get_centroid(self):
        tempLayer = UC.getlayer_byname('Bouwlagen')
        req = '"id" = ' + self.bouwlaag_id.text()
        request = QC.QgsFeatureRequest().setFilterExpression(req)
        ifeature = UC.featureRequest(tempLayer, request)
        if ifeature:
            return ifeature.geometry().centroid()

    def inlezen(self):
        features = []
        targetLayerName = self.import_laag.currentText()
        targetLayer = UC.getlayer_byname(targetLayerName)
        sourceLayerName = 'tempImport'
        sourceLayer = UC.getlayer_byname(sourceLayerName)
        if sourceLayer:
            for feature in sourceLayer.getFeatures():
                features.append(feature)
            UC.write_layer(targetLayer, features, False, False)
            QC.QgsProject.instance().removeMapLayers([sourceLayer.id()])
        ingangFeatures = []
        targetIngangLayerName = "Ingang bouwlaag"
        targetIngangLayer = UC.getlayer_byname(targetIngangLayerName)
        sourceIngangLayerName = 'tempImportIngang'
        sourceIngangLayer = UC.getlayer_byname(sourceIngangLayerName)
        if sourceIngangLayer:
            for feature in sourceIngangLayer.getFeatures():
                ingangFeatures.append(feature)
            UC.write_layer(targetIngangLayer, ingangFeatures, False, False)
            QC.QgsProject.instance().removeMapLayers([sourceIngangLayer.id()])
        MSG.showMsgBox('importsuccesfull')

    def init_templayers(self, targetLayer):
        typeLayer = None
        targetFields = targetLayer.fields()
        if targetLayer.name() == "Ruimten":
            typeLayer = UC.getlayer_byname('ruimten_type')
            tempImportLayer = self.init_layer_fields(targetFields, ["MultiPolygon?crs=epsg:28992", "tempImport", "memory"])
            tempImportLayerInvalid = self.init_layer_fields(targetFields, ["MultiPolygon?crs=epsg:28992", "tempImport_invalid", "memory"])
        else:
            tempImportLayer = self.init_layer_fields(targetFields, ["MultiLinestring?crs=epsg:28992", "tempImport", "memory"])
            tempImportLayerInvalid = self.init_layer_fields(targetFields, ["MultiLinestring?crs=epsg:28992", "tempImport_invalid", "memory"])
        ingangLayer = UC.getlayer_byname('Ingang bouwlaag')
        ingangFields = ingangLayer.fields()
        tempIngangLayer = self.init_layer_fields(ingangFields, ["Point?crs=epsg:28992", "tempImportIngang", "memory"])
        return tempImportLayer, tempImportLayerInvalid, typeLayer, tempIngangLayer, ingangFields

    def get_ingang_type(self):
        typeLayer = UC.getlayer_byname('ingang_type')
        request = QC.QgsFeatureRequest().setFilterExpression('"naam" = ' + "'Deur'")
        ifeature = UC.featureRequest(typeLayer, request)
        return ifeature["id"]

    def construct_features(self, targetFields, targetLayerName, identifier, typeLayer, ingangFields):
        bouwlaagGeomCentroid = self.get_centroid()
        dummy, progressBar = self.progressdialog(0)
        count = 0
        cntFeat = self.importLayer.featureCount()
        invalidCount = 0
        validFeatures = []
        invalidFeatures = []
        ingangFeatures = []
        geomCheck = True
        attributeField = self.type.currentText()
        bouwlaagId = int(self.bouwlaag_id.text())
        ingangTypeId = self.get_ingang_type()
        for feature in self.importLayer.getFeatures():
            targetFeature = QC.QgsFeature()
            targetFeature.initAttributes(targetFields.count())
            targetFeature.setFields(targetFields)
            count += 1
            if self.mappingDict[feature[attributeField]]["deur"] and feature.geometry():
                ingangFeature = self.convert_to_ingang(feature, ingangFields, bouwlaagId, ingangTypeId)
                if ingangFeature:
                    ingangFeatures.append(ingangFeature)
            elif self.mappingDict[feature[attributeField]]["soort"] != 'niet importeren' and feature.geometry():
                if self.importTypeFile == 'DXF':
                    geom, geomCheck = self.check_feature_validity(feature, bouwlaagGeomCentroid)
                elif self.importTypeFile in ('GPKG', 'SHP'):
                    geom = feature.geometry()
                targetFeature.setGeometry(geom)
                targetFeature["bouwlaag_id"] = bouwlaagId
                targetFeature["applicatie"] = 'OIV'
                if targetLayerName == "Ruimten":
                    req = '"naam" = ' + "'" + self.mappingDict[feature[attributeField]]["soort"] + "'"
                    request = QC.QgsFeatureRequest().setFilterExpression(req)
                    tempFeature = UC.featureRequest(typeLayer, request)
                    if tempFeature:
                        targetFeature[identifier] = tempFeature["id"]
                else:
                    targetFeature[identifier] = self.mappingDict[feature[attributeField]]["soort"]
                    if geomCheck:
                        validFeatures.append(targetFeature)
                    else:
                        invalidFeatures.append(targetFeature)
                        invalidCount += 1
            progress = (float(count) / float(cntFeat)) * 100
            progressBar.setValue(progress)
        return validFeatures, invalidFeatures, invalidCount, ingangFeatures

    def convert_to_ingang(self, feature, ingangFields, bouwlaagId, typeId):
        geom = feature.geometry()
        ingangFeature = QC.QgsFeature()
        ingangFeature.initAttributes(ingangFields.count())
        ingangFeature.setFields(ingangFields)
        points = feature.geometry().asPolyline()
        startPt = QC.QgsPoint(points[0])
        endPt = QC.QgsPoint(points[-1])
        angle = startPt.azimuth(endPt)
        length = geom.length()
        featureGeom = geom.interpolate(length / 2.0).asPoint()
        ingangFeature.setGeometry(QC.QgsGeometry().fromPointXY(featureGeom))
        ingangFeature["ingang_type_id"] = typeId
        ingangFeature["bouwlaag_id"] = bouwlaagId
        ingangFeature["applicatie"] = 'OIV'
        ingangFeature["rotatie"] = angle
        return ingangFeature

    def inlezen_validatie(self):
        """import the file after all settings wehere made"""
        targetLayerName = self.import_laag.currentText()
        targetLayer = UC.getlayer_byname(targetLayerName)
        targetFields = targetLayer.fields()
        tempImportLayer, tempImportLayerInvalid, typeLayer, tempIngangLayer, ingangFields = self.init_templayers(targetLayer)
        identifier = CH.get_identifier_bl(targetLayerName)
        validFeatures, invalidFeatures, invalidCount, ingangFeatures = self.construct_features(targetFields, targetLayerName, identifier, typeLayer, ingangFields)
        if validFeatures:
            UC.write_layer(tempImportLayer, validFeatures, False, False)
            QC.QgsProject.instance().addMapLayer(tempImportLayer, True)
        if invalidFeatures:
            UC.write_layer(tempImportLayerInvalid, invalidFeatures, False, False)
            QC.QgsProject.instance().addMapLayer(tempImportLayerInvalid, True)
        if ingangFeatures:
            UC.write_layer(tempIngangLayer, ingangFeatures, False, False)
            QC.QgsProject.instance().addMapLayer(tempIngangLayer, True)
        if invalidCount > 0:
            MSG.showMsgBox('importpartiallysuccesfull', '{}'.format(invalidCount))
        else:
            MSG.showMsgBox('importsuccesfull')
        QC.QgsProject.instance().removeMapLayers([self.importLayer.id()])
        self.label8.setVisible(True)
        self.import_file.setVisible(True)

    def check_feature_validity(self, feature, bouwlaagGeomCentroid):
        lenGeomCheck = True
        if self.importLayer.geometryType() == QC.QgsWkbTypes.PolygonGeometry:
            polygon = feature.geometry().asPolygon()
            geom = QC.QgsGeometry.fromPolygonXY(polygon)
            if len(polygon[0]) < 3:
                lenGeomCheck = False
        elif self.importLayer.wkbType() == QC.QgsWkbTypes.MultiLineString:
            multiLine = feature.geometry().asMultiPolyline()
            geom = QC.QgsGeometry.fromMultiPolylineXY(multiLine)
            for line in multiLine:
                if len(line) < 2:
                    lenGeomCheck = False
        else:
            line = feature.geometry().asPolyline()
            geom = QC.QgsGeometry.fromPolylineXY(line)
            if len(line) < 2:
                lenGeomCheck = False
        if lenGeomCheck:
            distanceToObject = QC.QgsGeometry.distance(bouwlaagGeomCentroid, geom)
            if distanceToObject > 20000000:
                lenGeomCheck = False
            checkGeomValidity = feature.geometry().isGeosValid()
            if not checkGeomValidity:
                lenGeomCheck = False
        return geom, lenGeomCheck

    def run_select_bouwlaag(self):
        """activate the selection tool"""
        try:
            self.selectTool.geomSelected.disconnect()
        except:  # pylint: disable=bare-except
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
        self.validatie_import.setVisible(True)

    def set_parent_id(self, ilayer, ifeature):
        """let user select the floor which to link to"""
        if ilayer.name() == 'Bouwlagen' and ifeature:
            self.bouwlaag_id.setText(str(ifeature["id"]))
            self.selectTool.geomSelected.disconnect(self.set_parent_id)
            self.label3.setVisible(True)
            self.label4.setVisible(True)
            self.label5a.setVisible(True)
            self.label5b.setVisible(True)
            self.import_laag.setVisible(True)
            self.check.setVisible(True)
            self.type.setVisible(True)
        elif ifeature:
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
        self.label8.setVisible(False)
        self.mapping.setVisible(False)
        self.selectId.setVisible(False)
        self.type.setVisible(False)
        self.select_file.setVisible(True)
        self.bestandsnaam.setVisible(True)
        self.import_file.setVisible(False)
        self.validatie_import.setVisible(False)
        self.import_laag.setVisible(False)

    def close_import(self):
        """close feature form and save changes"""
        self.helpBtn.clicked.disconnect()
        self.floatBtn.clicked.disconnect()
        self.hide_all()
        self.close()
        self.parent.bouwlagen_to_combobox(str(self.object_id.text()), int(self.bouwlaag.text()))
        try:
            self.parent.show_subwidget(False)
            del self.parent
        except:  # pylint: disable=bare-except
            pass
        try:
            QC.QgsProject.instance().removeMapLayers([self.importLayer.id()])
        except:  # pylint: disable=bare-except
            pass
        del self


class MappingDialog(PQtW.QDialog):
    """construct the mapping GUI"""

    targetTypes = []
    importTypes = []
    labels = {}
    comboBoxes = {}
    checkBoxes = {}

    def __init__(self, parent=None):
        super(MappingDialog, self).__init__(parent)
        self.setWindowTitle("Maak een mapping t.b.v. het importeren")
        mainLayout = PQtW.QVBoxLayout()
        qlayout = PQtW.QGridLayout()
        widget = PQtW.QWidget()
        scrollArea = PQtW.QScrollArea()
        widget.setLayout(qlayout)
        i = 0
        self.add_headers(qlayout)
        for importType in self.importTypes:
            self.labels[i] = PQtW.QLabel(self)
            self.labels[i].setText(str(importType))
            self.comboBoxes[i] = PQtW.QComboBox(self)
            self.comboBoxes[i].addItems(self.targetTypes)
            self.checkBoxes[i] = PQtW.QCheckBox(self)
            qlayout.addWidget(self.labels[i], i + 1, 0)
            qlayout.addWidget(self.comboBoxes[i], i + 1, 1)
            qlayout.addWidget(self.checkBoxes[i], i + 1, 2)
            i += 1
        buttons = PQtW.QDialogButtonBox(
            PQtW.QDialogButtonBox.Ok | PQtW.QDialogButtonBox.Cancel,
            PQtC.Qt.Horizontal, self)
        buttons.accepted.connect(self.accept)
        buttons.rejected.connect(self.reject)
        qlayout.addWidget(buttons)
        scrollArea.setWidget(widget)
        mainLayout.addWidget(scrollArea)
        self.setLayout(mainLayout)

    def add_headers(self, layout):
        j = 0
        headers = ['import type', 'target type', 'deur']
        for header in headers:
            label = PQtW.QLabel(self)
            label.setText(header)
            layout.addWidget(label, 0, j)
            j += 1

    @staticmethod
    def getMapping(parent=None):
        """initiate the GUI and redirect the input"""
        mapping = {}
        dialog = MappingDialog(parent)
        result = dialog.exec_()
        for i in range(len(dialog.importTypes)):
            mapping.update({dialog.labels[i].text(): {'soort': dialog.comboBoxes[i].currentText(), 'deur': dialog.checkBoxes[i].isChecked()}})
        return (mapping, result == PQtW.QDialog.Accepted)


class DxfDialog(PQtW.QDialog):
    """construct the import GUI"""

    def __init__(self, parent=None):
        super(DxfDialog, self).__init__(parent)
        self.setWindowTitle("Type geometrie")
        max_bouwlaag = 30
        min_bouwlaag = -10
        qlayout = PQtW.QVBoxLayout(self)
        self.label1 = PQtW.QLabel(self)
        self.label1.setText("Welke type geometrie wilt u importeren?")
        qlayout.addWidget(self.label1)
        self.inputGeometry = PQtW.QComboBox(self)
        self.inputGeometry.addItems(['lijn', 'vlak'])
        qlayout.addWidget(self.inputGeometry)
        """
        self.label2 = PQtW.QLabel(self)
        self.label2.setText("Wilt u de polygoon importeren als Bouwlaag?")
        qlayout.addWidget(self.label2)
        self.checkBouwlaag = PQtW.QCheckBox(self)
        qlayout.addWidget(self.checkBouwlaag)
        self.checkBouwlaag.stateChanged.connect(self.addBouwlaagQuestion)
        self.qComboA = PQtW.QComboBox(self)
        for i in range(max_bouwlaag - min_bouwlaag + 1):
            if max_bouwlaag - i != 0:
                self.qComboA.addItem(str(max_bouwlaag - i))
                if max_bouwlaag - i == 1:
                    init_index = i
        self.qComboA.setCurrentIndex(init_index)
        self.qComboA.setFixedWidth(100)
        self.qComboA.setMaxVisibleItems(30)
        self.label3 = PQtW.QLabel(self)
        self.label3.setText("Geef de bouwlaag op waarvoor u de polygoon wilt inlezen.")
        self.qComboA.setVisible(False)
        self.label3.setVisible(False)
        qlayout.addWidget(self.label3)
        qlayout.addWidget(self.qComboA)
        """
        buttons = PQtW.QDialogButtonBox(
            PQtW.QDialogButtonBox.Ok | PQtW.QDialogButtonBox.Cancel,
            PQtC.Qt.Horizontal, self)
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
    def getGeometryType(parent=None):
        """Contains DXF line or polygon geometrie"""
        dialog = DxfDialog(parent)
        result = dialog.exec_()
        return (dialog.inputGeometry.currentText(), result == PQtW.QDialog.Accepted)


class GpkgDialog(PQtW.QDialog):
    """construct the import GUI"""
    layerNames = []

    def __init__(self, parent=None):
        super(GpkgDialog, self).__init__(parent)
        self.setWindowTitle("Kies de laag die u wilt importeren")
        qlayout = PQtW.QVBoxLayout(self)
        self.qComboA = PQtW.QComboBox(self)
        self.qComboA.addItems(self.layerNames)
        self.qComboA.setFixedWidth(300)
        self.qComboA.setMaxVisibleItems(30)
        self.label3 = PQtW.QLabel(self)
        qlayout.addWidget(self.qComboA)
        buttons = PQtW.QDialogButtonBox(
            PQtW.QDialogButtonBox.Ok | PQtW.QDialogButtonBox.Cancel,
            PQtC.Qt.Horizontal, self)
        buttons.accepted.connect(self.accept)
        buttons.rejected.connect(self.reject)
        qlayout.addWidget(buttons)

    @staticmethod
    def getLayerName(parent=None):
        """Contains GeoPackage layername"""
        dialog = GpkgDialog(parent)
        result = dialog.exec_()
        return (dialog.qComboA.currentText(), result == PQtW.QDialog.Accepted)
