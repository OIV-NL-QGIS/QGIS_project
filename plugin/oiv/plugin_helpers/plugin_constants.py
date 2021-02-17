import os
import json

def read_plugin_settings():
    filename = os.path.join(os.path.dirname(__file__), '../config_files/plugin_settings.json')
    with open(filename, 'r') as f:
        data = json.load(f)
    return data

def write_plugin_settings(data):
    filename = os.path.join(os.path.dirname(__file__), '../config_files/plugin_settings.json')
    with open(filename, 'w') as outfile:
        json.dump(data, outfile)

def bagpand_layername():
    return PAND["bagpandlayername"] + read_plugin_settings()["BAGCONNECTION"]

OIV_VERSION = '3.2.9'

PLUGIN = {
    "name": "OIV Objecten",
    "icon": ":/plugins/oiv/config_files/png/oiv_plugin.png",
    "toolbartext": "OIV " + OIV_VERSION + " | Actieve bouwlaag: ",
    "compatibleDbVersion" : [324, 329],
    "menulocation": "&OIV Objecten",
    "settingsname": "Configure",
    "settingsicon": ":/plugins/oiv/config_files/png/settings.png",
    "menusettingslocation": "&OIV Objecten"
}

PAND = {
    "bagpandlayername": "BAG panden - ",
    "bouwlaaglayername": "Bouwlagen",
    "minbouwlaag": -10,
    "maxbouwlaag": 30,
    "configtable": "config_bouwlaag",
    "tekenwidgetui": "oiv_tekenen_widget.ui",
    "bouwlaagui": "oiv_bouwlaag_widget.ui",
    "pandui": "oiv_pandgegevens_widget.ui",
    "bagviewerurl": "https://bagviewer.kadaster.nl/lvbag/bag-viewer/#?searchQuery=",
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
    "bgtviewerurl": "https://verbeterdekaart.kadaster.nl/#?",
}
