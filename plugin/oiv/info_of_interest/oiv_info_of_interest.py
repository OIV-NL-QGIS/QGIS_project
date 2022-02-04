"""drawing class for repressief object"""
import os

from qgis.PyQt import uic
import qgis.PyQt.QtWidgets as PQtW

import oiv.helpers.utils_core as UC
import oiv.helpers.utils_gui as UG
import oiv.tools.stackwidget as SW
import oiv.tools.editFeature as EF
import oiv.helpers.drawing_helper as DH
import oiv.helpers.qt_helper as QT
import oiv.helpers.configdb_helper as CH
import oiv.helpers.constants as PC

FORM_CLASS, _ = uic.loadUiType(os.path.join(
    os.path.dirname(__file__), PC.INFO_INTEREST["tekenwidgetui"]))


class oivInfoOfInterestTekenWidget(PQtW.QDockWidget, FORM_CLASS):

    parent = None
    drawLayer = None
    identifier = None
    drawLayerType = None
    editableLayerNames = []
    moveLayerNames = []

    def __init__(self, parent=None):
        super(oivInfoOfInterestTekenWidget, self).__init__(parent)
        self.setupUi(self)
        self.parent = parent
        self.selectTool = parent.selectTool
        self.iface = parent.iface
        self.canvas = parent.canvas
        self.initUI()

    def initUI(self):
        """intitiate the UI elemets on the widget"""
        UG.set_lengte_oppervlakte_visibility(self, False, False, False, False)
        self.move.clicked.connect(self.run_move_point)
        self.identify.clicked.connect(self.run_edit_tool)
        self.select.clicked.connect(self.run_select_tool)
        self.delete_f.clicked.connect(self.run_delete_tool)
        self.pan.clicked.connect(self.activatePan)
        self.terug.clicked.connect(self.close_object_tekenen_show_base)
        actionList, self.editableLayerNames, self.moveLayerNames = UG.get_actions(PC.INFO_INTEREST["configtable"])
        self.initActions(actionList)
        self.helpBtn, self.floatBtn, titleBar = QT.getTitleBar()
        self.setTitleBarWidget(titleBar)
        self.helpBtn.clicked.connect(lambda: UC.open_url(PC.HELPURL["objecttekenenhelp"]))
        self.floatBtn.clicked.connect(lambda: self.setFloating(True))

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

    def close_object_tekenen_show_base(self):
        self.move.clicked.disconnect()
        self.identify.clicked.disconnect()
        self.select.clicked.disconnect()
        self.delete_f.clicked.disconnect()
        self.pan.clicked.disconnect()
        self.helpBtn.clicked.disconnect()
        self.floatBtn.clicked.disconnect()
        self.terug.clicked.disconnect()
        try:
            self.selectTool.geomSelected.disconnect()
        except:
            pass
        self.close()
        self.parent.show()
        del self

    def activatePan(self):
        """trigger pan function to loose other functions"""
        self.iface.actionPan().trigger()

    def run_edit_tool(self):
        """activate the edit feature tool"""
        try:
            self.selectTool.geomSelected.disconnect()
        except:
            pass
        self.selectTool.whichConfig = PC.INFO_INTEREST["configtable"]
        self.canvas.setMapTool(self.selectTool)
        self.selectTool.geomSelected.connect(self.edit_attribute)

    def run_select_tool(self):
        """activate the select feature tool"""
        try:
            self.selectTool.geomSelected.disconnect()
        except:
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
        self.selectTool.geomSelected.disconnect()
        self.run_select_tool()

    def run_delete_tool(self):
        """activate delete feature tool"""
        try:
            self.selectTool.geomSelected.disconnect()
        except:
            pass
        self.selectTool.whichConfig = PC.INFO_INTEREST["configtable"]
        self.canvas.setMapTool(self.selectTool)
        self.selectTool.geomSelected.connect(self.delete)

    def delete(self, ilayer, ifeature):
        """delete a feature"""
        reply = EF.delete_feature(ilayer, ifeature, self.editableLayerNames, self.iface)
        if reply == 'Retry':
            self.run_delete_tool()
        self.selectTool.geomSelected.disconnect()
        self.run_delete_tool()

    #open het formulier van een feature in een dockwidget, zodat de attributen kunnen worden bewerkt
    def edit_attribute(self, ilayer, ifeature):
        stackWidget = SW.oivStackWidget()
        self.iface.addDockWidget(QT.getWidgetType(), stackWidget)
        stackWidget.parentWidget = self
        stackWidget.parentWidth = self.width()
        stackWidget.open_feature_form(ilayer, ifeature)
        self.close()
        stackWidget.show()
        self.selectTool.geomSelected.disconnect()
        self.run_edit_tool()

    #om te verschuiven/roteren moeten de betreffende lagen op bewerken worden gezet
    def run_move_point(self):
        for lyrName in self.moveLayerNames:
            moveLayer = UC.getlayer_byname(lyrName)
            moveLayer.startEditing()
        self.parent.moveTool.onMoved = self.stop_moveTool
        self.canvas.setMapTool(self.parent.moveTool)

    #na de actie verschuiven/bewerken moeten de betreffende lagen opgeslagen worden en bewerken moet worden uitgezet.
    def stop_moveTool(self):
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
        if self.drawLayerType == "Point":
            pointTool = self.parent.pointTool
            pointTool.snapPt = None
            pointTool.snapping = False
            pointTool.startRotate = False
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
            drawTool.canvas = self.canvas
            drawTool.onGeometryAdded = self.place_feature
            self.canvas.setMapTool(drawTool)
            drawTool.parent = self

    def place_feature(self, points, snapAngle):
        self.iface.setActiveLayer(self.drawLayer)
        if points:
            parentId, childFeature = UC.construct_feature(self.drawLayerType, None, points, None)
        if parentId is not None:
            buttonCheck = UC.get_attributes(parentId, childFeature, snapAngle, self.identifier, self.drawLayer, PC.INFO_INTEREST["configtable"])
            if buttonCheck != 'Cancel':
                UC.write_layer(self.drawLayer, childFeature)
        self.run_tekenen('dummy', self.drawLayer.name(), self.identifier)
