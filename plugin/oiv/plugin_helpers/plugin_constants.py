OIV_VERSION = '3.2.9'

PLUGIN = {
    "name": "OIV Objecten",
    "icon": ":/plugins/oiv/config_files/png/oiv_plugin.png",
    "toolbartext": "OIV " + OIV_VERSION + " | Actieve bouwlaag: ",
    "compatibleDbVersion" : [324, 329],
    "menulocation": "&OIV Objecten"
}

PAND = {
    "bagpandlayername": "BAG panden",
    "bouwlaaglayername": "Bouwlagen",
    "minbouwlaag": -10,
    "maxbouwlaag": 30,
    "configtable": "config_bouwlaag",
    "tekenwidgetui": "oiv_tekenen_widget.ui",
    "bouwlaagui": "oiv_bouwlaag_widget.ui",
    "pandui": "oiv_pandgegevens_widget.ui",
    "bagviewerurl": "https://bagviewer.kadaster.nl/lvbag/bag-viewer/#?searchQuery=",
}
