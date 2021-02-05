"""utilities to adjust the UI of the widgets"""
import oiv.tools.utils_core as UC
import oiv.plugin_helpers.configdb_helper as CH
import oiv.plugin_helpers.messages as MSG

def set_layer_substring(subString):
    """set layer subset according (you can check the subset under properties of the layer)"""
    layersInEditMode = []
    layerNames = CH.get_chidlayers_bl()
    for layerName in layerNames:
        layer = UC.getlayer_byname(layerName[0])
        if layer.isModified():
            saveChanges = MSG.showMsgBox('unsavedchanges', layerName[0])
            if saveChanges:
                layer.commitChanges()
            else:
                layer.rollBack()
        elif layer.isEditable():
            layersInEditMode.append(layer)
            layer.commitChanges()
    for layerName in layerNames:
        lyr = UC.getlayer_byname(layerName[0])
        lyr.setSubsetString(subString)
        if lyr in layersInEditMode:
            lyr.startEditing()
    return "succes"

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
    layers = UC.read_settings(query, True)
    for layer in layers:
        layerName = layer[0]
        csvPath = layer[1]
        configTable = layer[2]
        if csvPath:
            editableLayerNames.append(layerName)
            layer = UC.getlayer_byname(layerName)
            layerType = UC.check_layer_type(layer)
            if layerType == "Point":
                moveLayerNames.append(layerName)
            if configTable:
                query = "SELECT '{}', type_id, button_name FROM {}".format(layerName, configTable)
                actionList.append(UC.read_settings(query, True))
    return actionList, editableLayerNames, moveLayerNames
