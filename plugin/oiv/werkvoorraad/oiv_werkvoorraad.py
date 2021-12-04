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
    os.path.dirname(__file__), "oiv_werkvoorraad_widget.ui"))


class oivWerkvoorraadWidget(PQtW.QDockWidget, FORM_CLASS):

    drawLayer = None

    def __init__(self, parent=None, objectId=None, bron=None, bronTbl=None):
        """Constructor."""
        super(oivWerkvoorraadWidget, self).__init__(parent)
        self.setupUi(self)
        self.parent = parent
        self.iface = parent.iface
        self.canvas = parent.canvas
        self.formelenaam.setText(parent.formelenaam.text())
        self.object_id.setText(parent.object_id.text())
        self.initUI()

    def initUI(self):
        #self.btn_opslaan.clicked.connect(self.run_tekenen)
        self.btn_terug.clicked.connect(self.close_werkvoorraad)
        self.helpBtn, self.floatBtn, titleBar = QT.getTitleBar()
        self.setTitleBarWidget(titleBar)
        self.helpBtn.clicked.connect(lambda: UC.open_url(PC.HELPURL["objectnieuwhelp"]))
        self.floatBtn.clicked.connect(lambda: self.setFloating(True))
        self.fr_verwerk.setVisible(False)

    def close_werkvoorraad(self):
        self.btn_opslaan.clicked.disconnect()
        self.btn_terug.clicked.disconnect()
        self.helpBtn.clicked.disconnect()
        self.floatBtn.clicked.disconnect()
        self.close()
        self.parent.show()
        del self

