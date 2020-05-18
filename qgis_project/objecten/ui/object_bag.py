from qgis.PyQt.QtWidgets import QComboBox, QDialogButtonBox, QLineEdit, QSpinBox
from qgis.core import QgsFeature, QgsSpatialIndex, QgsFeatureRequest
from qgis.utils import iface
 
def formOpen(dialog, layer, feature):
    myDialog = dialog
    myLayer = layer
    nameField = []
    nameValidate = []
    #test = dialog.findChild(QDateTimeEdit, "datum_geldig_vanaf")
    #test_date = feature["datum_geldig_vanaf"]
    #test.setDateTime(test_date)
    #try:
    if feature.geometry():
        featureGeometry = feature.geometry()
        nameField.append(dialog.findChild(QLineEdit, "formelenaam"))
        nameField.append(dialog.findChild(QSpinBox, "laagstebouw"))
        nameField.append(dialog.findChild(QSpinBox, "hoogstebouw"))
        okButton = dialog.findChild(QDialogButtonBox, "buttonBox")
        for i in range(3):
            nameValidate.append(0)
        if not (len(nameField[0].text()) > 0):
            nameField[0].setStyleSheet("background-color: rgba(255, 107, 107, 150);")
            okButton.setEnabled(False)
        else:
            nameValidate[0] = 1
        if not (nameField[1].value() <= nameField[2].value()):
            nameValidate[1] = 0
            nameValidate[2] = 0
            nameField[1].setStyleSheet("background-color: rgba(255, 107, 107, 150);")
            nameField[2].setStyleSheet("background-color: rgba(255, 107, 107, 150);")
            okButton.setEnabled(False)
        else:
            nameValidate[1] = 1
            nameValidate[2] = 1
        nameField[0].textChanged.connect(lambda: validate_0(nameField, nameValidate, okButton))
        nameField[1].valueChanged.connect(lambda: validate_1(nameField, nameValidate, okButton))
        nameField[2].valueChanged.connect(lambda: validate_1(nameField, nameValidate, okButton))
        if (feature['pand_id'] == NULL):
            geom = feature.geometry().asPoint()
            extent = iface.mapCanvas().extent()
            objectenLayer = getVectorLayerByName("BAG panden")
            index = QgsSpatialIndex(objectenLayer.getFeatures(QgsFeatureRequest(extent)))
            features = index.nearestNeighbor(geom, 2)
            feature = objectenLayer.getFeatures(QgsFeatureRequest(features[0])).next()
            attrs = feature.attributes()
            myDialog.changeAttribute("pand_id", attrs[1])
        bnOk = okButton.button(QDialogButtonBox.Ok)
        bnOk.clicked.connect(lambda: applySaveObject(featureGeometry, myLayer, myDialog))
    #except:
        #pass
 
def applySaveObject(featureGeometry, myLayer, myDialog):
    if (featureGeometry):
        myLayer.commitChanges()
        myLayer.startEditing()
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
        if (sum(nameValidate) == 3):
            okButton.setEnabled(True)

def validate_1(nameField, nameValidate, okButton):
    # Make sure that the name field isn't empty.
    if not (nameField[1].value() <= nameField[2].value()):
        nameValidate[1] = 0
        nameValidate[2] = 0
        nameField[1].setStyleSheet("background-color: rgba(255, 107, 107, 150);")
        nameField[2].setStyleSheet("background-color: rgba(255, 107, 107, 150);")
        okButton.setEnabled(False)
    else:
        # Return the form as accpeted to QGIS.
        nameValidate[1] = 1
        nameValidate[2] = 1
        nameField[1].setStyleSheet("")
        nameField[2].setStyleSheet("")
        if (sum(nameValidate) == 3):
            okButton.setEnabled(True)

def getVectorLayerByName(layerName):
    layer = None
    layers = QgsProject.instance().mapLayersByName(layername)
    layer = layers[0]
    return (layer)