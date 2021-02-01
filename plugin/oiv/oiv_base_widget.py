"""init the oiv base widget"""
import os
import qgis.PyQt as PQt #pylint: disable=import-error
import qgis.PyQt.QtWidgets as PQtW #pylint: disable=import-error

FORM_CLASS, _ = PQt.uic.loadUiType(os.path.join(
    os.path.dirname(__file__), 'oiv_base_widget.ui'))

class oivBaseWidget(PQtW.QDockWidget, FORM_CLASS):
    """create dockwidget as base of the oiv plugin"""

    def __init__(self, parent=None):
        """Constructor."""
        super(oivBaseWidget, self).__init__(parent)
        self.setupUi(self)
