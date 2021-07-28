from qgis.PyQt.QtWidgets import QDialogButtonBox

buttonBoxName = "buttonBox"
parentLayerName = 'gevaarlijkestof'
keyAttribute = 'gevaarlijkestof_id'
 
def formOpen(dialog, layer, feature):
    okButton = dialog.findChild(QDialogButtonBox, buttonBoxName)
    bnOk = okButton.button(QDialogButtonBox.Ok)
    bnOk.clicked.connect(lambda: applySave(layer))
		
def applySave(layer):
    if layer:
        layer.commitChanges()
