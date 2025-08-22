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
    isTekenen = False

    def __init__(self, parent=None):
        """Constructor."""
        super(oivStackWidget, self).__init__(parent)
        self.iface = QU.iface
        self.parent = parent
        self.baseWidget = self.parent.baseWidget
        self.baseWidget.done.setVisible(False)
        self.baseWidget.done_png.setVisible(False)
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
        self.attributeForm.save()
        ilayer.commitChanges()
        self.attributeForm.close()
        del self.attributeForm
        self.attributeForm = None
        if ilayer.name() == PC.OBJECT["objectlayername"]:
            request = QC.QgsFeatureRequest().setFilterExpression("id = " + str(ifeature["id"]))
            ifeature = UC.featureRequest(ilayer, request)
            if ifeature:
                self.parent.formelenaam.setText(ifeature["formelenaam"])
        if not self.isTekenen:
            self.baseWidget.done.setVisible(True)
            self.baseWidget.done_png.setVisible(True)
        else:
            self.parent.run_edit_tool()
        self.terug.clicked.disconnect()
        self.close()
        self.parent.show_subwidget(False)
        del self
