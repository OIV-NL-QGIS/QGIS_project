from qgis.PyQt.QtWidgets import QComboBox, QDialogButtonBox, QLineEdit
from qgis.core import QgsFeature, QgsSpatialIndex, QgsFeatureRequest
from qgis.utils import iface
 
myLayer = None
featureGeometry = None
 
def formOpen(dialog, layer, feature):
    global myLayer
    global featureGeometry
    myLayer = layer
    try:
        if (feature.geometry()):
            featureGeometry = feature.geometry()
            geom = feature.geometry().asPointXY()
            extent = iface.mapCanvas().extent()
            objectenLayer = getVectorLayerByName("Lokaties")
            index = QgsSpatialIndex(objectenLayer.getFeatures(QgsFeatureRequest(extent)))
            features = index.nearestNeighbor(geom, 2)
            feature = objectenLayer.getFeatures(QgsFeatureRequest(features[0]))
            featureId = feature.next().id()
            dialog.changeAttribute("wo_lokatie_id", featureId)
            buttonBox = dialog.findChild(QDialogButtonBox, "buttonBox")
            bnOk = buttonBox.button(QDialogButtonBox.Ok)
            bnOk.clicked.connect(applySave)
    except:
        pass
 
def applySave():
    if (featureGeometry):
        myLayer.commitChanges()
        myLayer.startEditing()

def getVectorLayerByName(layerName):
    layer = None
    layers = QgsProject.instance().mapLayersByName(layername)
    layer = layers[0]
    return (layer)