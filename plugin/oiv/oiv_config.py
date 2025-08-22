# -*- coding: utf-8 -*-
"""configure settings of plugin"""
import os
import shutil

from qgis.PyQt import uic
import qgis.PyQt.QtWidgets as PQtW
import qgis.core as QC

from .helpers.constants import plugin_settings, write_plugin_settings, PAND
from .helpers.utils_core import getlayer_byname

FORM_CLASS, _ = uic.loadUiType(os.path.join(
    os.path.dirname(__file__), 'oiv_config_widget.ui'))


class oivConfigWidget(PQtW.QDockWidget, FORM_CLASS):

    dataBag = None
    dataConn = None
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
        self.dataBag = plugin_settings("BAGCONNECTION")
        if self.dataBag["active"] == 'PDOK':
            self.bagwfs.setChecked(True)
        else:
            self.bagdatabase.setChecked(True)
        self.dataConn = plugin_settings("DBCONNECTION")
        if self.dataConn["active"] == 'prod':
            self.dbprod.setChecked(True)
        else:
            self.dbtest.setChecked(True)
        self.bkgrLayer = plugin_settings("BACKGROUNDLAYER")
        if self.bkgrLayer == 'Openbasiskaart':
            self.openbasiskaart.setChecked(True)
        elif self.bkgrLayer == 'Openstreetmap':
            self.openstreetmap.setChecked(True)
        else:
            self.brt.setChecked(True)

    def check_bag_layer_setting(self):
        if self.bagwfs.isChecked():
            QC.QgsExpressionContextUtils.setGlobalVariable('OIV_bag_connection', 'PDOK')
            return "PDOK"
        QC.QgsExpressionContextUtils.setGlobalVariable('OIV_bag_connection', 'Database')
        return "Database"

    def set_background_layer(self, visibility):
        layer = getlayer_byname(self.bkgrLayer)
        ltv = self.iface.layerTreeView()
        ltv.setLayerVisible(layer, visibility)

    def set_bag_layer(self, bagConSetting, visibility):
        baglayerName = PAND["bagpandlayername"] + bagConSetting
        layer = getlayer_byname(baglayerName)
        ltv = self.iface.layerTreeView()
        ltv.setLayerVisible(layer, visibility)

    def get_checked_background_layer(self):
        if self.openbasiskaart.isChecked():
            self.bkgrLayer = 'Openbasiskaart'
        elif self.openstreetmap.isChecked():
            self.bkgrLayer = 'Openstreetmap'
        else:
            self.bkgrLayer = 'BRT'

    def set_db_connection(self):
        if self.dbprod.isChecked():
            self.dataConn["active"] = 'prod'
            self.dataConn["inactive"] = 'test'
        else:
            self.dataConn["active"] = 'test'
            self.dataConn["inactive"] = 'prod'
        write_plugin_settings("DBCONNECTION", self.dataConn)
        #path = QC.QgsProject.instance().readPath("./")
        path = "C:/programdata/oiv"
        pgServiceFile = path + '/' + self.dataConn["filename"]
        os.remove(pgServiceFile)
        activeFileName = path + '/' + self.dataConn["filename"].split('.')[0] + '_' + self.dataConn["active"] + '.' + self.dataConn["filename"].split('.')[1]
        shutil.copy(activeFileName, pgServiceFile)

    def close_config(self, _dummy, saveConfig):
        if saveConfig:
            self.set_db_connection()
            self.set_background_layer(False)
            bagConSetting = self.check_bag_layer_setting()
            QC.QgsExpressionContextUtils.setGlobalVariable('OIV_bag_connection', bagConSetting)
            oldBagSetting = self.dataBag["active"]
            if oldBagSetting != bagConSetting:
                self.dataBag["active"] = bagConSetting
                self.dataBag["inactive"] = oldBagSetting
            write_plugin_settings("BAGCONNECTION", self.dataBag)
            self.get_checked_background_layer()
            QC.QgsExpressionContextUtils.setGlobalVariable('OIV_backgroundlayer', self.bkgrLayer)
            write_plugin_settings("BACKGROUNDLAYER", self.bkgrLayer) 
            self.set_bag_layer(bagConSetting, True)
            self.set_background_layer(True)
        else:
            print("changes canceled")
        self.close()
        del self
