"""StackWidget for feature info and feature editing"""
import os

import qgis.PyQt as PQt #pylint: disable=import-error
import qgis.PyQt.QtWidgets as PQtW #pylint: disable=import-error
import qgis.core as QC #pylint: disable=import-error
import qgis.gui as QG #pylint: disable=import-error
import qgis.utils as QU #pylint: disable=import-error

import oiv.helpers.constants as PC

FORM_CLASS, _ = PQt.uic.loadUiType(os.path.join(
    os.path.dirname(__file__), 'stackwidget.ui'))

class oivStackWidget(PQtW.QDockWidget, FORM_CLASS):
    """open any feature form as stackwidget in OOIV pluging"""
    attributeForm = None
    parentWidget = None

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
        self.attributeForm.save()
        self.terug.clicked.disconnect()
        ilayer.commitChanges()
        self.attributeForm.close()
        del self.attributeForm
        self.attributeForm = None
        if ilayer.name() == PC.OBJECT["objectlayername"]:
            request = QC.QgsFeatureRequest().setFilterExpression("id = " \
                             + str(ifeature["id"]))
            objectFeature = next(ilayer.getFeatures(request))
            self.parentWidget.formelenaam.setText(objectFeature["formelenaam"])
        self.close()
        try:
            self.parentWidget.show()
            self.iface.actionPan().trigger()
        except: # pylint: disable=bare-except
            pass
        del self
