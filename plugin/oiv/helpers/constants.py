import os
import json
import qgis.core as QC  # pylint: disable=import-error
from ..helpers.utils_core import getlayer_byname


def plugin_settings(key1, key2=None):
    filename = os.path.join(os.path.dirname(__file__), PLUGIN["configdbpath"])
    with open(filename, 'r') as f:
        data = json.load(f)
    if key2:
        return data[key1][key2]
    return data[key1]


def write_plugin_settings(key1, newData):
    filename = os.path.join(os.path.dirname(__file__), PLUGIN["configdbpath"])
    with open(filename, 'r') as f:
        data = json.load(f)
    with open(filename, 'w') as f:
        data[key1] = newData
        json.dump(data, f)


def bagpand_layername():
    baglayerName = PAND["bagpandlayername"] + plugin_settings("BAGCONNECTION")["active"]
    layer = getlayer_byname(baglayerName)
    if layer:
        ltr = QC.QgsProject.instance().layerTreeRoot()
        bagNode = ltr.findLayer(layer.id())
        if bagNode.isVisible():
            return baglayerName
        else:
            return PAND["bagpandlayername"] +\
                plugin_settings("BAGCONNECTION")["inactive"]
    return None


OIV_VERSION = '3.6.9'

PLUGIN = {
    "name": "OIV Objecten",
    "toolbartext": "OIV " + OIV_VERSION + " | Actieve bouwlaag: ",
    "compatibleDbVersion": {
        "min": 368,
        "max": 369
    },
    "menulocation": "&OIV Objecten",
    "settingsname": "Configure",
    "settingsicon": ":/plugins/oiv/config_files/png/settings.png",
    "menusettingslocation": "&OIV Objecten",
    "basewidget": "oiv_base_widget.ui",
    "icon": ":/plugins/oiv/config_files/png/oiv_plugin.png",
    "floaticon": ":/plugins/oiv/config_files/png/maximize.png",
    "helpicon": ":/plugins/oiv/config_files/png/help.png",
    "configdbpath": "../config_files/plugin_settings.json"
}

PAND = {
    "bagpandlayername": "BAG panden - ",
    "bouwlaaglayername": "Bouwlagen",
    "bouwlagen": {
        "min": -10,
        "max": 30
    },
    "configtable": "config_bouwlaag",
    "tekenwidgetui": "oiv_tekenen_widget.ui",
    "bouwlaagui": "oiv_bouwlaag_widget.ui",
    "pandui": "oiv_pandgegevens_widget.ui",
    "bagviewerurl": "https://bagviewer.kadaster.nl/lvbag/bag-viewer/#?searchQuery=",
    "werkvoorraadlayers": [
        "Werkvoorraad bouwlaag - punt",
        "Werkvoorraad bouwlaag - label",
        "Werkvoorraad bouwlaag - lijn",
        "Werkvoorraad bouwlaag - vlak"],
}

WERKVOORRAAD = {
    "tablelayertranslate": {
        "Werkvoorraad bouwlaag - punt": "werkvoorraad_punt",
        "Werkvoorraad bouwlaag - label": "werkvoorraad_label",
        "Werkvoorraad bouwlaag - lijn": "werkvoorraad_lijn",
        "Werkvoorraad bouwlaag - vlak": "werkvoorraad_vlak",
        "Werkvoorraad object - punt": "werkvoorraad_punt",
        "Werkvoorraad object - label": "werkvoorraad_label",
        "Werkvoorraad object - lijn": "werkvoorraad_lijn",
        "Werkvoorraad object - vlak": "werkvoorraad_vlak"
    }    
}

OBJECT = {
    "objectlayername": "Objecten",
    "terreinlayername": "Object terrein",
    "objectbgtlayername": "Objecten BGT",
    "objectwerkvoorraadlayername": "Werkvoorraad objecten",
    "gridlayername": "Grid",
    "configtable": "config_object",
    "gridwidgetui": "oiv_create_grid_widget.ui",
    "objectnieuwwidgetui": "oiv_objectnieuw_widget.ui",
    "tekenwidgetui": "oiv_object_tekenen_widget.ui",
    "objectwidgetui": "oiv_repressief_object_widget.ui",
    "bgtviewerurl": "https://verbeterdekaart.kadaster.nl/#?",
    "werkvoorraadlayers": [
            'Werkvoorraad object - punt', 
            'Werkvoorraad object - label', 
            'Werkvoorraad object - lijn', 
            'Werkvoorraad object - vlak'],
    "nogeotables": ["aanwezig", "historie", "gebruiksfunctie", "bedrijfshulpverlening", "contactpersoon", "scenario", "veilighv_org"],
    "objecttypes": ["objecten", "waterongeval", "evenement", "natuur", "recreatiegebied"],
}

INFO_INTEREST = {
    "configtable": "config_info_of_interest",
    "tekenwidgetui": "oiv_info_of_interest_tekenen_widget.ui"
}

HELPURL = {
    "basewidgethelp": "https://github.com/OIV-NL-QGIS/OIV_project/wiki",
    "objectnieuwhelp": "https://github.com/OIV-NL-QGIS/OIV_project/wiki",
    "repressiefobjecthelp": "https://github.com/OIV-NL-QGIS/OIV_project/wiki",
    "objecttekenenhelp": "https://github.com/OIV-NL-QGIS/OIV_project/wiki",
    "objectgridhelp": "https://github.com/OIV-NL-QGIS/OIV_project/wiki",
    "objectimporthelp": "https://github.com/OIV-NL-QGIS/OIV_project/wiki",
    "pandhelp": "https://github.com/OIV-NL-QGIS/OIV_project/wiki",
    "bouwlaaghelp": "https://github.com/OIV-NL-QGIS/OIV_project/wiki",
    "bouwlaagtekenenhelp": "https://github.com/OIV-NL-QGIS/OIV_project/wiki",
    "bouwlaagimporthelp": "https://github.com/OIV-NL-QGIS/OIV_project/wiki"
}

STATUSRGL = {
    "start" : "Selecteer tab Terrein of Bouwlaag",
    "object": {
        "toggletab": "Object: klik voor nieuw gebouw op BAG-pand, anders op bgt-terrein, voor bestaand op (blauwe) Object-stip of terrein.",

    },
    "bouwlaag": {
        "toggletab": "Bouwlaag: klik voor nieuw op (roze) bag-pand, voor bestaand op (gele) Bouwlaag.",
  
    }
}

ACTIONDICTOBJECT = {
    "Algemeen": {    
        "Bereikbaarheid" : [],
        "Dreiging": [],
        "Opstelplaats": [],
        "Point of interest": [],
        "Scenario": [],
        "Toegang": [],
        "Veiligheidsvoorzieningen": [],
        "Waterwinning": [],
        "Label": [],
        "Lijn": [],
        "Vlak": []
    }, 
    "Evenement": {
        "Bereikbaarheid" : [],
        "Dreiging": [],
        "Opstelplaats": [],
        "Point of interest": [],
        "Scenario": [],
        "Toegang": [],
        "Veiligheidsvoorzieningen": [],
        "Waterwinning": [],
        "Label": [],
        "Lijn": [],
        "Vlak": []        
    },
    "Gebouw": {
        "Bereikbaarheid" : [],
        "Dreiging": [],
        "Opstelplaats": [],
        "Point of interest": [],
        "Scenario": [],
        "Toegang": [],
        "Veiligheidsvoorzieningen": [],
        "Waterwinning": [],
        "Label": [],
        "Lijn": [],
        "Vlak": []        
    }, 
    "Infrastructuur": {
        "Bereikbaarheid" : [],
        "Dreiging": [],
        "Opstelplaats": [],
        "Point of interest": [],
        "Scenario": [],
        "Toegang": [],
        "Veiligheidsvoorzieningen": [],
        "Waterwinning": [],
        "Label": [],
        "Lijn": [],
        "Vlak": []        
    }, 
    "Natuur": {
        "Bereikbaarheid" : [],
        "Dreiging": [],
        "Opstelplaats": [],
        "Point of interest": [],
        "Scenario": [],
        "Toegang": [],
        "Veiligheidsvoorzieningen": [],
        "Waterwinning": [],
        "Label": [],
        "Lijn": [],
        "Vlak": []        
    }, 
    "Water": {
        "Bereikbaarheid" : [],
        "Dreiging": [],
        "Opstelplaats": [],
        "Point of interest": [],
        "Scenario": [],
        "Toegang": [],
        "Veiligheidsvoorzieningen": [],
        "Waterwinning": [],
        "Label": [],
        "Lijn": [],
        "Vlak": []        
    }
}

ACTIONDICTBOUWLAAG = {
    "Algemeen": {    
        "Bereikbaarheid" : [],
        "Dreiging": [],
        "Opstelplaats": [],
        "Point of interest": [],
        "Scenario": [],
        "Toegang": [],
        "Veiligheidsvoorzieningen": [],
        "Waterwinning": [],
        "Label": [],
        "Lijn": [],
        "Vlak": []
    }, 
    "Evenement": {
        "Bereikbaarheid" : [],
        "Dreiging": [],
        "Opstelplaats": [],
        "Point of interest": [],
        "Scenario": [],
        "Toegang": [],
        "Veiligheidsvoorzieningen": [],
        "Waterwinning": [],
        "Label": [],
        "Lijn": [],
        "Vlak": []        
    },
    "Gebouw": {
        "Bereikbaarheid" : [],
        "Dreiging": [],
        "Opstelplaats": [],
        "Point of interest": [],
        "Scenario": [],
        "Toegang": [],
        "Veiligheidsvoorzieningen": [],
        "Waterwinning": [],
        "Label": [],
        "Lijn": [],
        "Vlak": []        
    }, 
    "Infrastructuur": {
        "Bereikbaarheid" : [],
        "Dreiging": [],
        "Opstelplaats": [],
        "Point of interest": [],
        "Scenario": [],
        "Toegang": [],
        "Veiligheidsvoorzieningen": [],
        "Waterwinning": [],
        "Label": [],
        "Lijn": [],
        "Vlak": []        
    }, 
    "Natuur": {
        "Bereikbaarheid" : [],
        "Dreiging": [],
        "Opstelplaats": [],
        "Point of interest": [],
        "Scenario": [],
        "Toegang": [],
        "Veiligheidsvoorzieningen": [],
        "Waterwinning": [],
        "Label": [],
        "Lijn": [],
        "Vlak": []        
    }, 
    "Water": {
        "Bereikbaarheid" : [],
        "Dreiging": [],
        "Opstelplaats": [],
        "Point of interest": [],
        "Scenario": [],
        "Toegang": [],
        "Veiligheidsvoorzieningen": [],
        "Waterwinning": [],
        "Label": [],
        "Lijn": [],
        "Vlak": []        
    }
}