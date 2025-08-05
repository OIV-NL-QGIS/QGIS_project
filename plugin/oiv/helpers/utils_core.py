"""utils that are requested from the core plugin"""
import os
import sqlite3
import webbrowser
import math

import qgis.PyQt.QtWidgets as PQtW
import qgis.core as QC

import oiv.helpers.messages as MSG
import oiv.helpers.constants as PC
import oiv.helpers.configdb_helper as CH

def open_url(url):
    webbrowser.open(url)

def featureRequest(ilayer, request=None, mandatory=True):
    it = ilayer.getFeatures(request)
    try:
        ifeature = next(it)
        return ifeature
    except:
        if mandatory:
            MSG.showMsgBox('nofeature')
        return None

def read_settings(query, allResult):
    conn = None
    try:
        db_path = os.path.join(os.path.dirname(__file__), '..\\config_files\\configDB.db')
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

def getlayer_byname(layername):
    """get QgsLayer by name"""
    layer = None
    layers = QC.QgsProject.instance().mapLayersByName(layername)
    if layers:
        layer = layers[0]
    return layer

def user_input_label(label_req, question):
    """communiceer met de gebruiker voor input, waarbij question de vraag is die wordt gesteld"""
    label = ''
    qid = PQtW.QInputDialog()
    if label_req == '1':
        while True:
            label, ok = PQtW.QInputDialog.getText(qid, "Label:", question, PQtW.QLineEdit.Normal,)
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
    if layer.geometryType() == QC.QgsWkbTypes.PointGeometry:
        layerType = "Point"
    elif layer.geometryType() == QC.QgsWkbTypes.LineGeometry:
        layerType = "LineString"
    elif layer.geometryType() == QC.QgsWkbTypes.PolygonGeometry:
        layerType = "Polygon"
    else:
        layerType = "undefined"
    return layerType

def write_layer(layer, features, count=False, check=True):
    """write the attributes to layer"""
    checkGeomValidity = True
    if check:
        checkGeomValidity = features.geometry().isGeosValid()
    if checkGeomValidity:
        layer.startEditing()
        if not isinstance(features, list):
            features = [features]
        dummy, newFeatures = layer.dataProvider().addFeatures(features)
        layer.commitChanges()
        layer.reload()
        layer.triggerRepaint()
        return newFeatures[0].id()
    else:
        layer.commitChanges()
        if count:
            return 'invalid'
        else:
            MSG.showMsgBox('invalidgeometry')

def nearest_neighbor(layer, geom, geomType, objectId):
    """search the nearest parent feature id"""
    parentId = None
    dist = 9999
    if geomType in ("LineString", "Polygon"):
        geomCtr = geom.centroid()
    else:
        geomCtr = geom
    if layer.name() == PC.PAND["bouwlaaglayername"]:
        request = QC.QgsFeatureRequest().setFilterExpression('"pand_id" = ' + "'{}'".format(objectId))
        it = layer.getFeatures(request)
        for feat in it:
            parentCtr = feat.geometry().centroid()
            distance = geomCtr.distance(parentCtr)
            if distance < dist:
                dist = distance
                parentId = feat["id"]
    else:
        parentId = nearest_neighbor_point(layer, geom, 1)
    return parentId

def nearest_neighbor_point(layer, point, k):
    index = None
    parentId = None
    extent = layer.extent()
    index = QC.QgsSpatialIndex(layer.getFeatures(QC.QgsFeatureRequest(extent)))
    try:
        parentId = index.nearestNeighbor(point, k)[0]
    except: # pylint: disable=bare-except
        pass
    return parentId

def request_feature(ifeature, layer_feature_id, layer_name):
    """get feature from specific id"""
    ifeature = None
    objectId = ifeature[layer_feature_id]
    ilayer = getlayer_byname(layer_name)
    request = QC.QgsFeatureRequest().setFilterExpression('"id" = ' + str(objectId))
    ifeature = featureRequest(ilayer, request)
    if ifeature:
        return ifeature, objectId

def create_unique_sorted_list(sortList):
    """create unique sorted dropdown list"""
    output = []
    for x in sortList:
        if x not in output:
            output.append(x)
    output.sort()
    return output

def refresh_layers(iface):
    """refresh all layers on the canvas"""
    for layer in iface.mapCanvas().layers():
        layer.triggerRepaint()

def get_possible_snapFeatures_bouwlaag(layerNamesList, objectId):
    possibleSnapFeatures = []
    bouwlaagIds = []
    lyr = getlayer_byname(PC.PAND["bouwlaaglayername"])
    request = QC.QgsFeatureRequest().setFilterExpression('"pand_id" = ' + "'{}'".format(objectId))
    featureIt = lyr.getFeatures(request)
    baglayerName = PC.PAND["bagpandlayername"] + QC.QgsExpressionContextUtils.globalScope().variable('OIV_bag_connection')
    for feat in featureIt:
        bouwlaagIds.append(feat["id"])
    for name in layerNamesList:
        lyr = getlayer_byname(name)
        if lyr:
            if name == baglayerName:
                request = QC.QgsFeatureRequest().setFilterExpression('"identificatie" = ' + "'{}'".format(objectId))
                ifeature = featureRequest(lyr, request, False)
                if ifeature:
                    possibleSnapFeatures.append(ifeature.geometry())
            elif name == PC.PAND["bouwlaaglayername"]:
                request = QC.QgsFeatureRequest().setFilterExpression('"pand_id" = ' + "'{}'".format(objectId))
                featureIt = lyr.getFeatures(request)
                for feat in featureIt:
                    bouwlaagIds.append(feat["id"])
                    possibleSnapFeatures.append(feat.geometry())
            elif bouwlaagIds:
                for bid in bouwlaagIds:
                    request = QC.QgsFeatureRequest().setFilterExpression('"bouwlaag_id" = ' + str(bid))
                    featureIt = lyr.getFeatures(request)
                    for feat in featureIt:
                        possibleSnapFeatures.append(feat.geometry())
    return possibleSnapFeatures

def get_possible_snapFeatures_object(layerNamesList, objectId):
    possibleSnapFeatures = []
    for name in layerNamesList:
        lyr = getlayer_byname(name)
        if lyr:
            request = QC.QgsFeatureRequest().setFilterExpression('"object_id" = ' + str(objectId))
            featureIt = lyr.getFeatures(request)
            for feat in featureIt:
                if feat.hasGeometry():
                    possibleSnapFeatures.append(feat.geometry())
    return possibleSnapFeatures

def get_possible_snapFeatures_ioi(layerNamesList):
    possibleSnapFeatures = []
    for name in layerNamesList:
        lyr = getlayer_byname(name)
        featureIt = lyr.getFeatures()
        for feat in featureIt:
            possibleSnapFeatures.append(feat.geometry())
    return possibleSnapFeatures

def construct_feature(layerType, parentLayerName, points, objectId):
    tempFeature = QC.QgsFeature()
    parentId = None
    #converteer lijst van punten naar QgsGeometry, afhankelijk van soort geometrie
    if layerType == "Point":
        geom = QC.QgsGeometry.fromPointXY(points)
        tempFeature.setGeometry(geom)
    elif layerType == "LineString":
        geom = QC.QgsGeometry.fromPolylineXY(points)
        tempFeature.setGeometry(geom)
    elif layerType == "Polygon":
        geom = QC.QgsGeometry.fromPolygonXY([points])
        tempFeature.setGeometry(geom)
    if parentLayerName != '' and parentLayerName == PC.OBJECT["objectlayername"]:
        parentlayer = getlayer_byname(parentLayerName)
        parentId = int(objectId)
    elif parentLayerName != '' and parentLayerName is not None:
        parentlayer = getlayer_byname(parentLayerName)
        parentId = nearest_neighbor(parentlayer, geom, layerType, objectId)
    elif parentLayerName is None:
        parentId = ''
    else:
        parentId = None
    #foutafhandeling ivm als er geen parentId is
    if parentId is None and parentLayerName != '':
        MSG.showMsgBox('noparentfeature')
        return None, None
    else:
        return parentId, tempFeature

def get_attributes(foreignKey, childFeature, snapAngle, input_id, drawLayer, whichConfig):
    drawLayerName = drawLayer.name()
    #haal de vraag voor de inputdialog vanuit de config file
    query = "SELECT foreign_key, identifier, input_label, question, label_required, rotatie\
             FROM {} WHERE child_layer = '{}'".format(whichConfig, drawLayerName)
    attrs = read_settings(query, False)
    labelTekst = user_input_label(attrs[4], attrs[3])
    #attribuut naam ophalen van de foreignkey
    if labelTekst != 'Cancel':
        fields = drawLayer.fields()
        #initialiseer de childFeature
        childFeature.initAttributes(fields.count())
        childFeature.setFields(fields)
        #invullen van label, foreignkey en rotatie op de juiste plaats in childFeature
        field_index = fields.indexFromName('applicatie')
        if field_index != -1:
            childFeature['applicatie'] = 'OIV'
        if attrs[1]:
            if str(input_id).isdigit():
                childFeature[attrs[1]] = int(input_id)
            else:
                childFeature[attrs[1]] = input_id
        if attrs[2]:
            childFeature[attrs[2]] = labelTekst
        if attrs[0]:
            childFeature[attrs[0]] = foreignKey
        if snapAngle is not None:
            childFeature[attrs[5]] = int(snapAngle)
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


def is_layer_visible(layer):
    """Checks if the layer is currently set visible in the layer tree."""
    layer_tree_root = QC.QgsProject.instance().layerTreeRoot()
    layer_tree_layer = layer_tree_root.findLayer(layer)
    return layer_tree_layer.isVisible()

def move_point(feat, distance, angle_deg):
    geom = feat.geometry()
    if angle_deg:
        angle_rad = math.radians(angle_deg)
    else:
        angle_rad = 0
    dx = distance * math.sin(angle_rad)
    dy = distance * math.cos(angle_rad)
    geom.translate(dx, dy)
    feat.setGeometry(geom)
    return feat