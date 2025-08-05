"""drawing class for repressief object"""
import os

from qgis.PyQt import uic
import qgis.PyQt.QtWidgets as PQtW
import qgis.PyQt.QtCore as PQtC
from qgis.PyQt.QtGui import QIcon

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
    snapSymbols = []
    tabWidget = None
    anchorPoints = None

    def __init__(self, parent=None):
        super(oivInfoOfInterestTekenWidget, self).__init__(parent)
        self.setupUi(self)
        self.parent = parent
        self.baseWidget = parent
        self.selectTool = parent.selectTool
        self.polygonSelectTool = parent.polygonSelectTool
        self.iface = parent.iface
        self.canvas = parent.canvas
        self.initUI()

    def initUI(self):
        """intitiate the UI elemets on the widget"""
        UG.set_lengte_oppervlakte_visibility(self.baseWidget, False, False, False, False)
        self.baseWidget.setVisible(True)
        self.move.clicked.connect(self.run_move_point)
        self.identify.clicked.connect(self.run_edit_tool)
        self.select.clicked.connect(self.run_select_tool)
        self.delete_f.clicked.connect(self.run_delete_tool)
        self.terug.clicked.connect(self.close_object_tekenen_show_base)
        self.pan.clicked.connect(self.activatePan)
        self.baseWidget.done.setVisible(False)
        self.baseWidget.done_png.setVisible(False)
        self.baseWidget.filter_objecten.setVisible(False)
        self.baseWidget.label_filter.setVisible(False)
        self.baseWidget.info_of_interest.setVisible(False)
        self.baseWidget.label_info_of_interest.setVisible(False)
        actionList = PC.ACTIONDICTIOI
        actionList, self.editableLayerNames, self.moveLayerNames, self.snapSymbols, self.anchorPoints = UG.get_actions(PC.INFO_INTEREST["configtable"], actionList)
        self.initActions(actionList)

    def initActions(self, actionList):
        cnti = 0
        cntj = 0
        sizePolicy = PQtW.QSizePolicy(PQtW.QSizePolicy.Policy.Minimum, PQtW.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        self.tabWidget = self.findChild(PQtW.QTabWidget, 'tabWidgetInfoOfInterest')
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
        #self.close()
        self.drawbuttonframe.setVisible(False)
        self.baseWidget.filter_objecten.setVisible(True)
        self.baseWidget.label_filter.setVisible(True)
        self.baseWidget.info_of_interest.setVisible(True)
        self.baseWidget.label_info_of_interest.setVisible(True)
        self.baseWidget.cadframe.setVisible(False)
        self.baseWidget.close_info_of_interest()
        #del self

    def activatePan(self):
        """trigger pan function to loose other functions"""
        self.iface.actionPan().trigger()
        self.baseWidget.moveTool.possibleSnapFeatures = []
        self.selectTool.possibleSnapFeatures = []

    def run_edit_tool(self):
        """activate the edit feature tool"""
        try:
            self.selectTool.geomSelected.disconnect()
        except:
            pass
        self.selectTool.possibleSnapFeatures = self.get_snap_features()
        self.selectTool.layer = UC.getlayer_byname(PC.PAND["bouwlaaglayername"])
        self.selectTool.whichConfig = PC.INFO_INTEREST["configtable"]
        self.canvas.setMapTool(self.selectTool)
        self.selectTool.geomSelected.connect(self.edit_attribute)

    def get_snap_features(self):
        layerNamesTup = CH.get_childlayers_info_point()
        snapLayerNames = [i[0] for i in layerNamesTup]
        possibleSnapFeatures = UC.get_possible_snapFeatures_ioi(snapLayerNames)
        return possibleSnapFeatures

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
        self.selectTool.possibleSnapFeatures = self.get_snap_features()
        self.selectTool.layer = UC.getlayer_byname(PC.PAND["bouwlaaglayername"])
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
        stackWidget = SW.oivStackWidget(self)
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
        self.baseWidget.moveTool.possibleSnapFeatures = self.get_snap_features()
        self.baseWidget.moveTool.layer = UC.getlayer_byname(PC.PAND["bouwlaaglayername"])
        self.baseWidget.moveTool.onMoved = self.stop_moveTool
        self.canvas.setMapTool(self.baseWidget.moveTool)

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
            pointTool = self.baseWidget.pointTool
            pointTool.snapPt = None
            pointTool.snapping = False
            pointTool.startRotate = False
            pointTool.layer = self.drawLayer
            self.canvas.setMapTool(pointTool)
            UG.set_lengte_oppervlakte_visibility(self.baseWidget, False, False, False, False)
            pointTool.onGeometryAdded = self.place_feature
        else:
            drawTool = self.baseWidget.drawTool
            if self.drawLayerType == "LineString":
                drawTool.captureMode = 1
                UG.set_lengte_oppervlakte_visibility(self.baseWidget, True, True, False, True)
            else:
                drawTool.captureMode = 2
                UG.set_lengte_oppervlakte_visibility(self.baseWidget, True, True, True, True)
            drawTool.layer = self.drawLayer
            drawTool.canvas = self.canvas
            drawTool.onGeometryAdded = self.place_feature
            self.canvas.setMapTool(drawTool)
            drawTool.baseWidget = self.baseWidget

    def place_feature(self, points, snapAngle):
        self.iface.setActiveLayer(self.drawLayer)
        if points:
            parentId, childFeature = UC.construct_feature(self.drawLayerType, None, points, None)
        if parentId is not None:
            buttonCheck = UC.get_attributes(parentId, childFeature, snapAngle, self.identifier, self.drawLayer, PC.INFO_INTEREST["configtable"])
            if buttonCheck != 'Cancel':
                UC.write_layer(self.drawLayer, childFeature)
        self.run_tekenen('dummy', self.drawLayer.name(), self.identifier)
