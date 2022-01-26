import webbrowser
import qgis.PyQt.QtWidgets as PQtW

def formOpen(dialog, layer, feature):
    pushBtn = dialog.findChild(PQtW.QPushButton, "pushButton")
    pushBtn.clicked.connect(lambda: open_url(feature, dialog))
    okButton = dialog.findChild(PQtW.QDialogButtonBox, "buttonBox")
    bnOk = okButton.button(PQtW.QDialogButtonBox.Ok)
    bnOk.clicked.connect(lambda: applySave(layer))

def open_url(feature, dialog):
    fileUrl = dialog.findChild(PQtW.QLineEdit, "file_url").text()
    if fileUrl != '':
        webbrowser.open(fileUrl)

def applySave(layer):
    if layer:
        layer.commitChanges()