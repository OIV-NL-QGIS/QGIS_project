"""create new repressief object"""
import os

import qgis.PyQt as PQt #pylint: disable=import-error
import qgis.PyQt.QtWidgets as PQtW #pylint: disable=import-error
import qgis.core as QC #pylint: disable=import-error
import qgis.utils as QU #pylint: disable=import-error

import oiv.tools.utils_core as UC
import oiv.plugin_helpers.messages as MSG
import oiv.plugin_helpers.qt_helper as QH

FORM_CLASS, _ = PQt.uic.loadUiType(os.path.join(
    os.path.dirname(__file__), 'oiv_objectnieuw_widget.ui'))

class oivObjectNieuwWidget(PQtW.QDockWidget, FORM_CLASS):

    canvas = None
    newObject = None
    drawLayer = None
    basewidget = None
    objectwidget = None
    mapTool = None

    def __init__(self, parent=None):
        """Constructor."""
        super(oivObjectNieuwWidget, self).__init__(parent)
        self.setupUi(self)
        self.iface = QU.iface
        self.opslaan.clicked.connect(self.run_tekenen)
        self.terug.clicked.connect(self.close_objectnieuw_show_base)

    def close_objectnieuw_show_base(self):
        self.close()
        try:
            del self.objectwidget
        except: # pylint: disable=bare-except
            pass
        self.basewidget.show()
        del self

    #place new object (i-tje)
    def run_tekenen(self):
        if self.bron.text() == 'BAG':
            runLayer = "Objecten"
        else:
            runLayer = "Objecten BGT"
        self.drawLayer = UC.getlayer_byname(runLayer)
        self.canvas.setMapTool(self.mapTool)
        self.mapTool.canvasClicked.connect(self.place_feature)

    #construct the feature and save
    def place_feature(self, point):
        childFeature = QC.QgsFeature()
        newFeatureId = None
        self.iface.setActiveLayer(self.drawLayer)
        objectLayer = UC.getlayer_byname('Objecten')
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
        query = "SELECT foreign_key, input_label, question, label_required\
             FROM config_object WHERE child_layer = '{}'".format(self.drawLayer.name())
        attrs = UC.read_settings(query, False)
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
        self.objectwidget.drawLayer = UC.getlayer_byname('Objecten')
        self.objectwidget.object_id.setText(str(objectId))
        self.objectwidget.formelenaam.setText(formeleNaam)
        self.iface.addDockWidget(QH.getWidgetType(), self.objectwidget)
        self.objectwidget.initActions()
        self.objectwidget.show()
        self.iface.actionPan().trigger()
        self.close()
        del self.objectwidget
        del self
