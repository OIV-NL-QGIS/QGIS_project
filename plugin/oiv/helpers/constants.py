import os
import json
import qgis.core as QC #pylint: disable=import-error
from ..helpers.utils_core import getlayer_byname

def plugin_settings(key1, key2=None):
    filename = os.path.join(os.path.dirname(__file__), '../config_files/plugin_settings.json')
    with open(filename, 'r') as f:
        data = json.load(f)
    if key2:
        return data[key1][key2]
    return data[key1]

def write_plugin_settings(key1, newData):
    filename = os.path.join(os.path.dirname(__file__), '../config_files/plugin_settings.json')
    with open(filename, 'r') as f:
        data = json.load(f)
    with open(filename, 'w') as f:
        data[key1] = newData
        json.dump(data, f)

def bagpand_layername():
    baglayerName = PAND["bagpandlayername"] + plugin_settings("BAGCONNECTION")["active"]
    layer = getlayer_byname(baglayerName)
    if layer:
        bagNode = QC.QgsProject.instance().layerTreeRoot().findLayer(layer.id())
        if bagNode.isVisible():
            return baglayerName
        return PAND["bagpandlayername"] + plugin_settings("BAGCONNECTION")["inactive"]
    return None

OIV_VERSION = '3.3.0'

PLUGIN = {
        "name": "OIV Objecten",
        "toolbartext": "OIV " + OIV_VERSION + " | Actieve bouwlaag: ",
        "compatibleDbVersion" : {
            "min" : 324,
            "max" : 330
        },
        "menulocation": "&OIV Objecten",
        "settingsname": "Configure",
        "settingsicon": ":/plugins/oiv/config_files/png/settings.png",
        "menusettingslocation": "&OIV Objecten",
        "basewidget" : "oiv_base_widget.ui",
        "icon": ":/plugins/oiv/config_files/png/oiv_plugin.png",
        "floaticon" : ":/plugins/oiv/config_files/png/maximize.png",
        "helpicon" : ":/plugins/oiv/config_files/png/help.png",
    }

PAND = {
    "bagpandlayername": "BAG panden - ",
    "bouwlaaglayername": "Bouwlagen",
    "bouwlagen": {
        "min" : -10,
        "max" : 30
    },
    "configtable": "config_bouwlaag",
    "tekenwidgetui": "oiv_tekenen_widget.ui",
    "bouwlaagui": "oiv_bouwlaag_widget.ui",
    "pandui": "oiv_pandgegevens_widget.ui",
    "bagviewerurl": "https://bagviewer.kadaster.nl/lvbag/bag-viewer/#?searchQuery="
}

OBJECT = {
    "objectlayername": "Objecten",
    "terreinlayername": "Object terrein",
    "objectbgtlayername": "Objecten BGT",
    "gridlayername": "Grid",
    "configtable": "config_object",
    "gridwidgetui": "oiv_create_grid_widget.ui",
    "objectnieuwwidgetui": "oiv_objectnieuw_widget.ui",
    "tekenwidgetui": "oiv_object_tekenen_widget.ui",
    "objectwidgetui": "oiv_repressief_object_widget.ui",
    "bgtviewerurl": "https://verbeterdekaart.kadaster.nl/#?"
}

HELPURL = {
    "basewidgethelp": "https://github.com/OIV-NL-QGIS/OIV_project/wiki",
    "objectnieuwhelp": "https://github.com/OIV-NL-QGIS/OIV_project/wiki",
    "repressiefobjecthelp" : "https://github.com/OIV-NL-QGIS/OIV_project/wiki",
    "objecttekenenhelp" : "https://github.com/OIV-NL-QGIS/OIV_project/wiki",
    "objectgridhelp" : "https://github.com/OIV-NL-QGIS/OIV_project/wiki",
    "objectimporthelp" : "https://github.com/OIV-NL-QGIS/OIV_project/wiki",
    "pandhelp": "https://github.com/OIV-NL-QGIS/OIV_project/wiki",
    "bouwlaaghelp" : "https://github.com/OIV-NL-QGIS/OIV_project/wiki",
    "bouwlaagtekenenhelp" : "https://github.com/OIV-NL-QGIS/OIV_project/wiki",
    "bouwlaagimporthelp" : "https://github.com/OIV-NL-QGIS/OIV_project/wiki"
}