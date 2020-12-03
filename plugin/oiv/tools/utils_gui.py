"""utilities to adjust the UI of the widgets"""
import os
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

def get_actions(whichConfig):
    """connect buttons and signals to the real action run"""
    #skip first line because of header
    editableLayerNames = []
    moveLayerNames = []
    actionList = []
    query = "SELECT child_layer, bestand, config_table FROM '{}'".format(whichConfig)
    layers = read_settings(query, True)
    for layer in layers:
        layerName = layer[0]
        csvPath = layer[1]
        configTable = layer[2]
        if csvPath:
            editableLayerNames.append(layerName)
            layer = getlayer_byname(layerName)
            layerType = check_layer_type(layer)
            if layerType == "Point":
                moveLayerNames.append(layerName)
            if configTable:
                query = "SELECT '{}', type_id, button_name FROM {}".format(layerName, configTable)
                actionList.append(read_settings(query, True))
    return actionList, editableLayerNames, moveLayerNames
