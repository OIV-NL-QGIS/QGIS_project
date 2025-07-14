"""utilities to adjust the UI of the widgets"""
import qgis.core as QC
import oiv.helpers.utils_core as UC
import oiv.helpers.configdb_helper as CH
import oiv.helpers.constants as PC
import oiv.helpers.messages as MSG

layerCategorieDict = {
    "alternatieve_type": "Waterwinning",
    "afw_binnendekking_type": "Bereikbaarheid",
    "bereikbaarheid_type": "Lijn",
    "dreiging_type": "Dreiging",
    "gebiedsgerichte_aanpak_type": "Lijn",
    "gevaarlijkestof_opslag_type": "Dreiging",
    "ingang_type": "Toegang",
    "isolijnen_type": "Lijn",
    "label_type": "Label",
    "opstelplaats_type": "Opstelplaats",
    "points_of_interest_type": "Point of interest",
    "ruimten_type": "Vlak",
    "scenario_locatie_type": "Scenario",
    "sectoren_type": "Vlak",
    "sleutelkluis_type": "Toegang",
    "veiligh_bouwk_type": "Lijn",
    "veiligh_install_type": "Veiligheidsvoorzieningen"
}

def set_layer_substring(subString, bouwlaagOfObject='bouwlaag'):
    """set layer subset according (you can check the subset under properties of the layer)"""
    layersInEditMode = []
    if bouwlaagOfObject == 'object':
        layerNamesTup = CH.get_chidlayers_ob()
        extraLayerNames = PC.OBJECT["werkvoorraadlayers"]
        extraLayerNames.append('Objecten')
    else:
        layerNamesTup = CH.get_chidlayers_bl()
        extraLayerNames = PC.PAND["werkvoorraadlayers"]
    layerNames = [i[0] for i in layerNamesTup]
    layerNames = layerNames + extraLayerNames
    for layerName in layerNames:
        layer = UC.getlayer_byname(layerName)
        if layer:
            if layer.isModified():
                saveChanges = MSG.showMsgBox('unsavedchanges', layerName)
                if saveChanges:
                    layer.commitChanges()
                else:
                    layer.rollBack()
            elif layer.isEditable():
                layersInEditMode.append(layer)
                layer.commitChanges()
    for layerName in layerNames:
        lyr = UC.getlayer_byname(layerName)
        if lyr:
            if layerName == 'Objecten':
                lyr.setSubsetString(subString.replace('object_', ''))
            else:
                lyr.setSubsetString(subString)
            if lyr in layersInEditMode:
                lyr.startEditing()
    return "succes"

def set_lengte_oppervlakte_visibility(widget, lengteTF, straalTF, oppTF, offsetTF):
    """change UI based on drawing lines/polygons"""
    if True in (lengteTF, straalTF, oppTF, offsetTF):
        widget.cadframe.setVisible(True)
    else:
        widget.cadframe.setVisible(False)
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

def get_actions(whichConfig, actionDict):
    """connect buttons and signals to the real action run"""
    #skip first line because of header
    editableLayerNames = []
    moveLayerNames = []
    snapSymbols = []
    anchorpoints = {
        "anchorpointtop": [],
        "anchorpointbottom": []
    }
    query = "SELECT child_layer, layertype, type_layer_name, type_layer_name_identifier FROM '{}'".format(whichConfig)
    layers = UC.read_settings(query, True)
    for lyr in layers:
        layerName = lyr[0]
        layerType = lyr[1]
        typeLayerName = lyr[2]
        idColumn = lyr[3]
        editableLayerNames.append(layerName)
        layer = UC.getlayer_byname(typeLayerName)
        if layerType == "point" or layerType == "label":
            moveLayerNames.append(layerName)
        if layer:
            categorie = layerCategorieDict[typeLayerName]
            request = QC.QgsFeatureRequest()
            clause = QC.QgsFeatureRequest.OrderByClause('volgnummer', ascending=True)
            orderby = QC.QgsFeatureRequest.OrderBy([clause])
            request.setOrderBy(orderby)
            if whichConfig == PC.PAND["configtable"]:
                request.setFilterExpression('"actief_bouwlaag" = true')
            else:
                request.setFilterExpression('"actief_ruimtelijk" = true')
            featureIt = layer.getFeatures(request)
            for feat in featureIt:
                landOfReg = 'regionaal'
                if layerType == "point":
                    if feat["symbol_name"][:3] in ['poi', 'drg', 'bbh', 'wwn', 'tgn', 'vvz', 'osp', 'gev']:
                        symbol = feat["symbol_name"] + '_' + feat["symbol_type"]
                        landOfReg = 'landelijk'
                    else:
                        symbol = feat["symbol_name"]
                    if feat["snap"]:
                        snapSymbols.append(feat["naam"])
                    if feat["anchorpoint"] == 'top':
                        anchorpoints["anchorpointtop"].append(feat[idColumn])
                    elif feat["anchorpoint"] == 'bottom':
                        anchorpoints["anchorpointbottom"].append(feat[idColumn])
                else:
                    symbol = feat[idColumn].replace(' ', '_').lower()
                for key,value in feat["tabbladen"].items():
                    if value == 1:
                        actionDict[key][categorie].append((layerName, feat[idColumn], feat[idColumn].replace(' ', '_'), symbol, landOfReg))
    return actionDict, editableLayerNames, moveLayerNames, snapSymbols, anchorpoints
