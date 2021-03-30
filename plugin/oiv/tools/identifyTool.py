"""multiple classes to identify object on the map"""
import qgis.PyQt.QtCore as PQtC
import qgis.PyQt.QtWidgets as PQtW
import qgis.core as QC
import qgis.gui as QG

import oiv.helpers.utils_core as UC
import oiv.helpers.messages as MSG


class IdentifyGeometryTool(QG.QgsMapToolIdentify, QG.QgsMapTool):
    """identify geometry on the map"""

    def __init__(self, canvas):
        self.canvas = canvas
        QG.QgsMapToolIdentify.__init__(self, canvas)

    geomIdentified = PQtC.pyqtSignal(['QgsVectorLayer', 'QgsFeature'])

    def canvasReleaseEvent(self, mouseEvent):
        """handle mouse release event and return indetified feature"""
        tempfeature = QC.QgsFeature()
        results = self.identify(mouseEvent.x(), mouseEvent.y(), self.TopDownStopAtFirst, self.VectorLayer)
        if not results == []:
            tempfeature = results[0].mFeature
            idlayer = results[0].mLayer
            self.geomIdentified.emit(idlayer, tempfeature)
        else:
            self.geomIdentified.emit(None, tempfeature)


class SelectTool(QG.QgsMapToolIdentify, QG.QgsMapTool):
    """select geometry on the map"""

    whichConfig = ''

    def __init__(self, canvas):
        self.canvas = canvas
        QG.QgsMapToolIdentify.__init__(self, canvas)

    geomSelected = PQtC.pyqtSignal(['QgsVectorLayer', 'QgsFeature'])

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
            MSG.showMsgBox('noidentifiedobject')

    def ask_user_for_feature(self, idLayer, allFeatures):
        """if more features are identified ask user which one to choose"""
        targetFeature = None
        query = "SELECT identifier, type_layer_name FROM {} WHERE child_layer = '{}'".format(self.whichConfig, idLayer.name())
        attrs = UC.read_settings(query, False)
        sortList = []
        for feat in allFeatures:
            if len(attrs) > 1:
                typeValue = feat[attrs[0]]
                if isinstance(typeValue, (int, float)):
                    req = '"id" = {}'.format(typeValue)
                    request = QC.QgsFeatureRequest().setFilterExpression(req)
                    type_layer = UC.getlayer_byname(attrs[1])
                    tempFeature = next(type_layer.getFeatures(request))
                    sortList.append([feat["id"], tempFeature["naam"]])
                else:
                    sortList.append([feat["id"], typeValue])
            elif attrs:
                sortList.append([feat["id"], feat[attrs[0]]])
            else:
                sortList = None
        if sortList:
            AskFeatureDialog.askList = sortList
            chosen, dummy = AskFeatureDialog.askFeature()
        for feat in allFeatures:
            if feat["id"] == int(chosen):
                targetFeature = feat
        return targetFeature


class AskFeatureDialog(PQtW.QDialog):
    """if more features are identified ask user which one to choose"""
    askList = []

    def __init__(self, parent=None):
        super(AskFeatureDialog, self).__init__(parent)
        self.setWindowTitle("Selecteer feature")
        qlayout = PQtW.QVBoxLayout(self)
        self.qlineA = PQtW.QLabel(self)
        self.qlineB = PQtW.QLabel(self)
        self.qComboA = PQtW.QComboBox(self)
        self.qlineA.setText("U heeft meerdere features geselecteerd.")
        self.qlineB.setText("Selecteer in de lijst de feature die u wilt bewerken.")

        self.qComboA.setFixedWidth(100)
        self.qComboA.setMaxVisibleItems(30)
        for item in self.askList:
            self.qComboA.addItem(str(item[1]), str(item[0]))
        qlayout.addWidget(self.qlineA)
        qlayout.addWidget(self.qlineB)
        qlayout.addWidget(self.qComboA)
        buttons = PQtW.QDialogButtonBox(
            PQtW.QDialogButtonBox.Ok | PQtW.QDialogButtonBox.Cancel,
            PQtC.Qt.Horizontal, self)
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
        return (dialog.qComboA.itemData(indexCombo), result == PQtW.QDialog.Accepted)
