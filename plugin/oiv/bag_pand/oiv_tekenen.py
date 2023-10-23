"""draw items on pand"""
import os

from qgis.PyQt import uic
import qgis.PyQt.QtCore as PQtC
import qgis.PyQt.QtWidgets as PQtW

import oiv.helpers.utils_core as UC
import oiv.helpers.utils_gui as UG
import oiv.tools.stackwidget as SW
import oiv.tools.editFeature as EF
import oiv.helpers.drawing_helper as DW
import oiv.helpers.configdb_helper as CH
import oiv.helpers.constants as PC
import oiv.helpers.qt_helper as QT
import oiv.werkvoorraad.db_helper as DH

FORM_CLASS, _ = uic.loadUiType(os.path.join(
    os.path.dirname(__file__), PC.PAND["tekenwidgetui"]))

class oivTekenWidget(PQtW.QDockWidget, FORM_CLASS):
    """Organize all draw features on the map"""

    identifier = None
    parentLayerName = None
    drawLayerType = None
    drawLayer = None
    editableLayerNames = []
    moveLayerNames = []

    def __init__(self, parent=None):
        """Constructor."""
        super(oivTekenWidget, self).__init__(parent)
        self.setupUi(self)
        self.parent = parent
        self.baseWidget = parent.baseWidget
        self.iface = parent.iface
        self.canvas = parent.canvas
        self.selectTool = parent.selectTool
        self.bouwlaag.setText(str(parent.comboBox.currentText()))
        self.pand_id.setText(parent.pand_id.text())
        self.initUI()

    def initUI(self):
        """intitiate the UI elemets on the widget"""
        UG.set_lengte_oppervlakte_visibility(self.baseWidget, False, False, False, False)
        self.pand_id.setVisible(False)
        self.drawbuttonframe.setVisible(True)
        self.move.clicked.connect(self.run_move_point)
        #connect buttons to the action
        self.identify.clicked.connect(self.run_edit_tool)
        self.select.clicked.connect(self.run_select_tool)
        self.delete_f.clicked.connect(self.run_delete_tool)
        self.terug.clicked.connect(self.close_bouwlaag_tekenen_show_base)
        self.pan.clicked.connect(self.activatePan)
        self.baseWidget.done.setVisible(False)
        self.baseWidget.done_png.setVisible(False)
        self.baseWidget.filter_objecten.setVisible(False)
        self.baseWidget.label_filter.setVisible(False)
        self.baseWidget.info_of_interest.setVisible(False)
        self.baseWidget.label_info_of_interest.setVisible(False)
        actionList, self.editableLayerNames, self.moveLayerNames = UG.get_actions(PC.PAND["configtable"])
        self.initActions(actionList)

    def initActions(self, actionList):
        """connect all the buttons to the action"""
        for lyr in actionList:
            for action in lyr:
                runLayerName = action[0]
                buttonNr = action[1]
                buttonName = str(action[2].lower())
                strButton = self.findChild(PQtW.QPushButton, buttonName)
                if strButton:
                    #set tooltip per buttonn
                    strButton.setToolTip(buttonName)
                    #geef met de signal ook mee welke knop er is geklikt -> nr
                    strButton.clicked.connect(lambda dummy='dummyvar', rlayer=runLayerName, who=buttonNr: self.run_tekenen(dummy, rlayer, who))

    def run_edit_tool(self):
        """activate the edit feature tool"""
        try:
            self.selectTool.geomSelected.disconnect()
        except:
            pass
        self.selectTool.whichConfig = PC.PAND["configtable"]
        self.selectTool.expectedLayerName = None
        self.canvas.setMapTool(self.selectTool)
        self.selectTool.geomSelected.connect(self.edit_attribute)

    def run_select_tool(self):
        """activate the select feature tool"""
        try:
            self.selectTool.geomSelected.disconnect()
        except:
            pass
        self.canvas.setMapTool(self.selectTool)
        self.selectTool.expectedLayerName = None
        self.selectTool.geomSelected.connect(self.select_feature)

    def select_feature(self, ilayer, ifeature):
        """catch emitted signal from selecttool"""
        self.iface.setActiveLayer(ilayer)
        ids = []
        ids.append(ifeature.id())
        ilayer.selectByIds(ids)
        ilayer.startEditing()
        self.selectTool.geomSelected.disconnect()
        self.run_select_tool()

    def run_delete_tool(self):
        """activate delete feature tool"""
        try:
            self.selectTool.geomSelected.disconnect()
        except:
            pass
        self.selectTool.whichConfig = PC.PAND["configtable"]
        self.canvas.setMapTool(self.selectTool)
        self.selectTool.expectedLayerName = None
        self.selectTool.geomSelected.connect(self.delete)

    def delete(self, ilayer, ifeature):
        """delete a feature"""
        reply = DH.temp_delete_feature(ilayer, ifeature, 'Bouwlaag', self.editableLayerNames)
        #reply = EF.delete_feature(ilayer, ifeature, self.editableLayerNames, self.iface)
        if reply == 'Retry':
            self.run_delete_tool()
        self.selectTool.geomSelected.disconnect()
        self.run_delete_tool()

    def edit_attribute(self, ilayer, ifeature):
        """open het formulier van een feature in een dockwidget, zodat de attributen kunnen worden bewerkt"""
        if ilayer.name() != PC.OBJECT["objectlayername"]:
            stackWidget = SW.oivStackWidget(self)
            self.show_subwidget(True, stackWidget)
            stackWidget.parentWidget = self
            stackWidget.baseWidget = self.baseWidget
            stackWidget.isTekenen = True
            stackWidget.open_feature_form(ilayer, ifeature)
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

    def run_move_point(self):
        """om te verschuiven/roteren moeten de betreffende lagen op bewerken worden gezet"""
        for lyrName in self.moveLayerNames:
            moveLayer = UC.getlayer_byname(lyrName)
            moveLayer.startEditing()
        self.parent.moveTool.onMoved = self.stop_moveTool
        self.canvas.setMapTool(self.parent.moveTool)

    def stop_moveTool(self):
        """na de actie verschuiven/bewerken moeten de betreffende lagen opgeslagen worden en bewerken moet worden uitgezet"""
        for lyrName in self.moveLayerNames:
            moveLayer = UC.getlayer_byname(lyrName)
            moveLayer.commitChanges()
            moveLayer.reload()
        self.run_move_point()

    def run_tekenen(self, _dummy, runLayer, feature_id):
        """activate the right draw action"""
        #welke pictogram is aangeklikt en wat is de bijbehorende tekenlaag
        snapLayerNames = []
        self.identifier = feature_id
        self.drawLayer = UC.getlayer_byname(runLayer)
        self.drawLayerType = UC.check_layer_type(self.drawLayer)
        self.parentLayerName = CH.get_parentlayer_bl(runLayer)
        objectId = self.pand_id.text()
        #aan welke lagen kan worden gesnapt?
        baglayerName = PC.bagpand_layername()
        snapLayerNames = DW.BLSNAPLAYERS
        if baglayerName not in snapLayerNames:
            snapLayerNames.append(baglayerName)
        possibleSnapFeatures = UC.get_possible_snapFeatures_bouwlaag(snapLayerNames, objectId)
        if self.drawLayerType == "Point":
            pointTool = self.parent.pointTool
            pointTool.snapPt = None
            pointTool.snapping = False
            pointTool.startRotate = False
            pointTool.possibleSnapFeatures = possibleSnapFeatures
            if self.identifier in DW.BLSNAPSYMBOLS:
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
        """Save and place feature on the canvas"""
        parentId = None
        self.iface.setActiveLayer(self.drawLayer)
        objectId = self.pand_id.text()
        if points:
            parentId, childFeature = UC.construct_feature(self.drawLayerType, self.parentLayerName, points, objectId)
        if parentId is not None:
            buttonCheck = UC.get_attributes(parentId, childFeature, snapAngle, self.identifier, self.drawLayer, PC.PAND["configtable"])
            if buttonCheck != 'Cancel':
                UC.write_layer(self.drawLayer, childFeature)
        self.run_tekenen('dummy', self.drawLayer.name(), self.identifier)

    def activatePan(self):
        """trigger pan function to loose other functions"""
        self.iface.actionPan().trigger()

    def close_bouwlaag_tekenen_show_base(self):
        """destroy and close self"""
        self.move.clicked.disconnect()
        self.identify.clicked.disconnect()
        self.select.clicked.disconnect()
        self.delete_f.clicked.disconnect()
        try:
            self.selectTool.geomSelected.disconnect()
        except:
            pass
        for widget in self.children():
            if isinstance(widget, PQtW.QPushButton):
                try:
                    widget.clicked.disconnect()
                except: # pylint: disable=bare-except
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
        self.terug.clicked.connect(self.close_bouwlaag_tekenen_show_base)
        del self
