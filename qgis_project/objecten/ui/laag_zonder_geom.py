from qgis.PyQt.QtWidgets import QComboBox, QDialogButtonBox, QLineEdit
from qgis.core import QgsFeature, QgsSpatialIndex, QgsFeatureRequest
from qgis.utils import iface
 
myLayer = None
featureGeometry = None
 
def formOpen(dialog, layer, feature):
    global myLayer
    global featureGeometry
    myLayer = layer
    buttonBox = dialog.findChild(QDialogButtonBox, "buttonBox")
    bnOk = buttonBox.button(QDialogButtonBox.Ok)
    bnOk.clicked.connect(applySave)
 
def applySave():
    myLayer.commitChanges()