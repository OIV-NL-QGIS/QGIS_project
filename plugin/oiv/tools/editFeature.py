"""edit specific feature"""
import qgis.core as QC #pylint: disable=import-error
import oiv.plugin_helpers.messages as MSG

def delete_feature(ilayer, ifeature, rightLayerNames, _iface):
    """delete a feature"""
    if ilayer.name() in rightLayerNames:
        ids = []
        ids.append(ifeature.id())
        ilayer.selectByIds(ids)
        ilayer.startEditing()
        reply = MSG.showMsgBox('deleteobject')
        if not reply:
            ilayer.selectByIds([])
        elif reply:
            ilayer.deleteFeature(ifeature.id())
            ilayer.commitChanges()
        return "Done"
    else:
        reply = MSG.showMsgBox('noselectedtodelete')
        if reply:
            ilayer.selectByIds([])
            return "Done"
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
