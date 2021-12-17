"""create new repressief object"""
import os

from qgis.PyQt import uic
import qgis.PyQt.QtWidgets as PQtW
import qgis.core as QC

import oiv.helpers.utils_core as UC
import oiv.helpers.qt_helper as QT
import oiv.helpers.messages as MSG
import oiv.helpers.configdb_helper as CH
import oiv.helpers.constants as PC
import oiv.werkvoorraad.db_helper as WDH

FORM_CLASS, _ = uic.loadUiType(os.path.join(
    os.path.dirname(__file__), "oiv_werkvoorraad_widget.ui"))


class oivWerkvoorraadWidget(PQtW.QDockWidget, FORM_CLASS):

    bouwlaagOfObject = None
    drawLayer = None
    tableColumns = ['id', 'operatie', 'symbol_name', 'brontabel']

    def __init__(self, parent=None, objectId=None, bron=None, bronTbl=None):
        """Constructor."""
        super(oivWerkvoorraadWidget, self).__init__(parent)
        self.setupUi(self)
        self.parent = parent
        self.iface = parent.iface
        self.canvas = parent.canvas

    def initUI(self):
        if self.bouwlaagOfObject == 'Object':
            self.naam.setText(self.parent.formelenaam.text())
            self.identifier.setText(self.parent.object_id.text())
        elif self.bouwlaagOfObject == 'Bouwlaag':
            self.naam.setText(self.parent.comboBox.currentText())
            self.identifier.setText(self.parent.pand_id.text())
        self.btn_opslaan.clicked.connect(self.execute_selected_rows)
        self.btn_terug.clicked.connect(self.close_werkvoorraad)
        self.helpBtn, self.floatBtn, titleBar = QT.getTitleBar()
        self.setTitleBarWidget(titleBar)
        self.helpBtn.clicked.connect(lambda: UC.open_url(PC.HELPURL["objectnieuwhelp"]))
        self.floatBtn.clicked.connect(lambda: self.setFloating(True))
        self.fr_verwerk.setVisible(True)
        self.getData()

    def getData(self):
        tableData = []
        layerNames = PC.OBJECT["werkvoorraadlayers"]
        objectId = self.identifier.text()
        if self.bouwlaagOfObject == 'Object':
            request = QC.QgsFeatureRequest().setFilterExpression('"object_id" = ' + objectId)
        else:
            request = QC.QgsFeatureRequest().setFilterExpression('"bouwlaag_id" = ' + objectId)
        for layerName in layerNames:
            ilayer = UC.getlayer_byname(layerName)
            it = ilayer.getFeatures(request)
            for feat in it:
                data = []
                for fieldName in self.tableColumns:
                    data.append(feat[fieldName])
                data.append(layerName)
                tableData.append(data)
        self.populate_table(tableData)
        self.get_other_mods(objectId)
        
    def get_other_mods(self, objectId): 
        bouwlagen = WDH.get_bouwlagen(objectId)
        layout = self.fr_wijzigingen.layout()
        if bouwlagen:
            for bouwlaag in bouwlagen:
                labelText = 'Bouwlaag: {}'.format(str(bouwlaag))
                label = PQtW.QLabel()
                label.setText(labelText)
                layout.addWidget(label)

    def execute_selected_rows(self):
        executableFeatures = []
        indexes = self.tbl_werkvoorraad.selectionModel().selectedRows()
        for index in indexes:
            recordId = self.tbl_werkvoorraad.item(index.row(), 0).text()
            layerName = self.tbl_werkvoorraad.item(index.row(), 4).text()
            ilayer = UC.getlayer_byname(layerName)
            request = QC.QgsFeatureRequest().setFilterExpression('"id" = ' + recordId)
            ifeature = UC.featureRequest(ilayer, request)
            executableFeatures.append([ifeature, ilayer])
        if self.rb_accept.isChecked():
            WDH.execute_queries(executableFeatures, ilayer, True)
        else:
            WDH.execute_queries(executableFeatures, ilayer, False)
        self.remove_from_table(indexes)

    def remove_from_table(self, indexes):
        for index in indexes:                                      
            self.tbl_werkvoorraad.removeRow(index.row()) 

    def populate_table(self, entries):
        if len(entries):
            self.tbl_werkvoorraad.setRowCount(len(entries))
            self.tbl_werkvoorraad.setColumnCount(len(entries[0]))
            for i, row in enumerate(entries):
                for j, col in enumerate(row):
                    item = PQtW.QTableWidgetItem(str(col))
                    self.tbl_werkvoorraad.setItem(i, j, item)
            self.tbl_werkvoorraad.setHorizontalHeaderLabels(['id', 'Operatie', 'Type', 'Tabel', 'layerName'])
        self.tbl_werkvoorraad.setSelectionBehavior(PQtW.QAbstractItemView.SelectRows)

    def close_werkvoorraad(self):
        self.btn_opslaan.clicked.disconnect()
        self.btn_terug.clicked.disconnect()
        self.helpBtn.clicked.disconnect()
        self.floatBtn.clicked.disconnect()
        self.close()
        self.parent.show()
        del self

