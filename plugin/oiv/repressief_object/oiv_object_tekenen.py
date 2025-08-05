"""drawing class for repressief object"""
import os

from qgis.PyQt import uic
import qgis.PyQt.QtWidgets as PQtW
from qgis.PyQt.QtGui import QIcon
import qgis.PyQt.QtCore as PQtC
import qgis.core as QC

import oiv.helpers.utils_core as UC
import oiv.helpers.utils_gui as UG
import oiv.tools.stackwidget as SW
import oiv.tools.editFeature as EF
import oiv.helpers.drawing_helper as DW
import oiv.helpers.qt_helper as QT
import oiv.helpers.configdb_helper as CH
import oiv.helpers.constants as PC
import oiv.werkvoorraad.db_helper as DH
import oiv.helpers.messages as MSG

FORM_CLASS, _ = uic.loadUiType(os.path.join(
    os.path.dirname(__file__), PC.OBJECT["tekenwidgetui"]))


class oivObjectTekenWidget(PQtW.QDockWidget, FORM_CLASS):

    repressiefobjectwidget = None
    parent = None
    drawLayer = None
    identifier = None
    parentLayerName = None
    drawLayerType = None
    editableLayerNames = []
    moveLayerNames = []
    snapSymbols = []
    tabWidget = None
    anchorPoints = None

    def __init__(self, parent=None):
        super(oivObjectTekenWidget, self).__init__(parent)
        self.setupUi(self)
        self.parent = parent
        self.baseWidget = parent.baseWidget
        self.selectTool = parent.selectTool
        self.polygonSelectTool = parent.polygonSelectTool
        self.iface = parent.iface
        self.canvas = parent.canvas
        self.object_id.setText(parent.object_id.text())
        self.formelenaam.setText(parent.formelenaam.text())
        self.initUI()

    def initUI(self):
        """intitiate the UI elemets on the widget"""
        UG.set_lengte_oppervlakte_visibility(self.baseWidget, False, False, False, False)
        self.object_id.setVisible(False)
        self.drawbuttonframe.setVisible(True)
        self.move.clicked.connect(self.run_move_point)
        self.identify.clicked.connect(self.run_edit_tool)
        self.select.clicked.connect(self.run_select_tool)
        self.delete_f.clicked.connect(self.run_delete_tool)
        self.pan.clicked.connect(self.activatePan)
        self.baseWidget.done.setVisible(False)
        self.baseWidget.done_png.setVisible(False)
        self.baseWidget.filter_objecten.setVisible(False)
        self.baseWidget.label_filter.setVisible(False)
        self.baseWidget.info_of_interest.setVisible(False)
        self.baseWidget.label_info_of_interest.setVisible(False)
        self.terug.clicked.connect(self.close_object_tekenen_show_base)
        actionList = PC.ACTIONDICTOBJECT
        actionList, self.editableLayerNames, self.moveLayerNames, self.snapSymbols, self.anchorPoints = UG.get_actions(PC.OBJECT["configtable"], actionList)
        self.initActions(actionList)

    def initActions(self, actionList):
        """connect all the buttons to the action"""
        cnti = 0
        cntj = 0
        sizePolicy = PQtW.QSizePolicy(PQtW.QSizePolicy.Policy.Minimum, PQtW.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        self.tabWidget = self.findChild(PQtW.QTabWidget, 'tabWidgetObject')
        for tabblad, categorieen in actionList.items():
            widget = PQtW.QWidget()
            self.tabWidget.addTab(widget, tabblad)
            qlayout = PQtW.QGridLayout()
            for categorie, actions in categorieen.items():
                if actions:
                    label = PQtW.QLabel()
                    qlayout.addWidget(label, cnti, cntj, 1, 5)
                    label.setText(categorie)
                cnti += 1
                cntj = 0
                for action in actions:
                    runLayerName = action[0]
                    buttonNr = action[1]
                    buttonName = str(action[2].lower())
                    buttonIcon = action[3]
                    landOfReg = action[4]
                    strButton = PQtW.QPushButton()
                    if landOfReg == 'landelijk':
                        strButton.setIcon(QIcon(":/plugins/oiv/config_files/svg/" + buttonIcon + ".svg"))
                    else:
                        strButton.setIcon(QIcon(":/plugins/oiv/config_files/png/" + buttonIcon + ".png"))
                    strButton.setToolTip(buttonName)
                    sizePolicy.setHeightForWidth(strButton.sizePolicy().hasHeightForWidth())
                    strButton.setSizePolicy(sizePolicy)
                    strButton.setIconSize(PQtC.QSize(28, 28))
                    qlayout.addWidget(strButton, cnti, cntj)
                    if strButton:
                        #set tooltip per buttonn
                        strButton.setToolTip(buttonName)
                        strButton.setStyleSheet("background-color: #e0e0e0")
                        #geef met de signal ook mee welke knop er is geklikt -> nr
                        strButton.clicked.connect(lambda dummy='dummyvar', rlayer=runLayerName, who=buttonNr: self.run_tekenen(dummy, rlayer, who))
                    if cntj == 4:
                        cntj = 0
                        cnti += 1
                    else:
                        cntj += 1
                cnti += 1
                cntj = 0
            spacerItem = PQtW.QSpacerItem(0, 0, PQtW.QSizePolicy.Policy.Minimum, PQtW.QSizePolicy.Policy.Expanding)
            qlayout.addItem(spacerItem, cnti, cntj+1)
            widget.setLayout(qlayout)

    def close_object_tekenen_show_base(self):
        self.activatePan()
        try:
            self.selectTool.geomSelected.disconnect()
        except:
            pass
        self.close()
        self.parent.show_subwidget(False)
        self.drawbuttonframe.setVisible(False)
        self.baseWidget.done.setVisible(True)
        self.baseWidget.done_png.setVisible(True)
        self.baseWidget.filter_objecten.setVisible(True)
        self.baseWidget.label_filter.setVisible(True)
        self.baseWidget.info_of_interest.setVisible(True)
        self.baseWidget.label_info_of_interest.setVisible(True)
        self.baseWidget.cadframe.setVisible(False)
        self.baseWidget.tabWidget.setTabVisible(0, True)
        #self.terug.clicked.disconnect(self.close_object_tekenen_show_base)
        del self

    def run_edit_tool(self):
        """activate the edit feature tool"""
        try:
            self.selectTool.geomSelected.disconnect()
        except:
            pass
        self.selectTool.possibleSnapFeatures = self.get_snap_features()
        self.selectTool.layer = UC.getlayer_byname(PC.OBJECT["objectlayername"])
        self.selectTool.whichConfig = PC.OBJECT["configtable"]
        self.canvas.setMapTool(self.selectTool)
        self.selectTool.geomSelected.connect(self.edit_attribute)

    def run_select_tool(self):
        """activate the select feature tool"""
        self.polygonSelectTool.canvas = self.canvas
        self.polygonSelectTool.onGeometryAdded = self.select_features
        self.polygonSelectTool.parent = self
        self.canvas.setMapTool(self.polygonSelectTool)

    def get_snap_features(self):
        layerNamesTup = CH.get_childlayers_ob_point()
        snapLayerNames = [i[0] for i in layerNamesTup]
        objectId = self.object_id.text()
        possibleSnapFeatures = UC.get_possible_snapFeatures_object(snapLayerNames, objectId)
        return possibleSnapFeatures

    def select_features(self, points):
        geom = QC.QgsGeometry.fromPolygonXY([points])
        bbox = geom.boundingBox()
        req = QC.QgsFeatureRequest()
        filterRect = req.setFilterRect(bbox)
        layerNamesTup = CH.get_chidlayers_ob()
        layerNames = [i[0] for i in layerNamesTup]
        if PC.OBJECT["objectlayername"] in layerNames:
            layerNames.remove(PC.OBJECT["objectlayername"])
        for layerName in layerNames:
            layer = UC.getlayer_byname(layerName)
            if UC.is_layer_visible(layer):
                feats = layer.getFeatures(filterRect)
                for feat in feats:
                    if feat.geometry().within(geom):
                        layer.select(feat.id())
        reply, ok = MultiEditDialog.get_multi_edit_action()
        if reply == 'delete':
            self.delete_multi(layerNames)
        if reply == 'move':
            self.run_move_point(True)
        if reply == 'rotate':
            self.run_move_point(True)

    def delete_multi(self, layerNames):
        reply = MSG.showMsgBox('deleteobject')
        for layerName in layerNames:
            layer = UC.getlayer_byname(layerName)
            if reply:
                DH.temp_delete_feature_multi(layer, 'Object')
            else:
                layer.selectByIds([])

    def select_feature(self, ilayer, ifeature):
        """catch emitted signal from selecttool"""
        self.iface.setActiveLayer(ilayer)
        ids = []
        ids.append(ifeature.id())
        ilayer.selectByIds(ids)
        ilayer.startEditing()
        self.selectTool.geomSelected.disconnect()
        self.run_select_tool()

    def activatePan(self):
        """trigger pan function to loose other functions"""
        self.iface.actionPan().trigger()
        self.parent.moveTool.possibleSnapFeatures = []
        self.selectTool.possibleSnapFeatures = []

    def run_delete_tool(self):
        """activate delete feature tool"""
        try:
            self.selectTool.geomSelected.disconnect()
        except:
            pass
        self.selectTool.possibleSnapFeatures = self.get_snap_features()
        self.selectTool.layer = UC.getlayer_byname(PC.OBJECT["objectlayername"])
        self.selectTool.whichConfig = PC.OBJECT["configtable"]
        self.canvas.setMapTool(self.selectTool)
        self.selectTool.geomSelected.connect(self.delete)

    def delete(self, ilayer, ifeature):
        """delete a feature"""
        reply = DH.temp_delete_feature(ilayer, ifeature, 'Object', self.editableLayerNames)
        self.baseWidget.objectModified = True
        #reply = EF.delete_feature(ilayer, ifeature, self.editableLayerNames, self.iface)
        if reply == 'Retry':
            self.run_delete_tool()
        self.selectTool.geomSelected.disconnect()
        self.run_delete_tool()

    #open het formulier van een feature in een dockwidget, zodat de attributen kunnen worden bewerkt
    def edit_attribute(self, ilayer, ifeature):
        if ilayer.name() != PC.OBJECT["objectlayername"]:
            stackWidget = SW.oivStackWidget(self)
            self.show_subwidget(True, stackWidget)
            stackWidget.parentWidget = self
            stackWidget.baseWidget = self.baseWidget
            stackWidget.isTekenen = True
            stackWidget.open_feature_form(ilayer, ifeature)
            self.baseWidget.objectModified = True
            stackWidget.show()
            self.selectTool.geomSelected.disconnect()
        self.run_edit_tool()

    def show_subwidget(self, show, widget=None):
        if show:
            self.baseWidget.tabWidget.setTabVisible(3, False)
            self.baseWidget.tabWidget.addTab(widget, '')
            self.baseWidget.tabWidget.setCurrentIndex(4)
        else:
            self.baseWidget.tabWidget.setTabVisible(3, True)
            self.baseWidget.tabWidget.setCurrentIndex(3)
            self.baseWidget.tabWidget.removeTab(4)

    #om te verschuiven/roteren moeten de betreffende lagen op bewerken worden gezet
    def run_move_point(self, multi=False):
        """om te verschuiven/roteren moeten de betreffende lagen op bewerken worden gezet"""
        for lyrName in self.moveLayerNames:
            moveLayer = UC.getlayer_byname(lyrName)
            moveLayer.startEditing()
        self.parent.moveTool.possibleSnapFeatures = self.get_snap_features()
        self.parent.moveTool.layer = UC.getlayer_byname(PC.OBJECT["objectlayername"])
        self.parent.moveTool.onMoved = self.stop_moveTool
        self.parent.moveTool.multi = multi
        self.canvas.setMapTool(self.parent.moveTool)

    #na de actie verschuiven/bewerken moeten de betreffende lagen opgeslagen worden en bewerken moet worden uitgezet.
    def stop_moveTool(self, rotation, geom_old, geom_new, multi):
        """na de actie verschuiven/bewerken moeten de betreffende lagen opgeslagen worden en bewerken moet worden uitgezet"""
        if multi:
            layerNamesTup = CH.get_chidlayers_ob()
            layerNames = [i[0] for i in layerNamesTup]
            layerNames.remove(PC.OBJECT["objectlayername"])
            for layerName in layerNames:
                layer = UC.getlayer_byname(layerName)
                layer.startEditing()
                if rotation:
                    field_idx = layer.fields().indexOf("rotatie")
                    for feat in layer.selectedFeatures():
                        if field_idx != -1:
                            layer.changeAttributeValue(feat.id(), field_idx, rotation)
                if geom_new:
                    for feat in layer.selectedFeatures():
                        geom = feat.geometry()
                        deltaX = geom_new.asPoint().x() - geom_old.asPoint().x()
                        deltaY = geom_new.asPoint().y() - geom_old.asPoint().y()
                        geom.translate(deltaX , deltaY)
                        layer.changeGeometry(feat.id(), geom)
                layer.commitChanges()
                layer.reload()
        else:
            for lyrName in self.moveLayerNames:
                moveLayer = UC.getlayer_byname(lyrName)
                moveLayer.commitChanges()
                moveLayer.reload()
            self.run_move_point()

    def run_tekenen(self, _dummy, runLayer, featureId):
        #welke pictogram is aangeklikt en wat is de bijbehorende tekenlaag
        self.identifier = featureId
        self.drawLayer = UC.getlayer_byname(runLayer)
        self.drawLayerType = UC.check_layer_type(self.drawLayer)
        self.parentLayerName = CH.get_parentlayer_ob(runLayer)
        objectId = self.object_id.text()
        possibleSnapFeatures = UC.get_possible_snapFeatures_object(DW.ROSNAPLAYERS, objectId)
        if self.drawLayerType == "Point":
            pointTool = self.parent.pointTool
            pointTool.snapPt = None
            pointTool.snapping = False
            pointTool.startRotate = False
            pointTool.possibleSnapFeatures = possibleSnapFeatures
            if self.identifier in self.snapSymbols:
                pointTool.snapping = True
            pointTool.layer = self.drawLayer
            self.canvas.setMapTool(pointTool)
            UG.set_lengte_oppervlakte_visibility(self.baseWidget, False, False, False, False)
            pointTool.onGeometryAdded = self.place_feature
        else:
            drawTool = self.parent.drawTool
            if self.drawLayerType == "LineString":
                drawTool.captureMode = 1
                UG.set_lengte_oppervlakte_visibility(self.baseWidget, True, True, False, True)
            else:
                drawTool.captureMode = 2
                UG.set_lengte_oppervlakte_visibility(self.baseWidget, True, True, True, True)
            drawTool.layer = self.drawLayer
            drawTool.possibleSnapFeatures = possibleSnapFeatures
            drawTool.canvas = self.canvas
            drawTool.onGeometryAdded = self.place_feature
            self.canvas.setMapTool(drawTool)
            drawTool.baseWidget = self.baseWidget

    def place_feature(self, points, snapAngle):
        parentId = None
        translateGeom = False
        self.iface.setActiveLayer(self.drawLayer)
        if self.drawLayerType == 'Point':
            if self.identifier in self.anchorPoints["anchorpointtop"] or self.identifier in self.anchorPoints["anchorpointbottom"]:
                result = CH.get_type_layer_ob(self.drawLayer.name())
                typeLayerName = result[0]
                typeName = result[1]
                typeLayer = UC.getlayer_byname(typeLayerName)
                request = QC.QgsFeatureRequest().setFilterExpression('"{}" = '.format(typeName) + "'{}'".format(self.identifier))
                ifeature = UC.featureRequest(typeLayer, request)
                size = ifeature["size_object_middel"]
                translateGeom = True
        if points:
            parentId, childFeature = UC.construct_feature(self.drawLayerType, self.parentLayerName, points, self.object_id.text())
            if translateGeom:
                if self.identifier in self.anchorPoints["anchorpointtop"]:
                    delta = -0.5
                else:
                    delta = 0.5
                childFeature = UC.move_point(childFeature, delta * size, snapAngle)
        if parentId is not None:
            buttonCheck = UC.get_attributes(parentId, childFeature, snapAngle, self.identifier, self.drawLayer, PC.OBJECT["configtable"])
            if buttonCheck != 'Cancel':
                UC.write_layer(self.drawLayer, childFeature)
                self.baseWidget.objectModified = True
        self.run_tekenen('dummy', self.drawLayer.name(), self.identifier)
        UG.set_lengte_oppervlakte_visibility(self.baseWidget, False, False, False, False)

class MultiEditDialog(PQtW.QDialog):
    def __init__(self, parent=None):
        super(MultiEditDialog, self).__init__(parent)
        self.setWindowTitle("Multi verwijderen, roteren of verplaatsen")
        qlayout = PQtW.QVBoxLayout(self)
        self.qlineA = PQtW.QLabel(self)
        self.qRadioBtnMove = PQtW.QRadioButton(self)
        self.qRadioBtnRotate = PQtW.QRadioButton(self)
        self.qRadioBtnDelete = PQtW.QRadioButton(self)
        self.qlineA.setText("Selecteer de knop met wat u wilt doen")
        self.qRadioBtnMove.setToolTip("Verplaatsen")
        self.qRadioBtnMove.setText("Verplaatsen")
        self.qRadioBtnRotate.setToolTip("Draaien")
        self.qRadioBtnRotate.setText("Draaien")
        self.qRadioBtnDelete.setToolTip("Verwijderen")
        self.qRadioBtnDelete.setText("Verwijderen")
        self.qRadioBtnMove.setIcon(QIcon(':/plugins/oiv/config_files/png/move.png'))
        self.qRadioBtnRotate.setIcon(QIcon(':/plugins/oiv/config_files/png/rotate.png'))
        self.qRadioBtnDelete.setIcon(QIcon(':/plugins/oiv/config_files/png/delete.png'))
        self.qRadioBtnMove.setIconSize(PQtC.QSize(32,32))
        self.qRadioBtnRotate.setIconSize(PQtC.QSize(32,32))
        self.qRadioBtnDelete.setIconSize(PQtC.QSize(32,32))
        qlayout.addWidget(self.qlineA)
        qlayout.addWidget(self.qRadioBtnMove)
        qlayout.addWidget(self.qRadioBtnRotate)
        qlayout.addWidget(self.qRadioBtnDelete)
        buttons = PQtW.QDialogButtonBox(
            PQtW.QDialogButtonBox.Ok | PQtW.QDialogButtonBox.Cancel,
            PQtC.Qt.Horizontal, self)
        buttons.accepted.connect(self.accept)
        buttons.rejected.connect(self.reject)
        qlayout.addWidget(buttons)

    def get_checked_radiobutton(self):
        reply = None
        if self.qRadioBtnMove.isChecked():
            reply = 'move'
        if self.qRadioBtnRotate.isChecked():
            reply = 'rotate'
        if self.qRadioBtnDelete.isChecked():
            reply = 'delete'
        return reply

    @staticmethod
    def get_multi_edit_action(parent=None):
        dialog = MultiEditDialog(parent)
        result = dialog.exec_()
        return (dialog.get_checked_radiobutton(), result == PQtW.QDialog.Accepted)