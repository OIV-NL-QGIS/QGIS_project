from qgis.PyQt.QtWidgets import QComboBox, QDialogButtonBox, QLineEdit
from qgis.core import QgsFeature, QgsSpatialIndex, QgsFeatureRequest
from qgis.utils import iface

 
def formOpen(dialog, layer, feature):
    myLayer = layer
    myDialog = dialog
    nameField = []
    nameValidate = []
    try:
        if (feature.geometry()):
            featureGeometry = feature.geometry()
            nameField.append(dialog.findChild(QComboBox, "soort"))
            nameField.append(dialog.findChild(QLineEdit, "omschrijving"))
            nameValidate.append(0)
            nameValidate.append(0)
            okButton = dialog.findChild(QDialogButtonBox, "buttonBox")
            if not (len(nameField[0].currentText()) > 0):
                nameField[0].setStyleSheet("background-color: rgba(255, 107, 107, 150);")
                okButton.setEnabled(False)
            else: 
                nameValidate[0] = 1			
            if not (len(nameField[1].text()) > 0):
                nameField[1].setStyleSheet("background-color: rgba(255, 107, 107, 150);")
                okButton.setEnabled(False)
            else: 
                nameValidate[1] = 1					
            if (feature['bouwlaag_id'] == NULL):
                geom = feature.geometry().asPoint()
                extent = iface.mapCanvas().extent()
                objectenLayer = getVectorLayerByName("Bouwlagen")
                index = QgsSpatialIndex(objectenLayer.getFeatures(QgsFeatureRequest(extent)))
                features = index.nearestNeighbor(geom, 2)
                feature = objectenLayer.getFeatures(QgsFeatureRequest(features[0]))
                featureId = feature.next().id()
                myDialog.changeAttribute("bouwlaag_id", featureId)
            nameField[0].currentIndexChanged.connect(lambda: validate_0(nameField, nameValidate, okButton))
            nameField[1].textChanged.connect(lambda: validate_1(nameField, nameValidate, okButton))
            bnOk = okButton.button(QDialogButtonBox.Ok)
            bnOk.clicked.connect(lambda: applySave(featureGeometry, myLayer, myDialog))
    except:
        pass
		
def applySave(featureGeometry, myLayer, myDialog):
    if (featureGeometry):
        myLayer.commitChanges()
        myLayer.startEditing()
        qgis.utils.iface.actionAddFeature().trigger()
        
def validate_0(nameField, nameValidate, okButton):
    if (len(nameField[0].currentText()) > 0):
        nameField[0].setStyleSheet("")
        nameValidate[0] = 1
    if (sum(nameValidate) == 2):
        okButton.setEnabled(True)

def validate_1(nameField, nameValidate, okButton):
    # Make sure that the name field isn't empty.
    if not (len(nameField[1].text()) > 0):
        nameValidate[1] = 0
        nameField[1].setStyleSheet("background-color: rgba(255, 107, 107, 150);")
    else:
        # Return the form as accpeted to QGIS.
        nameValidate[1] = 1
        nameField[1].setStyleSheet("")
    if (sum(nameValidate) == 2):
        okButton.setEnabled(True)
		
def getVectorLayerByName(layerName):
    layer = None
    layers = QgsProject.instance().mapLayersByName(layername)
    layer = layers[0]
    return (layer)