
from qgis.PyQt.QtWidgets import QMessageBox #pylint: disable=import-error
from qgis.core import QgsGeometry #pylint: disable=import-error
from ..plugin_helpers.messages import showMsgBox

def delete_feature(ilayer, ifeature, rightLayerNames, _iface):
    """delete a feature"""
    if ilayer.name() in rightLayerNames:
        ids = []
        ids.append(ifeature.id())
        ilayer.selectByIds(ids)
        ilayer.startEditing()
        reply = showMsgBox('deleteobject')
        if reply == QMessageBox.No:
            ilayer.selectByIds([])
        elif reply == QMessageBox.Yes:
            ilayer.deleteFeature(ifeature.id())
            ilayer.commitChanges()
        return "Done"
    else:
        reply = showMsgBox('noselectedtodelete')
        if reply == QMessageBox.No:
            ilayer.selectByIds([])
            return "Done"
        else:
            return "Retry"

def getfeature_geometry(featGeom, layerType):
    geom = None
    if layerType == 'LineString' and featGeom.wkbType() in [2, 1002, 2002, 3002, -2147483646]:
        geom = QgsGeometry.fromMultiPolylineXY([featGeom.asPolyline()])
    elif layerType == 'LineString' and featGeom.wkbType() in [5, 1005, 2005, 3005]:
        geom = QgsGeometry.fromMultiPolylineXY(featGeom.asMultiPolyline())
    elif layerType == 'Polygon' and featGeom.wkbType() in [3, 1003, 2003, 3003]:
        geom = QgsGeometry.fromMultiPolygonXY([featGeom.asPolygon()])
    elif layerType == 'Polygon' and featGeom.wkbType() in [6, 1006, 2006, 3006]:
        geom = QgsGeometry.fromMultiPolygonXY(featGeom.asMultiPolygon())
    elif layerType == 'Point':
        geom = QgsGeometry.fromPointXY(featGeom.asPoint())
    return geom
