"""draw items on pand"""
import os

import qgis.PyQt as PQt #pylint: disable=import-error
import qgis.PyQt.QtCore as PQtC #pylint: disable=import-error
import qgis.PyQt.QtWidgets as PQtW #pylint: disable=import-error

import oiv.tools.utils_core as UC
import oiv.tools.utils_gui as UG
import oiv.tools.stackwidget as SW
import oiv.tools.editFeature as EF
import oiv.plugin_helpers.drawing_helper as DW
import oiv.plugin_helpers.configdb_helper as CH
import oiv.plugin_helpers.plugin_constants as PC

FORM_CLASS, _ = PQt.uic.loadUiType(os.path.join(
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
        self.iface = parent.iface
        self.canvas = parent.canvas
        self.selectTool = parent.selectTool
        self.bouwlaag.setText(str(parent.comboBox.currentText()))
        self.pand_id.setText(parent.pand_id.text())
        self.initUI()

    def initUI(self):
        """intitiate the UI elemets on the widget"""
        UG.set_lengte_oppervlakte_visibility(self, False, False, False, False)
        self.pand_id.setVisible(False)
        #connect buttons to the action
        self.move.clicked.connect(self.run_move_point)
        self.identify.clicked.connect(self.run_edit_tool)
        self.select.clicked.connect(self.run_select_tool)
        self.delete_f.clicked.connect(self.run_delete_tool)
        self.pan.clicked.connect(self.activatePan)
        self.terug.clicked.connect(self.close_teken_show_object)
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

    def activatePan(self):
        """trigger pan function to loose other functions"""
        self.iface.actionPan().trigger()

    def run_edit_tool(self):
        """activate the edit feature tool"""
        try:
            self.selectTool.geomSelected.disconnect()
        except: # pylint: disable=bare-except
            pass
        self.selectTool.whichConfig = PC.PAND["configtable"]
        self.canvas.setMapTool(self.selectTool)
        self.selectTool.geomSelected.connect(self.edit_attribute)

    def run_select_tool(self):
        """activate the select feature tool"""
        try:
            self.selectTool.geomSelected.disconnect()
        except: # pylint: disable=bare-except
            pass
        self.canvas.setMapTool(self.selectTool)
        self.selectTool.geomSelected.connect(self.select_feature)

    def select_feature(self, ilayer, ifeature):
        """catch emitted signal from selecttool"""
        self.iface.setActiveLayer(ilayer)
        ids = []
        ids.append(ifeature.id())
        ilayer.selectByIds(ids)
        ilayer.startEditing()
        self.selectTool.geomSelected.disconnect(self.select_feature)

    def run_delete_tool(self):
        """activate delete feature tool"""
        try:
            self.selectTool.geomSelected.disconnect()
        except: # pylint: disable=bare-except
            pass
        self.selectTool.whichConfig = PC.PAND["configtable"]
        self.canvas.setMapTool(self.selectTool)
        self.selectTool.geomSelected.connect(self.delete)

    def delete(self, ilayer, ifeature):
        """delete a feature"""
        reply = EF.delete_feature(ilayer, ifeature, self.editableLayerNames, self.iface)
        if reply == 'Retry':
            self.run_run_delete_tool()
        self.selectTool.geomSelected.disconnect(self.delete)

    def edit_attribute(self, ilayer, ifeature):
        """open het formulier van een feature in een dockwidget, zodat de attributen kunnen worden bewerkt"""
        stackWidget = SW.oivStackWidget()
        self.iface.addDockWidget(PQtC.Qt.RightDockWidgetArea, stackWidget)
        stackWidget.parentWidget = self
        stackWidget.open_feature_form(ilayer, ifeature)
        self.close()
        stackWidget.show()
        self.selectTool.geomSelected.disconnect(self.edit_attribute)
        self.run_edit_tool()

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
        self.activatePan()

    def run_tekenen(self, _dummy, runLayer, feature_id):
        """activate the right draw action"""
        #welke pictogram is aangeklikt en wat is de bijbehorende tekenlaag
        self.identifier = feature_id
        self.drawLayer = UC.getlayer_byname(runLayer)
        self.drawLayerType = UC.check_layer_type(self.drawLayer)
        self.parentLayerName = CH.get_parentlayer_bl(runLayer)
        objectId = self.pand_id.text()
        #aan welke lagen kan worden gesnapt?
        possibleSnapFeatures = UC.get_possible_snapFeatures_bouwlaag(DW.BLSNAPLAYERS, objectId)
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
            UG.set_lengte_oppervlakte_visibility(self, False, False, False, False)
            pointTool.onGeometryAdded = self.place_feature
        else:
            drawTool = self.parent.drawTool
            if self.drawLayerType == "LineString":
                drawTool.captureMode = 1
                UG.set_lengte_oppervlakte_visibility(self, True, True, False, True)
            else:
                drawTool.captureMode = 2
                UG.set_lengte_oppervlakte_visibility(self, True, True, True, True)
            drawTool.layer = self.drawLayer
            drawTool.possibleSnapFeatures = possibleSnapFeatures
            drawTool.canvas = self.canvas
            drawTool.onGeometryAdded = self.place_feature
            self.canvas.setMapTool(drawTool)
            drawTool.parent = self

    def place_feature(self, points, snapAngle):
        """Save and place feature on the canvas"""
        parentId = None
        self.iface.setActiveLayer(self.drawLayer)
        if points:
            parentId, childFeature = UC.construct_feature(self.drawLayerType, self.parentLayerName, points, None, self.iface)
        if parentId is not None:
            buttonCheck = UC.get_attributes(parentId, childFeature, snapAngle, self.identifier, self.drawLayer, PC.PAND["configtable"])
            if buttonCheck != 'Cancel':
                UC.write_layer(self.drawLayer, childFeature)
        self.run_tekenen('dummy', self.drawLayer.name(), self.identifier)

    def close_teken_show_object(self):
        """destroy and close self"""
        self.move.clicked.disconnect()
        self.identify.clicked.disconnect()
        self.select.clicked.disconnect()
        self.delete_f.clicked.disconnect()
        self.pan.clicked.disconnect()
        self.terug.clicked.disconnect()
        for widget in self.children():
            if isinstance(widget, PQtW.QPushButton):
                try:
                    widget.clicked.disconnect()
                except: # pylint: disable=bare-except
                    pass
        self.close()
        self.parent.show()
        del self
