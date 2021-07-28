from qgis.PyQt.QtWidgets import QComboBox, QDialogButtonBox
from qgis.core import QgsFeature, QgsSpatialIndex, QgsFeatureRequest, QgsProject
from qgis.utils import iface
 
def formOpen(dialog, layer, feature):
    myLayer = layer
    myDialog = dialog
    nameField = []
    nameValidate = []
    try:
        if feature.geometry():
            featureGeometry = feature.geometry()
            nameField.append(dialog.findChild(QComboBox, "ingang_type_id"))            
            nameValidate.append(0)
            okButton = dialog.findChild(QDialogButtonBox, "buttonBox")
            if not len(nameField[0].currentText()) > 0:
                nameField[0].setStyleSheet("background-color: rgba(255, 107, 107, 150);")
                okButton.setEnabled(False)
            else:
                nameValidate[0] = 1				
            if not feature['bouwlaag_id']:
                geom = feature.geometry().asPoint()
                extent = iface.mapCanvas().extent()
                objectenLayer = getVectorLayerByName("Bouwlagen")
                index = QgsSpatialIndex(objectenLayer.getFeatures(QgsFeatureRequest(extent)))
                features = index.nearestNeighbor(geom, 2)
                feature = objectenLayer.getFeatures(QgsFeatureRequest(features[0]))
                featureId = feature.next().id()
                myDialog.changeAttribute("bouwlaag_id", featureId)
            nameField[0].currentIndexChanged.connect(lambda: validate(nameField, nameValidate, okButton))
            bnOk = okButton.button(QDialogButtonBox.Ok)
            bnOk.clicked.connect(lambda: applySave(featureGeometry, myLayer, myDialog))
    except:
        pass
		
def applySave(featureGeometry, myLayer, myDialog):
    if (featureGeometry):
        myLayer.commitChanges()
        myLayer.startEditing()
        iface.actionAddFeature().trigger()
		
def validate(nameField, nameValidate, okButton):
    for i in range(len(nameField)):
        if len(nameField[i].currentText()) > 0:
            nameField[i].setStyleSheet("")
            nameValidate[i] = 1
    if sum(nameValidate) == 1:
        okButton.setEnabled(True)

def getVectorLayerByName(layerName):
    layer = None
    layers = QgsProject.instance().mapLayersByName(layerName)
    if layers:
        layer = layers[0]
    return layer