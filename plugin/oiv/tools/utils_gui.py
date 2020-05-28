"""utilities to adjust the UI of the widgets"""
import os
import sqlite3
from .utils_core import getlayer_byname, check_layer_type, read_settings

def set_layer_substring(subString):
    """set layer subset according (you can check the subset under properties of the layer)"""
    layerNames = read_settings("SELECT child_layer FROM config_bouwlaag;", True)
    for layerName in layerNames:
        layer = getlayer_byname(layerName[0])
        layer.setSubsetString(subString)

def set_lengte_oppervlakte_visibility(widget, lengteTF, straalTF, oppTF, offsetTF):
    """change UI based on drawing lines/polygons"""
    widget.lengte_label.setVisible(lengteTF)
    widget.lengte.setVisible(lengteTF)
    widget.straal.setVisible(straalTF)
    widget.straal_label.setVisible(straalTF)
    widget.straal_button.setVisible(straalTF)
    widget.straal_button.setCheckable(straalTF)
    widget.oppervlakte_label.setVisible(oppTF)
    widget.oppervlakte.setVisible(oppTF)
    widget.offset.setVisible(offsetTF)
    widget.offset_label.setVisible(offsetTF)
    widget.offset_button.setVisible(offsetTF)
    widget.offset_button.setCheckable(offsetTF)

def read_config_file(file, layerName):
    """Read lines from input file and convert to list"""
    configList = []
    basepath = os.path.dirname(__file__)
    if layerName is None:
        layerName = []
    if basepath:
        os.chdir(basepath)
    with open("../" + file, "r") as inputFile:
        lines = inputFile.read().splitlines()
    for line in lines:
        configList.append(layerName + line.split(','))
    inputFile.close()
    return configList

def get_actions(whichConfig):
    """connect buttons and signals to the real action run"""
    #skip first line because of header
    editableLayerNames = []
    moveLayerNames = []
    actionList = []
    query = "SELECT child_layer, bestand, type_layer_name FROM '{}'".format(whichConfig)
    layers = read_settings(query, True)
    for layer in layers:
        layerName = layer[0]
        csvPath = layer[1]
        typeLayerName = layer[2]
        if csvPath:
            editableLayerNames.append(layerName)
            layer = getlayer_byname(layerName)
            layerType = check_layer_type(layer)
            if layerType == "Point":
                moveLayerNames.append(layerName)
            if typeLayerName:
                query = "SELECT '{}', id, button_name FROM {}".format(layerName, typeLayerName)
                print(read_actions(query, True))
            actionList.append(read_config_file(csvPath, [layerName]))
    #print(actionList)
    return actionList, editableLayerNames, moveLayerNames

def read_actions(query, allResult):
    conn = None
    try:
        db_path = os.path.join(os.path.dirname(__file__), '..\\config_files\\dimension_tables.db')
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        cursor.execute(query)
        if allResult:
            result = cursor.fetchall()
        else:
            result = cursor.fetchone()
        cursor.close()
        return result
    except sqlite3.Error as error:
        print("Failed to read data from sqlite table", error)
    finally:
        if conn:
            conn.close()
