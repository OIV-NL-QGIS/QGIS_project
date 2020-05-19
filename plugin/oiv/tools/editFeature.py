
from qgis.PyQt.QtWidgets import QMessageBox
from qgis.core import QgsGeometry

def delete_feature(ilayer, ifeature, rightLayerNames, iface):
    """delete a feature"""
    if ilayer.name() in rightLayerNames:
        ids = []
        ids.append(ifeature.id())
        ilayer.selectByIds(ids)
        ilayer.startEditing()
        reply = QMessageBox.question(iface.mainWindow(), 'Continue?',
                                     "Weet u zeker dat u de geselecteerde feature wilt weggooien?",
                                     QMessageBox.Yes, QMessageBox.No)
        if reply == QMessageBox.No:
            ilayer.selectByIds([])
        elif reply == QMessageBox.Yes:
            ilayer.deleteFeature(ifeature.id())
            ilayer.commitChanges()
        return "Done"
    else:
        reply = QMessageBox.information(iface.mainWindow(), 'Geen tekenlaag!',
                                        "U heeft geen feature op een tekenlaag aangeklikt!"
                                        "Klik a.u.b. op de juiste locatie."
                                        "Weet u zeker dat u iets wilt weggooien?",
                                        QMessageBox.Yes, QMessageBox.No)
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
