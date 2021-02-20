"""create new repressief object"""
import os

import qgis.PyQt as PQt #pylint: disable=import-error
import qgis.PyQt.QtWidgets as PQtW #pylint: disable=import-error
import qgis.core as QC #pylint: disable=import-error

import oiv.helpers.utils_core as UC
import oiv.helpers.qt_helper as QT
import oiv.helpers.messages as MSG
import oiv.helpers.configdb_helper as CH
import oiv.helpers.constants as PC
import oiv.repressief_object.oiv_repressief_object as ORO

FORM_CLASS, _ = PQt.uic.loadUiType(os.path.join(
    os.path.dirname(__file__), PC.OBJECT["objectnieuwwidgetui"]))

class oivObjectNieuwWidget(PQtW.QDockWidget, FORM_CLASS):

    drawLayer = None

    def __init__(self, parent=None, objectId=None, bron=None, bronTbl=None):
        """Constructor."""
        super(oivObjectNieuwWidget, self).__init__(parent)
        self.setupUi(self)
        self.parent = parent
        self.iface = parent.iface
        self.canvas = parent.canvas
        self.identificatienummer.setText(str(objectId))
        self.bron.setText(str(bron))
        self.bron_table.setText(str(bronTbl))
        self.initUI()

    def initUI(self):
        self.opslaan.clicked.connect(self.run_tekenen)
        self.terug.clicked.connect(self.close_objectnieuw_show_base)
        self.helpBtn, self.floatBtn, titleBar = QT.getTitleBar()
        self.setTitleBarWidget(titleBar)
        self.helpBtn.clicked.connect(lambda: UC.open_url(PC.HELPURL["objectnieuwhelp"]))
        self.floatBtn.clicked.connect(lambda: self.setFloating(True))

    def close_objectnieuw_show_base(self):
        self.opslaan.clicked.disconnect()
        self.terug.clicked.disconnect()
        self.helpBtn.clicked.disconnect()
        self.floatBtn.clicked.disconnect()
        self.close()
        self.parent.show()
        del self

    #place new object (i-tje)
    def run_tekenen(self):
        if self.bron.text() == 'BAG':
            runLayer = PC.OBJECT["objectlayername"]
        else:
            runLayer = PC.OBJECT["objectbgtlayername"]
        self.drawLayer = UC.getlayer_byname(runLayer)
        self.canvas.setMapTool(self.parent.pinTool)
        self.parent.pinTool.canvasClicked.connect(self.place_feature)

    #construct the feature and save
    def place_feature(self, point):
        childFeature = QC.QgsFeature()
        newFeatureId = None
        objectLayer = UC.getlayer_byname(PC.OBJECT["objectlayername"])
        #set geometry from the point clicked on the canvas
        childFeature.setGeometry(QC.QgsGeometry.fromPointXY(point))
        foreignKey = self.identificatienummer.text()
        buttonCheck, formeleNaam = self.get_attributes(foreignKey, childFeature)
        #return of new created feature id
        if buttonCheck != 'Cancel':
            newFeatureId = UC.write_layer(self.drawLayer, childFeature)
            objectLayer.reload()
            if not newFeatureId:
                idx = objectLayer.fields().indexFromName('id')
                maxObjectId = objectLayer.maximumValue(idx)
                request = QC.QgsFeatureRequest().setFilterExpression('"id" > {}'.format(maxObjectId))
                self.drawLayer.reload()
                tempFeatureIt = objectLayer.getFeatures(request)
                for feat in tempFeatureIt:
                    if feat["formelenaam"] == formeleNaam:
                        newFeatureId = feat["id"]
            #with new created feature run existing object widget
            if newFeatureId:
                self.run_objectgegevens(formeleNaam, newFeatureId)
            else:
                MSG.showMsgBox('newobjectslowanswer')
        else:
            self.iface.actionPan().trigger()

    #get the right attributes from user
    def get_attributes(self, foreignKey, childFeature):
        attrs = CH.get_allkeys_ob(self.drawLayer.name())
        labelTekst = UC.user_input_label(attrs[3], attrs[2])
        if labelTekst != 'Cancel':
            fields = self.drawLayer.fields()
            childFeature.initAttributes(fields.count())
            childFeature.setFields(fields)
            if attrs[1] != '':
                childFeature[attrs[1]] = labelTekst
            if attrs[0] != '':
                childFeature[attrs[0]] = foreignKey
            childFeature["bron"] = self.bron.text()
            childFeature["bron_tabel"] = self.bron_table.text()
            return childFeature, labelTekst
        else:
            return 'Cancel'

    def run_objectgegevens(self, formeleNaam, objectId):
        """continue to existing object woth the newly created feature and already searched address"""
        self.parent.run_object(formeleNaam, objectId)
        self.iface.actionPan().trigger()
        self.close()
        del self
