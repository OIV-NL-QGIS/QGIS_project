"""StackWidget for feature info and feature editing"""
import os

from qgis.PyQt import uic
import qgis.PyQt.QtWidgets as PQtW
import qgis.core as QC
import qgis.gui as QG
import qgis.utils as QU

import oiv.helpers.constants as PC
import oiv.helpers.qt_helper as QH
import oiv.helpers.utils_core as UC

FORM_CLASS, _ = uic.loadUiType(os.path.join(
    os.path.dirname(__file__), 'stackwidget.ui'))


class oivStackWidget(PQtW.QDockWidget, FORM_CLASS):
    """open any feature form as stackwidget in OOIV pluging"""
    attributeForm = None
    parentWidget = None
    parentWidth = None

    def __init__(self, parent=None):
        """Constructor."""
        super(oivStackWidget, self).__init__(parent)
        self.iface = QU.iface
        self.setupUi(self)

    def open_feature_form(self, ilayer, ifeature):
        """"open feature form based on clicked object on the canvas"""
        ilayer.startEditing()
        context = QG.QgsAttributeEditorContext()
        context.setVectorLayerTools(self.iface.vectorLayerTools())
        self.attributeForm = QG.QgsAttributeForm(ilayer, ifeature, context)
        self.stackedWidget.addWidget(self.attributeForm)
        self.stackedWidget.setCurrentWidget(self.attributeForm)
        self.iface.setActiveLayer(ilayer)
        self.terug.clicked.connect(lambda: self.close_stacked(ilayer, ifeature))

    def close_stacked(self, ilayer, ifeature):
        """close feature form and save changes"""
        objectFeature = None
        self.attributeForm.save()
        self.terug.clicked.disconnect()
        ilayer.commitChanges()
        self.attributeForm.close()
        del self.attributeForm
        self.attributeForm = None
        if ilayer.name() == PC.OBJECT["objectlayername"]:
            request = QC.QgsFeatureRequest().setFilterExpression("id = " + str(ifeature["id"]))
            ifeature = UC.featureRequest(ilayer, request)
            if ifeature:
                self.parentWidget.formelenaam.setText(ifeature["formelenaam"])
        self.parentWidget.show()
        self.parentWidget.setFixedWidth(self.parentWidth)
        self.iface.actionPan().trigger()
        self.close()
        del self
