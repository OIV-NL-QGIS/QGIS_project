"""create new repressief object"""
import os
import json
from datetime import datetime

from qgis.PyQt import uic
from qgis.PyQt.QtGui import QColor
import qgis.PyQt.QtWidgets as PQtW
import qgis.PyQt.QtCore as PQtC
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
    tableData = None
    tableColumns = ['id', 'modified_at', 'operatie', 'status', 'soort', 'brontabel', 'modified_by']
    tableHeaders = ['id', 'Datum', 'Operatie', 'Status', 'Soort', 'Tabel', 'Wie', 'laagnaam']
    statusColumnIndex = 3
    layernameColumnIndex = 7

    def __init__(self, parent=None, objectId=None, bron=None, bronTbl=None):
        """Constructor."""
        super(oivWerkvoorraadWidget, self).__init__(parent)
        self.setupUi(self)
        self.parent = parent
        self.iface = parent.iface
        self.canvas = parent.canvas
        self.baseWidget = parent.baseWidget
        self.polygonSelectTool = parent.polygonSelectTool

    def initUI(self):
        if self.bouwlaagOfObject == 'Object':
            self.naam.setText(self.parent.formelenaam.text())
            self.identifier.setText(self.parent.object_id.text())
        elif self.bouwlaagOfObject == 'Bouwlaag':
            self.naam.setText(self.parent.comboBox.currentText())
            self.identifier.setText(self.parent.pand_id.text())
        self.btn_opslaan.clicked.connect(self.execute_selected_rows)
        self.btn_terug.clicked.connect(self.close_werkvoorraad)
        titleBar = QT.getTitleBar()
        self.baseWidget.done.setVisible(False)
        self.baseWidget.done_png.setVisible(False)
        self.baseWidget.filter_objecten.setVisible(False)
        self.baseWidget.label_filter.setVisible(False)
        self.baseWidget.info_of_interest.setVisible(False)
        self.baseWidget.label_info_of_interest.setVisible(False)
        self.setTitleBarWidget(titleBar)
        self.select_by_polygon.clicked.connect(self.run_select)
        self.tbl_werkvoorraad.cellClicked.connect(self.select_on_canvas)
        self.tbl_werkvoorraad.itemSelectionChanged.connect(self.on_selection_changed)
        self.fr_conflict.setVisible(False)
        self.identifier.setVisible(False)
        self.naam.setVisible(False)
        self.fr_verwerk.setVisible(True)
        self.getData()

    def getData(self):
        self.tableData = []
        objectId = self.identifier.text()
        if self.bouwlaagOfObject == 'Object':
            layerNames = PC.OBJECT["werkvoorraadlayers"]
            request = QC.QgsFeatureRequest().setFilterExpression('"object_id" = ' + objectId)
        else:
            layerNames = PC.PAND["werkvoorraadlayers"]
            objectIds = self.getbouwlaag_ids(objectId)
            request = QC.QgsFeatureRequest().setFilterExpression('"bouwlaag_id" in ({})'.format(objectIds))
        for layerName in layerNames:
            ilayer = UC.getlayer_byname(layerName)
            if ilayer:
                it = ilayer.getFeatures(request)
                for feat in it:
                    data = []
                    for fieldName in self.tableColumns:
                        if fieldName == 'modified_at':
                            data.append(feat[fieldName].toString('yyyy-MM-dd HH:mm'))
                        else:
                            data.append(feat[fieldName])
                    data.append(layerName)
                    self.tableData.append(data)
        self.populate_table(self.tableData)
        self.get_other_mods(objectId)

    def populate_table(self, entries):
        if len(entries):
            self.tbl_werkvoorraad.setRowCount(len(entries))
            self.tbl_werkvoorraad.setColumnCount(len(entries[0]))
            for i, row in enumerate(entries):
                for j, col in enumerate(row):
                    item = PQtW.QTableWidgetItem(str(col))
                    self.tbl_werkvoorraad.setItem(i, j, item)
                    if j == self.statusColumnIndex:
                        if str(col) == "CONFLICT":
                            item.setBackground(QColor("#FFF3CD"))
                        elif str(col) == "OPEN":
                            item.setBackground(QColor("#D4EDDA"))
            self.tbl_werkvoorraad.setHorizontalHeaderLabels(self.tableHeaders)
        self.tbl_werkvoorraad.setSelectionBehavior(PQtW.QAbstractItemView.SelectRows)
        self.tbl_werkvoorraad.setColumnHidden(0, True);
        self.tbl_werkvoorraad.setColumnHidden(5, True);
        self.tbl_werkvoorraad.setColumnHidden(self.layernameColumnIndex, True);

    def run_select(self):
        self.polygonSelectTool.canvas = self.canvas
        self.polygonSelectTool.onGeometryAdded = self.select_features
        self.polygonSelectTool.parent = self
        self.canvas.setMapTool(self.polygonSelectTool)
        
    def select_on_canvas(self, row, col):
        if self.bouwlaagOfObject == 'Object':
            layerNames = PC.OBJECT["werkvoorraadlayers"]
        else:
            layerNames = PC.PAND["werkvoorraadlayers"]
        for layerName in layerNames:
            layer = UC.getlayer_byname(layerName)
            layer.removeSelection()
        recordId = self.tbl_werkvoorraad.item(row, 0).text()
        layerName = self.tbl_werkvoorraad.item(row, self.layernameColumnIndex).text()
        layer = UC.getlayer_byname(layerName)
        layer.selectByExpression('"id" = {}'.format(recordId))
        
    def select_features(self, points):
        index = []
        geom = QC.QgsGeometry.fromPolygonXY([points])
        bbox = geom.boundingBox()
        if self.bouwlaagOfObject == 'Object':
            layerNames = PC.OBJECT["werkvoorraadlayers"]
        else:
            layerNames = PC.PAND["werkvoorraadlayers"]
        for layerName in layerNames:
            if 'Hulp' not in layerName:
                layer = UC.getlayer_byname(layerName)
                layer.selectByRect(bbox)
                for feat in layer.selectedFeatures():
                    if not geom.intersects(feat.geometry()):
                        layer.deselect(feat.id())
                    else:
                        indx = self.get_index(feat, layerName)
                        index.append(indx)
        self.select_in_table(index)

    def get_index(self, feat, layerName):
        data = []
        for fieldName in self.tableColumns:
            if fieldName == 'modified_at':
                data.append(feat[fieldName].toString('yyyy-MM-dd HH:mm'))
            else:
                data.append(feat[fieldName])
        data.append(layerName)
        return self.tableData.index(data)
        
    def select_in_table(self, index):
        model = self.tbl_werkvoorraad.model()
        selection = PQtC.QItemSelection()
        for i in index:
            model_index = model.index(i,0)
            selection.select(model_index, model_index)
        mode = PQtC.QItemSelectionModel.Select | PQtC.QItemSelectionModel.Rows
        tblSelection = self.tbl_werkvoorraad.selectionModel()
        tblSelection.select(selection, mode)
        
    def getbouwlaag_ids(self, bagId):
        ids = []
        layerName = 'Bouwlagen'
        ilayer = UC.getlayer_byname(layerName)
        request = QC.QgsFeatureRequest().setFilterExpression('"pand_id" = ' + "'{}'".format(bagId))
        it = ilayer.getFeatures(request)
        for feat in it:
            ids.append(str(feat["id"]))
        return ','.join(ids)
        
    def get_other_mods(self, objectId):
        layout = self.fr_wijzigingen.layout()
        if self.bouwlaagOfObject == 'Object':
            bouwlagen = WDH.get_bouwlagen(objectId)
            if bouwlagen:
                for bouwlaag in bouwlagen:
                    labelText = 'Bouwlaag: {}'.format(str(bouwlaag))
                    label = PQtW.QLabel()
                    label.setText(labelText)
                    layout.addWidget(label)
        else:
            objectMods = WDH.check_object_mods(objectId)
            if objectMods:
                labelText = 'Het terrein / repressief object'
                label = PQtW.QLabel()
                label.setText(labelText)
                layout.addWidget(label)

    def execute_selected_rows(self):
        accepted_ids = []
        open_records, conflict_records = self.update_selection()
        accepted = self.rb_accept.isChecked()

        # Eerst alle normale werkvoorraad verwerken
        if open_records:
            for record in open_records:
                WDH.verwerk_werkvoorraad(record["tabel"], record["id"], accepted)
                accepted_ids.append(record["id"])
            if conflict_records:
                MSG.showMsgBox("werkvoorraad_conflict_overgeslagen")
            self.remove_from_table(accepted_ids)
            return

        # Geen open records -> conflictafhandeling
        if len(conflict_records) == 1:
            record = conflict_records[0]
            conflict_actie = ("OIV" if self.rb_oiv.isChecked() else "MOBIEL")
            WDH.verwerk_werkvoorraad(record["tabel"], record["id"], accepted, conflict_actie)
            self.remove_from_table([record["id"]])
            self.clear_conflict()
            return

        self.canvas.refresh()

        if len(conflict_records) > 1:
            MSG.showMsgBox("werkvoorraad_meerdere_conflicten")

    def update_selection(self):
        open_records = []
        conflict_records = []
        indexes = self.tbl_werkvoorraad.selectionModel().selectedRows()
        layer_col = self.layernameColumnIndex
        status_col = self.statusColumnIndex

        for index in indexes:
            row = index.row()
            werkvoorraad_id = int(self.tbl_werkvoorraad.item(row, 0).text())
            laagnaam = self.tbl_werkvoorraad.item(row, layer_col).text()
            status = self.tbl_werkvoorraad.item(row, status_col).text()
            werkvoorraad_tabel = PC.WERKVOORRAAD["tablelayertranslate"].get(laagnaam)

            if not werkvoorraad_tabel:
                continue

            record = {
                "tabel": werkvoorraad_tabel,
                "id": werkvoorraad_id
            }

            if status == "CONFLICT":
                conflict_records.append(record)
            else:
                open_records.append(record)

        return open_records, conflict_records

    def remove_from_table(self, ids):
        rows = []
        for row in range(self.tbl_werkvoorraad.rowCount()):
            werkvoorraad_id = int(self.tbl_werkvoorraad.item(row, 0).text())
            if werkvoorraad_id in ids:
                rows.append(row)
        # Van onder naar boven verwijderen
        for row in sorted(rows, reverse=True):
            self.tbl_werkvoorraad.removeRow(row)

    def on_selection_changed(self):
        self.fr_conflict.setVisible(False)
        indexes = self.tbl_werkvoorraad.selectionModel().selectedRows()

        # Alleen één geselecteerde regel
        if len(indexes) != 1:
            self.clear_conflict()
            return

        row = indexes[0].row()
        status = self.tbl_werkvoorraad.item(row, self.statusColumnIndex).text()
        # Alleen bij conflicten
        if status != "CONFLICT":
            self.clear_conflict()
            return
        werkvoorraad_id = int(self.tbl_werkvoorraad.item(row, 0).text())
        self.fr_conflict.setVisible(True)
        self.load_conflict(werkvoorraad_id)


    def load_conflict(self, werkvoorraad_id):
        layer_name = self.tbl_werkvoorraad.item(self.tbl_werkvoorraad.currentRow(), self.layernameColumnIndex).text()
        layer = UC.getlayer_byname(layer_name)
        request = QC.QgsFeatureRequest().setFilterExpression(f'"id" = {werkvoorraad_id}')
        feature = next(layer.getFeatures(request), None)

        if not feature:
            self.clear_conflict()
            return

        conflict_data = feature["conflict_data"]["oiv"]
        modified_at = feature["modified_at"]
        oiv_datum_gewijzigd = conflict_data["oiv"]["oiv_datum_gewijzigd"]

        self.mobiel_datum_gewijzigd.setText(modified_at.toString('yyyy-MM-dd HH:mm'))
        oiv_dt = datetime.fromisoformat(oiv_datum_gewijzigd)
        oiv_fmt = oiv_dt.strftime("%Y-%m-%d %H:%M")
        self.oiv_datum_gewijzigd.setText(oiv_fmt)

        if not conflict_data:
            self.clear_conflict()
            return

        if isinstance(conflict_data, str):
            conflict_data = json.loads(conflict_data)
        self.populate_conflict_table(conflict_data)

        if self.geometry_changed(conflict_data):
            self.show_conflict_geometry(conflict_data)
        else:
            self.clear_conflict_geometry()


    def populate_conflict_table(self, conflict):
        verschillen = []
        oiv = conflict.get("oiv", {})
        mobiel = conflict.get("mobiel", {})
        keys = sorted(set(oiv.keys()) | set(mobiel.keys()))

        for key in sorted(keys):
            oiv_value = oiv.get(key)
            mobiel_value = mobiel.get(key)
            if oiv_value != mobiel_value:
                verschillen.append((key, oiv_value, mobiel_value))

        self.conflict_table.setRowCount(len(verschillen))
        self.conflict_table.setColumnCount(3)

        for row, (key, oiv_value, mobiel_value) in enumerate(verschillen):

            values = [
                key,
                str(oiv_value) if oiv_value is not None else "",
                str(mobiel_value) if mobiel_value is not None else ""
            ]

            for col, value in enumerate(values):
                item = PQtW.QTableWidgetItem(value)
                self.conflict_table.setItem(row, col, item)


    def clear_conflict(self):
        self.clear_conflict_geometry()
        self.conflict_table.clearContents()
        self.conflict_table.setRowCount(0)
        self.fr_conflict.setVisible(False)


    def close_werkvoorraad(self):
        self.clear_conflict()
        self.fr_conflict.setVisible(False)
        self.btn_opslaan.clicked.disconnect()
        self.btn_terug.clicked.disconnect()
        self.baseWidget.done.setVisible(True)
        self.baseWidget.done_png.setVisible(True)
        self.baseWidget.filter_objecten.setVisible(True)
        self.baseWidget.label_filter.setVisible(True)
        self.baseWidget.info_of_interest.setVisible(True)
        self.baseWidget.label_info_of_interest.setVisible(True)
        self.baseWidget.cadframe.setVisible(False)
        self.baseWidget.tabWidget.setTabVisible(1, True)
        self.close()
        self.parent.show_subwidget(False)
        del self


    def show_conflict_geometry(self, conflict_data):
        # Oude conflictweergave verwijderen
        self.clear_conflict_geometry()

        if not conflict_data:
            return

        oiv = conflict_data.get("oiv")
        mobiel = conflict_data.get("mobiel")

        if not oiv or not mobiel:
            return

        # Geometrieën ophalen
        oiv_geom_json = oiv.get("geom")
        mobiel_geom_json = mobiel.get("geom")

        if not oiv_geom_json or not mobiel_geom_json:
            return

        # GeoJSON -> QgsGeometry
        oiv_geom = self.json_to_geometry(oiv_geom_json)
        mobiel_geom = self.json_to_geometry(mobiel_geom_json)

        # Memory layers maken
        self.conflict_oiv_layer = self.create_memory_layer(oiv_geom, "Conflict OIV")
        self.conflict_mobiel_layer = self.create_memory_layer(mobiel_geom, "Conflict Mobiel")

        # Toevoegen aan project
        QC.QgsProject.instance().addMapLayer(self.conflict_oiv_layer)
        QC.QgsProject.instance().addMapLayer(self.conflict_mobiel_layer)

        # Styling
        self.style_conflict_layer(self.conflict_oiv_layer, "oiv")
        self.style_conflict_layer(self.conflict_mobiel_layer, "mobiel")


    def geometry_changed(self, conflict_data):
        return (conflict_data["oiv"]["geom"] != conflict_data["mobiel"]["geom"])


    def create_memory_layer(self, geom, name):
        geom_type = QC.QgsWkbTypes.geometryType(geom.wkbType())

        if geom_type == QC.QgsWkbTypes.PointGeometry:
            uri = "Point?crs=EPSG:28992"
        elif geom_type == QC.QgsWkbTypes.LineGeometry:
            uri = "LineString?crs=EPSG:28992"
        elif geom_type == QC.QgsWkbTypes.PolygonGeometry:
            uri = "Polygon?crs=EPSG:28992"
        else:
            raise Exception(f"Onbekend geometrie type: {geom.wkbType()}")
        layer = QC.QgsVectorLayer(uri, name, "memory")
        provider = layer.dataProvider()
        feature = QC.QgsFeature()
        feature.setGeometry(geom)
        provider.addFeature(feature)
        layer.updateExtents()
        return layer

    def json_to_geometry(self, geom_json):
        return QC.QgsGeometry.fromWkt(
            QC.QgsJsonUtils.geometryFromGeoJson(
                json.dumps(geom_json)
            ).asWkt()
        )

    def style_conflict_layer(self, layer, versie):
        symbol = layer.renderer().symbol()
        if versie == "oiv":
            kleur = QColor("#0066CC")
        else:
            kleur = QColor("#CC0000")
        symbol.setColor(kleur)
        symbol.setOpacity(0.8)
        geom_type = layer.geometryType()
        if geom_type == QC.QgsWkbTypes.PointGeometry:
            symbol.setSize(5)  # grootte in mm
        elif geom_type == QC.QgsWkbTypes.LineGeometry:
            symbol.setWidth(1.5)  # lijndikte in mm
        elif geom_type == QC.QgsWkbTypes.PolygonGeometry:
            symbol.symbolLayer(0).setStrokeColor(kleur)
            symbol.symbolLayer(0).setFillColor(QColor(kleur.red(), kleur.green(), kleur.blue(), 50))
        layer.triggerRepaint()

    def clear_conflict_geometry(self):
        project = QC.QgsProject.instance()
        if hasattr(self, "conflict_oiv_layer") and self.conflict_oiv_layer:
            if project.mapLayer(self.conflict_oiv_layer.id()):
                project.removeMapLayer(self.conflict_oiv_layer.id())
            self.conflict_oiv_layer = None

        if hasattr(self, "conflict_mobiel_layer") and self.conflict_mobiel_layer:
            if project.mapLayer(self.conflict_mobiel_layer.id()):
                project.removeMapLayer(self.conflict_mobiel_layer.id())
            self.conflict_mobiel_layer = None