from qgis.PyQt.QtWidgets import QComboBox, QDialogButtonBox, QLineEdit
from qgis.core import QgsFeature, QgsSpatialIndex, QgsFeatureRequest
from qgis.utils import iface
 
myLayer = None
featureGeometry = None
 
def formOpen(dialog, layer, feature):
    global myLayer
    global featureGeometry
    myDialog = dialog
    myLayer = layer
    buttonBox = dialog.findChild(QDialogButtonBox, "buttonBox")
    bnOk = buttonBox.button(QDialogButtonBox.Ok)
    bnOk.clicked.connect(lambda: applySave(myLayer, myDialog))

	
def applySave(myLayer, myDialog):
    myLayer.commitChanges()
    myDialog.save()