"""utils that are requested from the core plugin"""
import os
from qgis.core import QgsProject, QgsWkbTypes, QgsSpatialIndex, QgsFeatureRequest, QgsGeometry, QgsFeature
from qgis.PyQt.QtWidgets import QInputDialog, QLineEdit, QMessageBox

def getlayer_byname(layername):
    """get QgsLayer by name"""
    layer = None
    layers = QgsProject.instance().mapLayersByName(layername)
    layer = layers[0]
    return layer

def user_input_label(label_req, question):
    """communiceer met de gebruiker voor input, waarbij question de vraag is die wordt gesteld"""
    label = ''
    qid = QInputDialog()
    if label_req < '2' and label_req != '':
        while True:
            label, ok = QInputDialog.getText(qid, "Label:", question, QLineEdit.Normal,)
            if ok:
                if label != '' or label_req == '0':
                    return label
            else:
                label = 'Cancel'
                return label
    else:
        return label

def check_layer_type(layer):
    """derivation of layer type"""
    layerType = None
    if layer.geometryType() == QgsWkbTypes.PointGeometry:
        layerType = "Point"
    elif layer.geometryType() == QgsWkbTypes.LineGeometry:
        layerType = "Line"
    elif layer.geometryType() == QgsWkbTypes.PolygonGeometry:
        layerType = "Polygon"
    else:
        layerType = "undefined"
    return layerType

def write_layer(layer, childFeature):
    """write the attributes to layer"""
    layer.startEditing()
    dummy, newFeatures = layer.dataProvider().addFeatures([childFeature])
    layer.commitChanges()
    layer.triggerRepaint()
    return newFeatures[0].id()

def nearest_neighbor(iface, layer, point):
    """search the nearest parent feature id"""
    index = None
    parentId = None
    parentFeature = None
    extent = iface.mapCanvas().extent()
    #veroorzaakt foutmelding als er niets in het kaartvenster staat, daarom in try/except statement
    index = QgsSpatialIndex(layer.getFeatures(QgsFeatureRequest(extent)))
    try:
        parentId = index.nearestNeighbor(point, 1)[0]
        parentFeature = next(layer.getFeatures(QgsFeatureRequest(parentId)))
    except: # pylint: disable=bare-except
        pass
    return parentFeature, parentId

def request_feature(ifeature, layer_feature_id, layer_name):
    """get feature from specific id"""
    objectId = ifeature[layer_feature_id]
    request = QgsFeatureRequest().setFilterExpression('"id" = ' + str(objectId))
    tempLayer = getlayer_byname(layer_name)
    tempFeature = next(tempLayer.getFeatures(request))
    return tempFeature, objectId

def create_unique_sorted_list(sortList):
    """create unique sorted dropdown list"""
    output = []
    for x in sortList:
        if x not in output:
            output.append(x)
    output.sort()
    return output

def set_layer_substring(readConfig, subString):
    """set layer subset according (you can check the subset under properties of the layer)"""
    for line in readConfig[1:]:
        layer = getlayer_byname(line[0])
        layer.setSubsetString(subString)

def refresh_layers(iface):
    """refresh all layers on the canvas"""
    for layer in iface.mapCanvas().layers():
        layer.triggerRepaint()

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

def get_actions(configLines):
    """connect buttons and signals to the real action run"""
    #skip first line because of header
    editableLayerNames = []
    moveLayerNames = []
    actionList = []
    for line in configLines[1:]:
        layerName = line[0]
        csvPath = line[1]

        if csvPath:
            editableLayerNames.append(layerName)
            layer = getlayer_byname(layerName)
            layerType = check_layer_type(layer)

            if layerType == "Point":
                moveLayerNames.append(layerName)

            actionList.append(read_config_file(csvPath, [layerName]))
    return actionList, editableLayerNames, moveLayerNames

def get_possible_snapFeatures_bouwlaag(layerNamesList, objectId):
    possibleSnapFeatures = []
    bouwlaagIds = []
    for name in layerNamesList:
        lyr = getlayer_byname(name)
        if name == 'BAG panden':
            request = QgsFeatureRequest().setFilterExpression('"identificatie" = ' + objectId)
            tempFeature = next(lyr.getFeatures(request))
            possibleSnapFeatures.append(tempFeature.geometry())
        elif name == 'Bouwlagen':
            request = QgsFeatureRequest().setFilterExpression('"pand_id" = ' + objectId)
            featureIt = lyr.getFeatures(request)
            for feat in featureIt:
                bouwlaagIds.append(feat["id"])
                possibleSnapFeatures.append(feat.geometry())
        elif bouwlaagIds:
            for bid in bouwlaagIds:
                request = QgsFeatureRequest().setFilterExpression('"bouwlaag_id" = ' + str(bid))
                featureIt = lyr.getFeatures(request)
                for feat in featureIt:
                    possibleSnapFeatures.append(feat.geometry())
    return possibleSnapFeatures

def get_possible_snapFeatures_object(layerNamesList, objectId):
    possibleSnapFeatures = []
    objectIds = []
    for name in layerNamesList:
        lyr = getlayer_byname(name)
        if name == 'Object':
            request = QgsFeatureRequest().setFilterExpression('"id" = ' + objectId)
            tempFeature = next(lyr.getFeatures(request))
            possibleSnapFeatures.append(tempFeature.geometry())
        elif name == 'Object terrein':
            request = QgsFeatureRequest().setFilterExpression('"id" = ' + objectId)
            featureIt = lyr.getFeatures(request)
            for feat in featureIt:
                possibleSnapFeatures.append(feat.geometry())
                objectIds.append(feat["id"])
        elif objectIds:
            for bid in objectIds:
                request = QgsFeatureRequest().setFilterExpression('"object_id" = ' + str(bid))
                featureIt = lyr.getFeatures(request)
                for feat in featureIt:
                    possibleSnapFeatures.append(feat.geometry())
    return possibleSnapFeatures

def construct_feature(layerType, parentLayerName, points, objectId, iface):
    tempFeature = QgsFeature()
    parentId = None
    #converteer lijst van punten naar QgsGeometry, afhankelijk van soort geometrie
    if layerType == "Point":
        tempFeature.setGeometry(QgsGeometry.fromPointXY(points))
        geom = points
    elif layerType == "Line":
        tempFeature.setGeometry(QgsGeometry.fromPolylineXY(points))
        geom = points[0]
    elif layerType == "Polygon":
        tempFeature.setGeometry(QgsGeometry.fromPolygonXY([points]))
        geom = points[0]

    if parentLayerName != '' and parentLayerName == 'Objecten':
        parentlayer = getlayer_byname(parentLayerName)
        parentId = int(objectId)
    elif parentLayerName != '':
        parentlayer = getlayer_byname(parentLayerName)
        dummy, parentId = nearest_neighbor(iface, parentlayer, geom)
    else:
        parentId = None

    #foutafhandeling ivm als er geen parentId is
    if parentId is None and parentLayerName != '':
        QMessageBox.information(None, "Oeps:", "Geen object gevonden om aan te koppelen.")
        return None, None
    else:
        return parentId, tempFeature

def get_attributes(foreignKey, childFeature, snapAngle, input_id, drawLayer, configFile):
    drawLayerName = drawLayer.name()
    #haal de vraag voor de inputdialog vanuit de config file
    attrs = {"foreign_key" : '', "identifier" : '', "input_label" : '', "question" : '', "label_required" : ''}
    attrs = get_draw_layer_attr(attrs, drawLayerName, configFile)
    labelTekst = user_input_label(attrs["label_required"], attrs["question"])
    #attribuut naam ophalen van de foreignkey
    if labelTekst != 'Cancel':
        fields = drawLayer.fields()
        #initialiseer de childFeature
        childFeature.initAttributes(fields.count())
        childFeature.setFields(fields)
        #invullen van label, foreignkey en rotatie op de juiste plaats in childFeature
        if attrs["identifier"] != '':
            if str(input_id).isdigit():
                childFeature[attrs["identifier"]] = int(input_id)
            else:
                childFeature[attrs["identifier"]] = input_id
        if attrs["input_label"] != '':
            childFeature[attrs["input_label"]] = labelTekst
        if attrs["foreign_key"] != '':
            childFeature[attrs["foreign_key"]] = foreignKey
        if snapAngle is not None:
            childFeature['rotatie'] = snapAngle
        return childFeature
    else:
        return 'Cancel'

def get_draw_layer_attr(attrDict, runLayerName, configFile):
    """get attribute value out of config file related to header(q_string)"""
    headerCsv = []
    headerCsv = configFile[0]
    for line in configFile:
        if line[0] == runLayerName:
            for key in attrDict:
                attrY = headerCsv.index(key)
                attrDict[key] = line[attrY]
    return attrDict
