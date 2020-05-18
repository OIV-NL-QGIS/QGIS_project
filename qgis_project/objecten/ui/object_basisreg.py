from qgis.PyQt.QtWidgets import QComboBox, QPushButton, QLineEdit
from qgis.core import QgsFeature, QgsSpatialIndex, QgsFeatureRequest
from qgis.utils import iface
 
def formOpen(dialog, layer, feature):
    myDialog = dialog
    myLayer = layer
    nameField = []
    nameValidate = []
    #try:
    if feature.geometry():
        featureGeometry = feature.geometry()
        nameField.append(dialog.findChild(QLineEdit, "formelenaam"))
        okButton = dialog.findChild(QPushButton, "opslaan")
        nameValidate.append(0)
        if not (len(nameField[0].text()) > 0):
            nameField[0].setStyleSheet("background-color: rgba(255, 107, 107, 150);")
            okButton.setEnabled(False)
        else:
            nameValidate[0] = 1
        nameField[0].textChanged.connect(lambda: validate_0(nameField, nameValidate, okButton))
        #bnOk = okButton.button(QDialogButtonBox.Ok)
        okButton.clicked.connect(lambda: applySaveObject(featureGeometry, myLayer, myDialog))
    #except:
        #pass
 
def applySaveObject(featureGeometry, myLayer, myDialog):
    if (featureGeometry):
        myLayer.commitChanges()
        qgis.utils.iface.actionAddFeature().trigger()
		
def validate_0(nameField, nameValidate, okButton):
    # Make sure that the name field isn't empty.
    if not (len(nameField[0].text()) > 0):
        nameValidate[0] = 0
        nameField[0].setStyleSheet("background-color: rgba(255, 107, 107, 150);")
        okButton.setEnabled(False)
    else:
        # Return the form as accpeted to QGIS.
        nameValidate[0] = 1
        nameField[0].setStyleSheet("")
        if (sum(nameValidate) == 1):
            okButton.setEnabled(True)

def getVectorLayerByName(layerName):
    layer = None
    layers = QgsProject.instance().mapLayersByName(layername)
    layer = layers[0]
    return (layer)