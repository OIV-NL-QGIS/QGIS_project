from qgis.PyQt.QtWidgets import QDialogButtonBox, QLineEdit
 
def formOpen(dialog, layer, feature):
    myLayer = layer
    myDialog = dialog
    featureGeometry = feature.geometry()
    buttonBox = dialog.findChild(QDialogButtonBox, "buttonBox")
    bnOk = buttonBox.button(QDialogButtonBox.Ok)
    bnOk.clicked.connect(lambda: applySave(featureGeometry, myLayer))
 
def applySave(featureGeometry, myLayer):
    if (featureGeometry):
        myLayer.commitChanges()