"""utils that are requested from the core plugin"""
import os
import sqlite3
import webbrowser

import qgis.PyQt.QtWidgets as PQtW #pylint: disable=import-error
import qgis.core as QC #pylint: disable=import-error

import oiv.plugin_helpers.messages as MSG
import oiv.plugin_helpers.plugin_constants as PC

def open_url(url):
    webbrowser.open(url)

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

def write_layer(layer, childFeature, count=False):
    """write the attributes to layer"""
    layer.startEditing()
    checkGeomValidity = childFeature.geometry().isGeosValid()
    if checkGeomValidity:
        dummy, newFeatures = layer.dataProvider().addFeatures([childFeature])
        layer.commitChanges()
        layer.reload()
        layer.triggerRepaint()
        return newFeatures[0].id()
    else:
        layer.commitChanges()
        MSG.showMsgBox('invalidgeometry')
        if count:
            return 'invalid'

def nearest_neighbor(iface, layer, point):
    """search the nearest parent feature id"""
    index = None
    parentId = None
    parentFeature = None
    extent = iface.mapCanvas().extent()
    #veroorzaakt foutmelding als er niets in het kaartvenster staat, daarom in try/except statement
    index = QC.QgsSpatialIndex(layer.getFeatures(QC.QgsFeatureRequest(extent)))
    try:
        parentId = index.nearestNeighbor(point, 1)[0]
        parentFeature = next(layer.getFeatures(QC.QgsFeatureRequest(parentId)))
        parentId = parentFeature["id"]
    except: # pylint: disable=bare-except
        pass
    return parentFeature, parentId

def request_feature(ifeature, layer_feature_id, layer_name):
    """get feature from specific id"""
    objectId = ifeature[layer_feature_id]
    request = QC.QgsFeatureRequest().setFilterExpression('"id" = ' + str(objectId))
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

def refresh_layers(iface):
    """refresh all layers on the canvas"""
    for layer in iface.mapCanvas().layers():
        layer.triggerRepaint()

def get_possible_snapFeatures_bouwlaag(layerNamesList, objectId):
    possibleSnapFeatures = []
    bouwlaagIds = []
    for name in layerNamesList:
        lyr = getlayer_byname(name)
        if name == PC.bagpand_layername():
            request = QC.QgsFeatureRequest().setFilterExpression('"identificatie" = ' + "'{}'".format(objectId))
            tempFeature = next(lyr.getFeatures(request))
            possibleSnapFeatures.append(tempFeature.geometry())
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
        request = QC.QgsFeatureRequest().setFilterExpression('"object_id" = ' + str(objectId))
        featureIt = lyr.getFeatures(request)
        for feat in featureIt:
            if feat.hasGeometry():
                possibleSnapFeatures.append(feat.geometry())
    return possibleSnapFeatures

def construct_feature(layerType, parentLayerName, points, objectId, iface):
    tempFeature = QC.QgsFeature()
    parentId = None
    #converteer lijst van punten naar QgsGeometry, afhankelijk van soort geometrie
    if layerType == "Point":
        tempFeature.setGeometry(QC.QgsGeometry.fromPointXY(points))
        geom = points
    elif layerType == "LineString":
        tempFeature.setGeometry(QC.QgsGeometry.fromPolylineXY(points))
        geom = points[0]
    elif layerType == "Polygon":
        tempFeature.setGeometry(QC.QgsGeometry.fromPolygonXY([points]))
        geom = points[0]
    if parentLayerName != '' and parentLayerName == PC.OBJECT["objectlayername"]:
        parentlayer = getlayer_byname(parentLayerName)
        parentId = int(objectId)
    elif parentLayerName != '' and parentLayerName is not None:
        parentlayer = getlayer_byname(parentLayerName)
        dummy, parentId = nearest_neighbor(iface, parentlayer, geom)
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
