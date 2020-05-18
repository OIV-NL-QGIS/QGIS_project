from qgis.PyQt.QtWidgets import QComboBox, QDialogButtonBox, QLineEdit
from qgis.core import QgsFeature, QgsSpatialIndex, QgsFeatureRequest
from qgis.utils import iface
 
def formOpen(dialog, layer, feature):
    myDialog = dialog
    myLayer = layer
    nameField = []
    nameValidate = []
    try:
        nameField.append(myDialog.findChild(QLineEdit, "hoeveelheid"))
        nameField.append(myDialog.findChild(QLineEdit, "omschrijving"))
        nameField.append(myDialog.findChild(QComboBox, "gevaarlijkestof_vnnr_id"))
        nameField[2].setCurrentText('geen vn nummer')
        nameField.append(myDialog.findChild(QComboBox, "eenheid"))
        nameField.append(myDialog.findChild(QComboBox, "toestand"))
        okButton = dialog.findChild(QDialogButtonBox, "buttonBox")
        for i in range(5):
            nameValidate.append(0)
        for i in range(2):
            if not (len(nameField[i + 3].currentText()) > 0):
                nameField[i + 3].setStyleSheet("background-color: rgba(255, 107, 107, 150);")
                okButton.setEnabled(False)
        if not (len(nameField[0].text()) > 0):
            nameField[0].setStyleSheet("background-color: rgba(255, 107, 107, 150);")
            okButton.setEnabled(False)
        if not (len(nameField[1].text()) > 0 or nameField[2].currentText() != ' geen vn nummer'):
            nameField[1].setStyleSheet("background-color: rgba(255, 107, 107, 150);")
            nameField[2].setStyleSheet("background-color: rgba(255, 107, 107, 150);")	
            okButton.setEnabled(False)			
        nameField[0].textChanged.connect(lambda: validate_0(nameField, nameValidate, okButton))
        nameField[1].textChanged.connect(lambda: validate_1(nameField, nameValidate, okButton))
        nameField[2].currentIndexChanged.connect(lambda: validate_1(nameField, nameValidate, okButton))
        nameField[3].currentIndexChanged.connect(lambda: validate_2(nameField, nameValidate, okButton))
        nameField[4].currentIndexChanged.connect(lambda: validate_2(nameField, nameValidate, okButton))
        bnOk = okButton.button(QDialogButtonBox.Ok)	
        bnOk.clicked.connect(lambda: applySaveGVS(myLayer, myDialog))
    except:
        pass
 
def applySaveGVS(myLayer, myDialog):
    myLayer.commitChanges()
    myDialog.save()
	
def validate_0(nameField, nameValidate, okButton):
    if not (len(nameField[0].text()) > 0):
        nameValidate[0] = 0
        nameField[0].setStyleSheet("background-color: rgba(255, 107, 107, 150);")
        okButton.setEnabled(False)
    else:
        nameValidate[0] = 1
        nameField[0].setStyleSheet("")
        if (sum(nameValidate) == 4):
            okButton.setEnabled(True)

def validate_1(nameField, nameValidate, okButton):
    if not (len(nameField[1].text()) > 0 or nameField[2].currentText() != ' geen vn nummer'):
        nameValidate[1] = 0
        nameField[1].setStyleSheet("background-color: rgba(255, 107, 107, 150);")
        nameField[2].setStyleSheet("background-color: rgba(255, 107, 107, 150);")
        okButton.setEnabled(False)
    else:
        nameValidate[1] = 1
        nameField[1].setStyleSheet("")
        nameField[2].setStyleSheet("")
        if (sum(nameValidate) == 4):
            okButton.setEnabled(True)	
	
def validate_2(nameField, nameValidate, okButton):
    for i in range(2):
        if (len(nameField[i + 3].currentText()) > 0):
            nameField[i + 3].setStyleSheet("")
            nameValidate[i + 3] = 1
    if (sum(nameValidate) == 4):
        okButton.setEnabled(True)