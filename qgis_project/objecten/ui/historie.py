from qgis.PyQt.QtWidgets import QComboBox, QDialogButtonBox, QLineEdit
from qgis.core import QgsFeature, QgsSpatialIndex, QgsFeatureRequest
from qgis.utils import iface

def formOpen(dialog, layer, feature):
    myDialog = dialog
    myLayer = layer
    nameField = []
    nameValidate = []
    try:
        nameField.append(myDialog.findChild(QComboBox, "teamlid_behandeld_id"))
        nameField.append(myDialog.findChild(QComboBox, "teamlid_afgehandeld_id"))
        nameField.append(myDialog.findChild(QComboBox, "status"))
        nameField.append(myDialog.findChild(QComboBox, "aanpassing"))
        nameField.append(myDialog.findChild(QComboBox, "matrix_code_id"))
        okButton = dialog.findChild(QDialogButtonBox, "buttonBox")
        for i in range(5):
            nameValidate.append(0)
        for i in range(len(nameField)):
            if not (len(nameField[i].currentText()) > 0):
                nameField[i].setStyleSheet("background-color: rgba(255, 107, 107, 150);")
                okButton.setEnabled(False)
            else:
                nameValidate[i] = 1
        nameField[0].currentIndexChanged.connect(lambda: validate_1(nameField, nameValidate, okButton))
        nameField[1].currentIndexChanged.connect(lambda: validate_1(nameField, nameValidate, okButton))
        nameField[2].currentIndexChanged.connect(lambda: validate(nameField, nameValidate, okButton))
        nameField[3].currentIndexChanged.connect(lambda: validate(nameField, nameValidate, okButton))
        nameField[4].currentIndexChanged.connect(lambda: validate(nameField, nameValidate, okButton))
        bnOk = okButton.button(QDialogButtonBox.Ok)	
        bnOk.clicked.connect(lambda: applySave(myLayer, myDialog))
    except:
        pass
	
def applySave(myLayer, myDialog):
    myLayer.commitChanges()
    myDialog.save()
	
def validate(nameField, nameValidate, okButton):
    for i in range(len(nameField)-2):
        if (len(nameField[i+2].currentText()) > 0):
            nameField[i+2].setStyleSheet("")
            nameValidate[i+2] = 1
    if (sum(nameValidate) == 4):
        okButton.setEnabled(True)
		
def validate_1(nameField, nameValidate, okButton):
    if not (len(nameField[0].currentText()) > 0 or len(nameField[1].currentText()) > 0):
        nameValidate[1] = 0
        nameField[0].setStyleSheet("background-color: rgba(255, 107, 107, 150);")
        nameField[1].setStyleSheet("background-color: rgba(255, 107, 107, 150);")
        okButton.setEnabled(False)
    else:
        nameValidate[1] = 1
        nameField[0].setStyleSheet("")
        nameField[1].setStyleSheet("")
        if (sum(nameValidate) == 4):
            okButton.setEnabled(True)