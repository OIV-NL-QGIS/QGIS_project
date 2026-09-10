"""edit specific feature"""
import qgis.core as QC
import oiv.helpers.messages as MSG


def delete_features(ilayer, editableLayerNames, confirm):
    """Delete selected features from a QGIS layer"""
    if ilayer.name() not in editableLayerNames:
        MSG.showMsgBox('layernoteditable')
        ilayer.selectByIds([])
        return "Done"
    features = ilayer.selectedFeatures()
    if not features:
        return "Done"
    # Alleen bevestigen als dit gevraagd wordt
    if confirm:
        reply = MSG.showMsgBox('deleteobject_question')
        if not reply:
            ilayer.selectByIds([])
            return "Done"
    ilayer.startEditing()
    for feature in features:
        ilayer.deleteFeature(feature.id())
    if ilayer.commitChanges():
        ilayer.selectByIds([])
        ilayer.triggerRepaint()
        return "Done"
    ilayer.rollBack()
    return "Retry"

def getfeature_geometry(featGeom, layerType):
    """get geometry type of a feature"""
    geom = None
    if layerType == 'LineString' and featGeom.wkbType() in [2, 1002, 2002, 3002, -2147483646]:
        geom = QC.QgsGeometry.fromMultiPolylineXY([featGeom.asPolyline()])
    elif layerType == 'LineString' and featGeom.wkbType() in [5, 1005, 2005, 3005]:
        geom = QC.QgsGeometry.fromMultiPolylineXY(featGeom.asMultiPolyline())
    elif layerType == 'Polygon' and featGeom.wkbType() in [3, 1003, 2003, 3003]:
        geom = QC.QgsGeometry.fromMultiPolygonXY([featGeom.asPolygon()])
    elif layerType == 'Polygon' and featGeom.wkbType() in [6, 1006, 2006, 3006]:
        geom = QC.QgsGeometry.fromMultiPolygonXY(featGeom.asMultiPolygon())
    elif layerType == 'Point':
        geom = QC.QgsGeometry.fromPointXY(featGeom.asPoint())
    return geom
