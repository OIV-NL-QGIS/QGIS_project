from qgis.PyQt.QtWidgets import QDialogButtonBox
from qgis.core import QgsFeature, QgsSpatialIndex, QgsFeatureRequest, QgsProject
from qgis.utils import iface

buttonBoxName = "buttonBox"
parentLayerName = 'Ingang ruimtelijk'
keyAttribute = 'ingang_id'
 
def formOpen(dialog, layer, feature):
    okButton = dialog.findChild(QDialogButtonBox, buttonBoxName)
    if not feature[keyAttribute]:
        geom = feature.geometry().asPoint()
        extent = iface.mapCanvas().extent()
        objectenLayer = getVectorLayerByName(parentLayerName)
        index = QgsSpatialIndex(objectenLayer.getFeatures(QgsFeatureRequest(extent)))
        features = index.nearestNeighbor(geom, 2)
        feature = objectenLayer.getFeatures(QgsFeatureRequest(features[0]))
        featureId = feature.next().id()
        dialog.changeAttribute(keyAttribute, featureId)
    bnOk = okButton.button(QDialogButtonBox.Ok)
    bnOk.clicked.connect(lambda: applySave(layer))
		
def applySave(layer):
    if layer:
        layer.commitChanges()

def getVectorLayerByName(layerName):
    layer = None
    layers = QgsProject.instance().mapLayersByName(layerName)
    if layers:
        layer = layers[0]
    return layer