import webbrowser
import qgis.PyQt.QtWidgets as PQtW
import qgis.core as QC
from qgis.gui import QgsEditorWidgetWrapper, QgsFilterLineEdit

def formOpen(dialog, layer, feature):
    pushBtn = dialog.findChild(PQtW.QPushButton, "pushButton")
    pushBtn.clicked.connect(lambda: open_url(dialog.findChild(PQtW.QLineEdit, "file_name").text()))

    for wrapper in dialog.findChildren(QgsEditorWidgetWrapper):
        if isinstance(wrapper.widget(), PQtW.QComboBox):
            wrapper.widget().setStyleSheet("color: rgb(0, 0, 0); background-color: lightgray;")

    comboBoxes = dialog.findChildren(PQtW.QComboBox)
    for box in comboBoxes:
        box.setStyleSheet("color: rgb(0, 0, 0); background-color: lightgray;")

    okButton = dialog.findChild(PQtW.QDialogButtonBox, "buttonBox")
    bnOk = okButton.button(PQtW.QDialogButtonBox.Ok)
    bnOk.clicked.connect(lambda: applySave(layer))

def open_url(fileName):
    layer = QC.QgsProject.instance().mapLayersByName('settings')[0]
    request = QC.QgsFeatureRequest().setFilterExpression("\"setting_key\" = 'scenario_base_url'")
    feature = next(layer.getFeatures(request), None)
    print(request, feature)
    if feature:
        fileUrl = feature["setting_value"] + fileName
        print(fileUrl)
        webbrowser.open(fileUrl)

def applySave(layer):
    if layer:
        layer.commitChanges()