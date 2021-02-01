"""filter on type of repressief object"""
import qgis.PyQt.QtCore as PQtC #pylint: disable=import-error

import oiv.tools.utils_core as UC
import oiv.plugin_helpers.drawing_helper as DH

def init_filter_section(wdgt):
    wdgt.filterframe.setVisible(True)
    wdgt.objecttype.clear()
    wdgt.objecttype.addItems(DH.OBJECTTYPES)
    set_current_date(wdgt)

def set_current_date(wdgt):
    now = PQtC.QDateTime.currentDateTime()
    wdgt.datum_vanaf.setDateTime(now)
    wdgt.datum_tot.setDateTime(now)

def set_object_filter(wdgt):
    filters = []
    if wdgt.checkVanaf.isChecked():
        filters.append("(datum_geldig_vanaf >= '{}' OR datum_geldig_vanaf IS NULL)".format(wdgt.datum_vanaf.date().toPyDate()))
    if wdgt.checkTot.isChecked():
        filters.append("(datum_geldig_tot < '{}' OR datum_geldig_tot IS NULL)".format(wdgt.datum_tot.date().toPyDate()))
    if wdgt.checkSoort.isChecked():
        filters.append("typeobject = '{}'".format(wdgt.objecttype.currentText()))
    layerNames = UC.read_settings("SELECT child_layer FROM config_object;", True)
    if filters:
        subString = ' AND '.join(filters)
    else:
        subString = ''
    for layerName in layerNames:
        if layerName[0] != 'Alternatief bluswater':#TO_DO:alle lagen die geen objecten als parent hebben
            layer = UC.getlayer_byname(layerName[0])
            layer.setSubsetString(subString)
