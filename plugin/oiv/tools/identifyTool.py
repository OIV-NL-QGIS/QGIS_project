"""multiple classes to identify object on the map"""

from qgis.PyQt.QtCore import pyqtSignal, Qt
from qgis.PyQt.QtWidgets import QDialog, QVBoxLayout, QLabel, QDialogButtonBox, QComboBox, QMessageBox

from qgis.gui import QgsMapToolIdentify, QgsMapTool
from qgis.core import QgsFeatureRequest, QgsFeature

from .utils_core import getlayer_byname, read_settings

class IdentifyGeometryTool(QgsMapToolIdentify, QgsMapTool):
    """identify geometry on the map"""

    def __init__(self, canvas):
        self.canvas = canvas
        QgsMapToolIdentify.__init__(self, canvas)

    geomIdentified = pyqtSignal(['QgsVectorLayer', 'QgsFeature'])

    def canvasReleaseEvent(self, mouseEvent):
        """handle mouse release event and return indetified feature"""
        tempfeature = QgsFeature()
        results = self.identify(mouseEvent.x(), mouseEvent.y(), self.TopDownStopAtFirst, self.VectorLayer)
        if not results == []:
            tempfeature = results[0].mFeature
            idlayer = results[0].mLayer
            self.geomIdentified.emit(idlayer, tempfeature)
        else:
            self.geomIdentified.emit(None, tempfeature)

class SelectTool(QgsMapToolIdentify, QgsMapTool):
    """select geometry on the map"""

    whichConfig = ''

    def __init__(self, canvas):
        self.canvas = canvas
        QgsMapToolIdentify.__init__(self, canvas)

    geomSelected = pyqtSignal(['QgsVectorLayer', 'QgsFeature'])

    def canvasReleaseEvent(self, mouseEvent):
        """handle mouse release event and return indetified feature"""
        results = self.identify(mouseEvent.x(), mouseEvent.y(), self.TopDownStopAtFirst, self.VectorLayer)
        if not results == []:
            idlayer = results[0].mLayer
            allFeatures = []
            if len(results) > 1:
                for result in results:
                    allFeatures.append(result.mFeature)
                tempfeature = self.ask_user_for_feature(idlayer, allFeatures)
            else:
                tempfeature = results[0].mFeature
            self.geomSelected.emit(idlayer, tempfeature)
        else:
            QMessageBox.information(None, 'Geen tekenlaag!',
                                    "U heeft geen feature op een tekenlaag aangeklikt!\n\nKlik a.u.b. op de juiste locatie."\
                                    , QMessageBox.Ok)

    def ask_user_for_feature(self, idLayer, allFeatures):
        """if more features are identified ask user which one to choose"""
        targetFeature = None
        query = "SELECT identifier, type_layer_name FROM {} WHERE child_layer = '{}'".format(self.whichConfig, idLayer.name())
        attrs = read_settings(query, False)[0]
        sortList = []
        for feat in allFeatures:
            if attrs[1] != '':
                request = QgsFeatureRequest().setFilterExpression('"id" = ' + str(feat[attrs[0]]))
                type_layer = getlayer_byname(attrs[1])
                tempFeature = next(type_layer.getFeatures(request))
                sortList.append([feat["id"], tempFeature["naam"]])
            else:
                sortList.append([feat["id"], feat[attrs[0]]])
        AskFeatureDialog.askList = sortList
        chosen, dummy = AskFeatureDialog.askFeature()
        for feat in allFeatures:
            if feat["id"] == int(chosen):
                targetFeature = feat
        return targetFeature

class AskFeatureDialog(QDialog):
    """if more features are identified ask user which one to choose"""
    askList = []

    def __init__(self, parent = None):
        super(AskFeatureDialog, self).__init__(parent)
        self.setWindowTitle("Selecteer feature")
        qlayout = QVBoxLayout(self)
        self.qlineA = QLabel(self)
        self.qlineB = QLabel(self)
        self.qComboA = QComboBox(self)
        self.qlineA.setText("U heeft meerdere features geselecteerd.")
        self.qlineB.setText("Selecteer in de lijst de feature die u wilt bewerken.")

        self.qComboA.setFixedWidth(100)
        self.qComboA.setMaxVisibleItems(30)
        for item in self.askList:
            self.qComboA.addItem(str(item[1]), str(self.item[0]))
        qlayout.addWidget(self.qlineA)
        qlayout.addWidget(self.qlineB)
        qlayout.addWidget(self.qComboA)
        buttons = QDialogButtonBox(
            QDialogButtonBox.Ok | QDialogButtonBox.Cancel,
            Qt.Horizontal, self)
        buttons.accepted.connect(self.accept)
        buttons.rejected.connect(self.reject)
        qlayout.addWidget(buttons)

    # static method to create the dialog and return (date, time, accepted)
    @staticmethod
    def askFeature(parent=None):
        """if more features are identified ask user which one to choose"""
        dialog = AskFeatureDialog(parent)
        result = dialog.exec_()
        indexCombo = dialog.qComboA.currentIndex()
        return (dialog.qComboA.itemData(indexCombo), result == QDialog.Accepted)         
