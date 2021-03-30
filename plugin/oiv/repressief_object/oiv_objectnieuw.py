"""create new repressief object"""
import os

from qgis.PyQt import uic
import qgis.PyQt.QtWidgets as PQtW
import qgis.core as QC

import oiv.helpers.utils_core as UC
import oiv.helpers.qt_helper as QT
import oiv.helpers.messages as MSG
import oiv.helpers.configdb_helper as CH
import oiv.helpers.constants as PC

FORM_CLASS, _ = uic.loadUiType(os.path.join(
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

    def run_tekenen(self):
        '''place new object (i-tje)'''
        if self.bron.text() == 'BAG':
            runLayer = PC.OBJECT["objectlayername"]
        else:
            runLayer = PC.OBJECT["objectbgtlayername"]
        self.drawLayer = UC.getlayer_byname(runLayer)
        self.canvas.setMapTool(self.parent.pinTool)
        self.parent.pinTool.canvasClicked.connect(self.place_feature)

    # construct the feature and save
    def place_feature(self, point):
        childFeature = QC.QgsFeature()
        objectLayer = UC.getlayer_byname(PC.OBJECT["objectlayername"])
        # set geometry from the point clicked on the canvas
        childFeature.setGeometry(QC.QgsGeometry.fromPointXY(point))
        foreignKey = self.identificatienummer.text()
        buttonCheck, formeleNaam = self.get_attributes(foreignKey, childFeature)
        # return of new created feature id
        if buttonCheck != 'Cancel':
            UC.write_layer(self.drawLayer, childFeature)
            objectLayer.reload()
            self.close_objectnieuw_show_base()
        else:
            self.iface.actionPan().trigger()
        try:
            self.parent.pinTool.canvasClicked.disconnect()
        except:
            pass

    def get_attributes(self, foreignKey, childFeature):
        '''get the right attributes from user'''
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
            return 'Cancel', None

    def run_objectgegevens(self, formeleNaam, objectId):
        """continue to existing object woth the newly created feature and already searched address"""
        self.parent.run_object(formeleNaam, objectId)
        self.iface.actionPan().trigger()
        self.close()
        del self
