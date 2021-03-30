# -*- coding: utf-8 -*-
"""configure settings of plugin"""
import os

from qgis.PyQt import uic
import qgis.PyQt.QtWidgets as PQtW
import qgis.core as QC

from .helpers.constants import plugin_settings, write_plugin_settings, bagpand_layername
from .helpers.utils_core import getlayer_byname

FORM_CLASS, _ = uic.loadUiType(os.path.join(
    os.path.dirname(__file__), 'oiv_config_widget.ui'))


class oivConfigWidget(PQtW.QDockWidget, FORM_CLASS):

    data = None
    filename = None

    def __init__(self, parent=None):
        super(oivConfigWidget, self).__init__(parent)
        self.setupUi(self)
        self.parent = parent
        self.iface = parent.iface
        self.read_settings()
        self.save.clicked.connect(lambda dummy=None, saveConfig=True: self.close_config(dummy, saveConfig))
        self.cancel.clicked.connect(lambda dummy=None, saveConfig=False: self.close_config(dummy, saveConfig))

    def read_settings(self):
        self.data = plugin_settings("BAGCONNECTION")
        if self.data["active"] == 'PDOK':
            self.bagwfs.setChecked(True)
        else:
            self.bagdatabase.setChecked(True)

    def check_bag_layer_setting(self):
        if self.bagwfs.isChecked():
            QC.QgsExpressionContextUtils.setGlobalVariable('OIV_bag_connection', 'PDOK')
            return "PDOK"
        QC.QgsExpressionContextUtils.setGlobalVariable('OIV_bag_connection', 'Database')
        return "Database"

    def set_bag_layer(self, visibility):
        layerName = bagpand_layername()
        layer = getlayer_byname(layerName)
        ltv = self.iface.layerTreeView()
        ltv.setLayerVisible(layer, visibility)

    def close_config(self, _dummy, saveConfig):
        if saveConfig:
            self.set_bag_layer(False)
            bagConSetting = self.check_bag_layer_setting()
            QC.QgsExpressionContextUtils.setGlobalVariable('OIV_bag_connection', bagConSetting)
            oldBagSetting = self.data["active"]
            if oldBagSetting != bagConSetting:
                self.data["active"] = bagConSetting
                self.data["inactive"] = oldBagSetting
            write_plugin_settings("BAGCONNECTION", self.data)
            self.set_bag_layer(True)
        else:
            print("changes canceled")
        self.close()
        del self
