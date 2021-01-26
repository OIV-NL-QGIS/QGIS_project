"""drawing class for repressief object"""
import os

from qgis.PyQt import uic #pylint: disable=import-error
from qgis.PyQt.QtWidgets import QDockWidget, QPushButton #pylint: disable=import-error
from qgis.utils import iface #pylint: disable=import-error

from ..tools.utils_core import check_layer_type, getlayer_byname, write_layer, get_attributes
from ..tools.utils_core import construct_feature, get_possible_snapFeatures_object, read_settings
from ..tools.utils_gui import get_actions, set_lengte_oppervlakte_visibility
from ..tools.oiv_stackwidget import oivStackWidget
from ..tools.editFeature import delete_feature

from ..plugin_helpers.drawing_helper import ROSNAPSYMBOLS, ROSNAPLAYERS
from ..plugin_helpers.qt_helper import getWidgetType

FORM_CLASS, _ = uic.loadUiType(os.path.join(
    os.path.dirname(__file__), 'oiv_object_tekenen_widget.ui'))

class oivObjectTekenWidget(QDockWidget, FORM_CLASS):

    config = 'config_object'
    repressiefobjectwidget = None
    iface = None
    canvas = None
    selectTool = None
    pointTool = None
    drawLayer = None
    identifier = None
    parentLayerName = None
    drawLayerType = None
    editableLayerNames = []
    drawTool = None
    moveTool = None
    snapPicto = ROSNAPSYMBOLS
    moveLayerNames = []
    snapLayerNames = ROSNAPLAYERS

    def __init__(self, parent=None):
        super(oivObjectTekenWidget, self).__init__(parent)
        self.setupUi(self)
        self.iface = iface

    def initUI(self):
        """intitiate the UI elemets on the widget"""
        set_lengte_oppervlakte_visibility(self, False, False, False, False)
        self.object_id.setVisible(False)
        self.move.clicked.connect(self.run_move_point)
        self.identify.clicked.connect(self.run_edit_tool)
        self.select.clicked.connect(self.run_select_tool)
        self.delete_f.clicked.connect(self.run_delete_tool)
        self.pan.clicked.connect(self.activatePan)
        self.terug.clicked.connect(self.close_object_tekenen_show_base)
        actionList, self.editableLayerNames, self.moveLayerNames = get_actions(self.config)
        self.initActions(actionList)

    def initActions(self, actionList):
        """connect all the buttons to the action"""
        for lyr in actionList:
            for action in lyr:
                runLayerName = action[0]
                buttonNr = action[1]
                buttonName = str(action[2].lower())
                strButton = self.findChild(QPushButton, buttonName)
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
        self.terug.clicked.disconnect()
        self.close()
        self.repressiefobjectwidget.show()
        del self

    def ini_action(self, actionList, run_layer):
        """connect all the buttons to the action"""
        for action in actionList:
            buttonNr = action[0]
            buttonName = str(action[1].lower())
            strButton = self.findChild(QPushButton, buttonName)
            if strButton:
                #set tooltip per buttonn
                strButton.setToolTip(buttonName)
                #geef met de signal ook mee welke knop er is geklikt -> nr
                strButton.clicked.connect(lambda dummy='dummyvar', rlayer=run_layer, who=buttonNr: self.run_tekenen(dummy, rlayer, who))

    def activatePan(self):
        self.iface.actionPan().trigger()

    def run_edit_tool(self):
        self.selectTool.whichConfig = self.config
        self.canvas.setMapTool(self.selectTool)
        self.selectTool.geomSelected.connect(self.edit_attribute)

    def run_select_tool(self):
        self.canvas.setMapTool(self.selectTool)
        self.selectTool.geomSelected.connect(self.select_feature)

    def select_feature(self, ilayer, ifeature):
        self.iface.setActiveLayer(ilayer)
        ids = []
        ids.append(ifeature.id())
        ilayer.selectByIds(ids)
        ilayer.startEditing()
        self.selectTool.geomSelected.disconnect(self.select_feature)

    def run_delete_tool(self):
        self.selectTool.whichConfig = self.config
        self.canvas.setMapTool(self.selectTool)
        self.selectTool.geomSelected.connect(self.delete)

    def delete(self, ilayer, ifeature):
        """delete a feature"""
        reply = delete_feature(ilayer, ifeature, self.editableLayerNames, self.iface)
        if reply == 'Retry':
            self.run_delete_tool()
        self.selectTool.geomSelected.disconnect(self.delete)

    #open het formulier van een feature in een dockwidget, zodat de attributen kunnen worden bewerkt
    def edit_attribute(self, ilayer, ifeature):
        stackWidget = oivStackWidget()
        self.iface.addDockWidget(getWidgetType(), stackWidget)
        stackWidget.parentWidget = self
        stackWidget.open_feature_form(ilayer, ifeature)
        self.close()
        stackWidget.show()
        self.selectTool.geomSelected.disconnect(self.edit_attribute)

    #om te verschuiven/roteren moeten de betreffende lagen op bewerken worden gezet
    def run_move_point(self):
        for lyrName in self.moveLayerNames:
            moveLayer = getlayer_byname(lyrName)
            moveLayer.startEditing()
        self.moveTool.onMoved = self.stop_moveTool
        self.canvas.setMapTool(self.moveTool)

    #na de actie verschuiven/bewerken moeten de betreffende lagen opgeslagen worden en bewerken moet worden uitgezet.
    def stop_moveTool(self):
        for lyrName in self.moveLayerNames:
            moveLayer = getlayer_byname(lyrName)
            moveLayer.commitChanges()
            moveLayer.reload()
        self.activatePan()

    def run_tekenen(self, _dummy, runLayer, feature_id):
        #welke pictogram is aangeklikt en wat is de bijbehorende tekenlaag
        self.identifier = feature_id
        self.drawLayer = getlayer_byname(runLayer)
        self.drawLayerType = check_layer_type(self.drawLayer)
        query = "SELECT parent_layer FROM config_object WHERE child_layer = '{}'".format(runLayer)
        self.parentLayerName = read_settings(query, False)[0]
        objectId = self.object_id.text()
        possibleSnapFeatures = get_possible_snapFeatures_object(self.snapLayerNames, objectId)
        if self.drawLayerType == "Point":
            self.pointTool.snapPt = None
            self.pointTool.snapping = False
            self.pointTool.startRotate = False
            self.pointTool.possibleSnapFeatures = possibleSnapFeatures
            if self.identifier in self.snapPicto:
                self.pointTool.snapping = True
            self.pointTool.layer = self.drawLayer
            self.canvas.setMapTool(self.pointTool)
            set_lengte_oppervlakte_visibility(self, False, False, False, False)
            self.pointTool.onGeometryAdded = self.place_feature
        else:
            if self.drawLayerType == "LineString":
                self.drawTool.captureMode = 1
                set_lengte_oppervlakte_visibility(self, True, True, False, True)
            else:
                self.drawTool.captureMode = 2
                set_lengte_oppervlakte_visibility(self, True, True, True, True)
            self.drawTool.layer = self.drawLayer
            self.drawTool.possibleSnapFeatures = possibleSnapFeatures
            self.drawTool.canvas = self.canvas
            self.drawTool.onGeometryAdded = self.place_feature
            self.canvas.setMapTool(self.drawTool)
            self.drawTool.parent = self

    def place_feature(self, points, snapAngle):
        parentId = None
        self.iface.setActiveLayer(self.drawLayer)
        if points:
            parentId, childFeature = construct_feature(self.drawLayerType, self.parentLayerName, points, self.object_id.text(), self.iface)
        if parentId is not None:
            buttonCheck = get_attributes(parentId, childFeature, snapAngle, self.identifier, self.drawLayer, self.config)
            if buttonCheck != 'Cancel':
                write_layer(self.drawLayer, childFeature)
        self.run_tekenen('dummy', self.drawLayer.name(), self.identifier)
