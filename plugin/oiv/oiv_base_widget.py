"""init the oiv base widget"""

import os
from qgis.PyQt import uic
from qgis.PyQt.QtWidgets import QDockWidget

FORM_CLASS, _ = uic.loadUiType(os.path.join(
    os.path.dirname(__file__), 'oiv_base_widget.ui'))

class oivBaseWidget(QDockWidget, FORM_CLASS):
    """create dockwidget as base of the oiv plugin"""

    def __init__(self, parent=None):
        """Constructor."""
        super(oivBaseWidget, self).__init__(parent)
        self.setupUi(self)
