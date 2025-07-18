"""initialize al action for repressief object"""
import os

from qgis.PyQt import uic
import qgis.PyQt.QtWidgets as PQtW
import qgis.PyQt.QtCore as PQtC
import qgis.core as QC

import oiv.helpers.utils_core as UC
import oiv.helpers.utils_gui as UG
import oiv.tools.editFeature as EF
import oiv.tools.stackwidget as SW
import oiv.tools.import_file as IFW
import oiv.repressief_object.oiv_object_tekenen as OTW
import oiv.repressief_object.oiv_create_grid as GW
import oiv.werkvoorraad.oiv_werkvoorraad as OWW
import oiv.helpers.messages as MSG
import oiv.helpers.drawing_helper as DH
import oiv.helpers.constants as PC
import oiv.helpers.qt_helper as QT
import oiv.tools.print as PR
import oiv.helpers.rubberband_helper as RH

from .oiv_object_tekenen import oivObjectTekenWidget

FORM_CLASS, _ = uic.loadUiType(os.path.join(
    os.path.dirname(__file__), PC.OBJECT["objectwidgetui"]))


class oivRepressiefObjectWidget(PQtW.QDockWidget, FORM_CLASS):
    """interactive UI management"""

    attributeform = None
    identifier = None
    snapLayerNames = DH.ROSNAPLAYERS
    tekensymbolenwidget = None
    importwidget = None
    gridWidget = None
    workWidget = None
    workLayout = None
    objectId = None
    printCoverageLayer = None
    legenda = None

    def __init__(self, parent=None, objectId=None, formeleNaam=None):
        super(oivRepressiefObjectWidget, self).__init__(parent)
        self.setupUi(self)
        self.baseWidget = parent
        self.objectId = objectId
        self.iface = parent.iface
        self.canvas = parent.canvas
        self.object_id.setVisible(False)
        self.selectTool = parent.selectTool
        self.polygonSelectTool = parent.polygonSelectTool
        self.pointTool = parent.pointTool
        self.drawTool = parent.drawTool
        self.moveTool = parent.moveTool
        self.identifyTool = parent.identifyTool
        self.initActions()

    def initActions(self):
        """connect the buttons to their actions"""
        self.baseobjectFrame.setVisible(True)
        self.addobjectFrame.setVisible(False)
        self.deleteobjectFrame.setVisible(False)
        self.delete_menu.clicked.connect(self.object_verwijderen)
        self.object_add.clicked.connect(self.object_toevoegen)
        self.object_info.clicked.connect(self.run_objectgegevens_bewerken)
        self.object_bgt.clicked.connect(self.open_bgt_viewer)
        self.terrein_tekenen.clicked.connect(self.run_terrein_toevoegen)
        self.object_draw.clicked.connect(self.run_object_symbolen_tekenen)
        self.object_print.clicked.connect(self.run_print)
        self.create_grid.clicked.connect(self.run_create_grid)
        self.import_drawing.clicked.connect(self.run_import)
        self.object_inventory.clicked.connect(self.run_werkvoorraad)
        self.check_werkvoorraad()

    def check_werkvoorraad(self):
        layerName = 'Werkvoorraad objecten'
        ilayer = UC.getlayer_byname(layerName)
        request = QC.QgsFeatureRequest().setFilterExpression('"id" = ' + str(self.objectId))
        it = ilayer.getFeatures(request)
        if len(list(it)) > 0:
            self.object_inventory.setEnabled(True)
        else:
            self.object_inventory.setEnabled(False)

    def run_objectgegevens_bewerken(self):
        """select bouwlaag on canvas to edit the atrribute form"""
        objectId = self.object_id.text()
        request = QC.QgsFeatureRequest().setFilterExpression('"id" = ' + str(objectId))
        ilayer = UC.getlayer_byname(PC.OBJECT["objectlayername"])
        try:
            ifeature = UC.featureRequest(ilayer, request)
            if ifeature:
                self.edit_attribute(ilayer, ifeature)
        except StopIteration:
            MSG.showMsgBox('no_objectid')

    def open_georeferencer(self):
        UG.set_lengte_oppervlakte_visibility(self.baseWidget, False, False, False, False)
        self.iface.mainWindow().findChildren(PQtW.QAction, 'mActionShowGeoreferencer')[0].trigger()

    def open_bgt_viewer(self):
        """open url based on BGT location, i.v.m. terugmelden"""
        e = self.canvas.extent()
        gemx = (e.xMaximum() + e.xMinimum())/2
        gemy = (e.yMaximum() + e.yMinimum())/2
        url = PC.OBJECT["bgtviewerurl"] + 'geometry.x=' + str(gemx) + '&geometry.y=' + str(gemy) + '&zoomlevel=12'
        UC.open_url(url)

    def run_delete_object(self):
        """delete repressief object"""
        ifeature = None
        ilayer = UC.getlayer_byname(PC.OBJECT["objectlayername"])
        objectId = self.object_id.text()
        request = QC.QgsFeatureRequest().setFilterExpression('"id" = ' + str(objectId))
        ifeature = UC.featureRequest(ilayer, request)
        ilayer.startEditing()
        ilayer.selectByIds([ifeature.id()])
        reply = MSG.showMsgBox('deleteobject')
        if not reply:
            #als "nee" deselecteer alle geselecteerde features
            ilayer.selectByIds([])
        elif reply:
            #als "ja" -> verwijder de feature op basis van het unieke feature id
            ilayer.deleteFeature(ifeature.id())
            ilayer.commitChanges()
            reply = MSG.showMsgBox('deletedobject')
            self.baseobjectFrame.setVisible(True)
            self.deleteobjectFrame.setVisible(False)
            self.baseWidget.handleDoneBtn(False)
            UC.refresh_layers(self.iface)

    def edit_attribute(self, ilayer, ifeature):
        """open het formulier van een feature in een dockwidget, zodat de attributen kunnen worden bewerkt"""
        stackWidget = SW.oivStackWidget(self)
        self.show_subwidget(True, stackWidget)
        #stackWidget.parentWidget = self
        stackWidget.parentWidth = self.width()
        stackWidget.open_feature_form(ilayer, ifeature)
        layerNames = PC.OBJECT["nogeotables"]
        for name in layerNames:
            layer = UC.getlayer_byname(name)
            layer.updateExtents()
        stackWidget.show()
        try: 
            self.selectTool.geomSelected.disconnect(self.edit_attribute)
        except: # pylint: disable=bare-except
            pass

    def control_buttons_addobjectframe(self, terrein, importbtn, grid, georeference, terrein_del):
        self.terrein_tekenen.setEnabled(terrein)
        self.create_grid.setEnabled(grid)
        self.import_drawing.setEnabled(importbtn)
        self.georeferencer.setEnabled(georeference)
        self.terrein_delete.setEnabled(terrein_del)

    def object_toevoegen(self):
        self.baseWidget.done.setVisible(False)
        self.baseWidget.done_png.setVisible(False)
        self.baseobjectFrame.setVisible(False)
        self.addobjectFrame.setVisible(True)
        self.georeferencer.clicked.connect(self.open_georeferencer)
        self.terug_add.clicked.connect(self.object_toevoegen_sluiten)

    def object_verwijderen(self):
        self.baseWidget.done.setVisible(False)
        self.baseWidget.done_png.setVisible(False)
        self.baseobjectFrame.setVisible(False)
        self.deleteobjectFrame.setVisible(True)
        self.terrein_delete.clicked.connect(self.run_delete_terrein)
        self.object_delete.clicked.connect(self.run_delete_object)
        self.terug_delete.clicked.connect(self.object_verwijderen_sluiten)

    def object_toevoegen_sluiten(self):
        self.baseWidget.done.setVisible(True)
        self.baseWidget.done_png.setVisible(True)
        self.baseobjectFrame.setVisible(True)
        self.addobjectFrame.setVisible(False)
        self.georeferencer.clicked.disconnect(self.open_georeferencer)
        UG.set_lengte_oppervlakte_visibility(self.baseWidget, False, False, False, False)
        self.control_buttons_addobjectframe(True, True, True, True, True)
        self.terug_add.clicked.disconnect(self.object_toevoegen_sluiten)

    def object_verwijderen_sluiten(self):
        self.baseWidget.done.setVisible(True)
        self.baseWidget.done_png.setVisible(True)
        self.baseobjectFrame.setVisible(True)
        self.deleteobjectFrame.setVisible(False)
        self.terrein_delete.clicked.disconnect(self.run_delete_terrein)
        self.object_delete.clicked.disconnect(self.run_delete_object)
        self.terug_delete.clicked.disconnect(self.object_verwijderen_sluiten)

    def edit_feature(self):
        self.selectTool.whichConfig = PC.OBJECT["configtable"]
        self.canvas.setMapTool(self.selectTool)
        self.selectTool.geomSelected.connect(self.edit_attribute)

    def run_create_grid(self):
        UG.set_lengte_oppervlakte_visibility(self.baseWidget, False, False, False, False)
        gridWidget = GW.oivGridWidget(self)
        gridWidget.object_id.setText(self.object_id.text())
        self.show_subwidget(True, gridWidget)

    def show_subwidget(self, show, widget=None):
        if show:
            self.baseWidget.tabWidget.setTabVisible(0, False)
            self.baseWidget.tabWidget.addTab(widget, '')
            self.baseWidget.tabWidget.setCurrentIndex(3)
        else:
            self.baseWidget.tabWidget.setTabVisible(0, True)
            self.baseWidget.tabWidget.setCurrentIndex(0)
            self.baseWidget.tabWidget.removeTab(3)

    def run_terrein_toevoegen(self):
        self.control_buttons_addobjectframe(True, False, False, False, False)
        objectId = self.object_id.text()
        possibleSnapFeatures = UC.get_possible_snapFeatures_object(self.snapLayerNames, objectId)
        self.drawTool.parent = self
        self.drawTool.baseWidget = self.baseWidget
        self.drawTool.layer = UC.getlayer_byname(PC.OBJECT["terreinlayername"])
        UG.set_lengte_oppervlakte_visibility(self.baseWidget, True, True, True, True)
        self.drawTool.possibleSnapFeatures = possibleSnapFeatures
        self.drawTool.canvas = self.canvas
        self.drawTool.onGeometryAdded = self.place_object_terrein
        self.drawTool.captureMode = 2
        self.canvas.setMapTool(self.drawTool)

    def run_delete_terrein(self):
        try:
            self.selectTool.geomSelected.disconnect(self.delete)
        except:
            None
        self.control_buttons_addobjectframe(False, False, False, False, True)
        self.selectTool.whichConfig = PC.OBJECT["configtable"]
        self.canvas.setMapTool(self.selectTool)
        self.selectTool.geomSelected.connect(self.delete)

    def delete(self, ilayer, ifeature):
        deleteLayerNames = [PC.OBJECT["objectlayername"], PC.OBJECT["terreinlayername"]]
        reply = EF.delete_feature(ilayer, ifeature, deleteLayerNames, self.iface)
        if reply == 'Retry':
            self.run_delete_terrein()
        self.selectTool.geomSelected.disconnect(self.delete)
        self.control_buttons_addobjectframe(True, True, True, True, True)

    def place_object_terrein(self, points, _dummy):
        """save drawn terrain"""
        layer = UC.getlayer_byname(PC.OBJECT["terreinlayername"])
        if points:
            parentId, childFeature = UC.construct_feature('Polygon', PC.OBJECT["objectlayername"], points, self.object_id.text())
        if parentId is not None:
            buttonCheck = UC.get_attributes(parentId, childFeature, None, None, layer, PC.OBJECT["configtable"])
            if buttonCheck != 'Cancel':
                UC.write_layer(layer, childFeature)
                self.baseWidget.objectModified = True
        layer.commitChanges()
        layer.triggerRepaint()
        UG.set_lengte_oppervlakte_visibility(self.baseWidget, False, False, False, False)
        self.control_buttons_addobjectframe(True, True, True, True, True)

    def run_object_symbolen_tekenen(self):
        if not self.baseWidget.parent.tekenObjectWidget:
            self.baseWidget.parent.tekenObjectWidget = oivObjectTekenWidget(self)
        self.baseWidget.parent.tekenObjectWidget.object_id.setText(self.object_id.text())
        self.baseWidget.parent.tekenObjectWidget.drawbuttonframe.setVisible(True)
        self.show_subwidget(True, self.baseWidget.parent.tekenObjectWidget)

    def run_werkvoorraad(self):
        werkvoorraadWidget = OWW.oivWerkvoorraadWidget(self)
        werkvoorraadWidget.bouwlaagOfObject = 'Object'
        werkvoorraadWidget.initUI()
        self.show_subwidget(True, werkvoorraadWidget)

    def run_print(self):
        self.object_print.setEnabled(False)
        printWhat, reply, self.legenda = PrintDialog.get_print_settings()
        if reply and printWhat == 'polygon':
            self.printCoverageLayer = PR.create_temp_print_layer('object_id')
            self.draw_print_polygon()
        elif reply:
            self.resume_printing('terrein')
        else:
            self.object_print.setEnabled(True)

    def resume_printing(self, byWhichLayer):
        directory = PQtW.QFileDialog().getExistingDirectory()
        if directory != '':
            fileName = self.object_id.text() + '_' + self.formelenaam.text()
            filterString = '"object_id"='+"'{}'".format(self.object_id.text())
            UG.set_layer_substring(filterString, 'object')
            rotation = self.canvas.rotation()
            reply, directory = PR.load_composer(directory, 'object', fileName, byWhichLayer, rotation, self.legenda)
            MSG.showMsgBox(reply, directory)
            UG.set_layer_substring('', 'object')
        if byWhichLayer == 'polygon':
            qinst = QC.QgsProject.instance()
            qinst.removeMapLayer(qinst.mapLayersByName("tempPrintCoverage")[0].id())
        self.iface.actionPan().trigger()
        self.object_print.setEnabled(True)

    def draw_print_polygon(self):
        drawTool = self.baseWidget.drawTool
        drawTool.captureMode = 2
        drawTool.layer = self.printCoverageLayer
        drawTool.canvas = self.canvas
        drawTool.onGeometryAdded = self.place_feature
        self.canvas.setMapTool(drawTool)
        drawTool.baseWidget = self.baseWidget

    def place_feature(self, points, snapAngle):
        """Save and place feature on the canvas"""
        tempFeature = QC.QgsFeature()
        tempFields = self.printCoverageLayer.fields()
        tempFeature.initAttributes(tempFields.count())
        tempFeature.setFields(tempFields)
        geom = QC.QgsGeometry.fromPolygonXY([points])
        tempFeature.setGeometry(geom)
        tempFeature["object_id"] = int(self.object_id.text())
        UC.write_layer(self.printCoverageLayer, tempFeature)
        RH.set_printcoverage_style(self.iface, self.printCoverageLayer)
        self.resume_printing('polygon')

    def run_import(self):
        """initiate import widget"""
        UG.set_lengte_oppervlakte_visibility(self.baseWidget, False, False, False, False)
        importwidget = IFW.oivImportFileWidget(self)
        self.show_subwidget(True, importwidget)

class PrintDialog(PQtW.QDialog):
    def __init__(self, parent=None):
        super(PrintDialog, self).__init__(parent)
        self.setWindowTitle("Repressief object printen")
        self.chkBoxDict = {}
        qlayout = PQtW.QVBoxLayout(self)
        self.qlineA = PQtW.QLabel(self)
        self.qRadioBtnPolygon = PQtW.QRadioButton(self)
        self.qRadioBtnTerrain = PQtW.QRadioButton(self)
        self.qlineA.setText("Selecteer hoe u wilt printen")
        self.qRadioBtnPolygon.setToolTip("Polygoon tekenen")
        self.qRadioBtnPolygon.setText("Polygoon tekenen")
        self.qRadioBtnTerrain.setToolTip("Via terrein")
        self.qRadioBtnTerrain.setText("Via terrein")
        qlayout.addWidget(self.qlineA)
        qlayout.addWidget(self.qRadioBtnPolygon)
        qlayout.addWidget(self.qRadioBtnTerrain)
        self.qlineB = PQtW.QLabel(self)
        self.qlineB.setText("Voeg een legenda toe:")
        qlayout.addWidget(self.qlineB)
        self.cmbBoxLegenda = PQtW.QComboBox(self)
        self.cmbBoxLegenda.addItems([''] + PC.OBJECT["objecttypes"])
        qlayout.addWidget(self.cmbBoxLegenda)
        buttons = PQtW.QDialogButtonBox(
            PQtW.QDialogButtonBox.Ok | PQtW.QDialogButtonBox.Cancel,
            PQtC.Qt.Horizontal, self)
        buttons.accepted.connect(self.accept)
        buttons.rejected.connect(self.reject)
        qlayout.addWidget(buttons)

    def get_checked_radiobutton(self):
        reply = None
        if self.qRadioBtnPolygon.isChecked():
            reply = 'polygon'
        if self.qRadioBtnTerrain.isChecked():
            reply = 'terrein'
        return reply

    @staticmethod
    def get_print_settings(parent=None):
        dialog = PrintDialog(parent)
        result = dialog.exec_()
        return (dialog.get_checked_radiobutton(), result == PQtW.QDialog.Accepted, dialog.cmbBoxLegenda.currentText())