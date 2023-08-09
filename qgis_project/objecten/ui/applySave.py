from qgis.PyQt.QtWidgets import QDialogButtonBox, QComboBox
from qgis.gui import QgsEditorWidgetWrapper, QgsFilterLineEdit

buttonBoxName = "buttonBox"
 
def formOpen(dialog, layer, feature):

    for wrapper in dialog.findChildren(QgsEditorWidgetWrapper):
        if isinstance(wrapper.widget(), QComboBox):
            wrapper.widget().setStyleSheet("color: rgb(0, 0, 0); background-color: lightgray;")

    comboBoxes = dialog.findChildren(QComboBox)
    for box in comboBoxes:
        box.setStyleSheet("color: rgb(0, 0, 0); background-color: lightgray;")
        
    okButton = dialog.findChild(QDialogButtonBox, buttonBoxName)
    bnOk = okButton.button(QDialogButtonBox.Ok)
    bnOk.clicked.connect(lambda: applySave(layer))
		
def applySave(layer):
    if layer:
        layer.commitChanges()
