# Form implementation generated from reading ui file 'c:\Users\JoostDeen\AppData\Roaming\QGIS\QGIS3\profiles\default\python\plugins\oiv\repressief_object\oiv_repressief_object_widget.ui'
#
# Created by: PyQt6 UI code generator 6.3.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_OivObjectenDockWidgetBase(object):
    def setupUi(self, OivObjectenDockWidgetBase):
        OivObjectenDockWidgetBase.setObjectName("OivObjectenDockWidgetBase")
        OivObjectenDockWidgetBase.resize(406, 812)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(OivObjectenDockWidgetBase.sizePolicy().hasHeightForWidth())
        OivObjectenDockWidgetBase.setSizePolicy(sizePolicy)
        OivObjectenDockWidgetBase.setFeatures(QtWidgets.QDockWidget.DockWidgetFeature.NoDockWidgetFeatures)
        OivObjectenDockWidgetBase.setAllowedAreas(QtCore.Qt.DockWidgetArea.NoDockWidgetArea)
        OivObjectenDockWidgetBase.setWindowTitle("")
        self.dockWidgetContents = QtWidgets.QWidget()
        self.dockWidgetContents.setObjectName("dockWidgetContents")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.dockWidgetContents)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.scrollArea = QtWidgets.QScrollArea(self.dockWidgetContents)
        self.scrollArea.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.scrollArea.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.scrollArea.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.scrollArea.setLineWidth(0)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 388, 772))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.baseobjectFrame = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.baseobjectFrame.sizePolicy().hasHeightForWidth())
        self.baseobjectFrame.setSizePolicy(sizePolicy)
        self.baseobjectFrame.setMinimumSize(QtCore.QSize(0, 0))
        self.baseobjectFrame.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.baseobjectFrame.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.baseobjectFrame.setObjectName("baseobjectFrame")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.baseobjectFrame)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_4.setSpacing(6)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.object_info = QtWidgets.QPushButton(self.baseobjectFrame)
        self.object_info.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.object_info.sizePolicy().hasHeightForWidth())
        self.object_info.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.object_info.setFont(font)
        self.object_info.setStyleSheet("background-color: rgb(240, 240, 240);")
        self.object_info.setCheckable(False)
        self.object_info.setObjectName("object_info")
        self.gridLayout_4.addWidget(self.object_info, 2, 1, 1, 1)
        self.label_draw = QtWidgets.QLabel(self.baseobjectFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_draw.sizePolicy().hasHeightForWidth())
        self.label_draw.setSizePolicy(sizePolicy)
        self.label_draw.setMaximumSize(QtCore.QSize(25, 25))
        self.label_draw.setText("")
        self.label_draw.setPixmap(QtGui.QPixmap(":/plugins/oiv/config_files/png/interface/draw.png"))
        self.label_draw.setScaledContents(True)
        self.label_draw.setObjectName("label_draw")
        self.gridLayout_4.addWidget(self.label_draw, 1, 0, 1, 1)
        self.label_info = QtWidgets.QLabel(self.baseobjectFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_info.sizePolicy().hasHeightForWidth())
        self.label_info.setSizePolicy(sizePolicy)
        self.label_info.setMaximumSize(QtCore.QSize(25, 25))
        self.label_info.setText("")
        self.label_info.setPixmap(QtGui.QPixmap(":/plugins/oiv/config_files/png/interface/edit.png"))
        self.label_info.setScaledContents(True)
        self.label_info.setObjectName("label_info")
        self.gridLayout_4.addWidget(self.label_info, 2, 0, 1, 1)
        self.object_draw = QtWidgets.QPushButton(self.baseobjectFrame)
        self.object_draw.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.object_draw.sizePolicy().hasHeightForWidth())
        self.object_draw.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.object_draw.setFont(font)
        self.object_draw.setStyleSheet("background-color: rgb(240, 240, 240);")
        self.object_draw.setCheckable(False)
        self.object_draw.setObjectName("object_draw")
        self.gridLayout_4.addWidget(self.object_draw, 1, 1, 1, 1)
        self.object_delete = QtWidgets.QPushButton(self.baseobjectFrame)
        self.object_delete.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.object_delete.sizePolicy().hasHeightForWidth())
        self.object_delete.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.object_delete.setFont(font)
        self.object_delete.setStyleSheet("background-color: rgb(240, 240, 240);")
        self.object_delete.setCheckable(False)
        self.object_delete.setObjectName("object_delete")
        self.gridLayout_4.addWidget(self.object_delete, 3, 1, 1, 1)
        self.label_delete = QtWidgets.QLabel(self.baseobjectFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_delete.sizePolicy().hasHeightForWidth())
        self.label_delete.setSizePolicy(sizePolicy)
        self.label_delete.setMaximumSize(QtCore.QSize(25, 25))
        self.label_delete.setText("")
        self.label_delete.setPixmap(QtGui.QPixmap(":/plugins/oiv/config_files/png/interface/close.png"))
        self.label_delete.setScaledContents(True)
        self.label_delete.setObjectName("label_delete")
        self.gridLayout_4.addWidget(self.label_delete, 3, 0, 1, 1)
        self.object_add = QtWidgets.QPushButton(self.baseobjectFrame)
        self.object_add.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.object_add.sizePolicy().hasHeightForWidth())
        self.object_add.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.object_add.setFont(font)
        self.object_add.setStyleSheet("background-color: rgb(240, 240, 240);")
        self.object_add.setCheckable(False)
        self.object_add.setObjectName("object_add")
        self.gridLayout_4.addWidget(self.object_add, 0, 1, 1, 1)
        self.object_bgt = QtWidgets.QPushButton(self.baseobjectFrame)
        self.object_bgt.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.object_bgt.sizePolicy().hasHeightForWidth())
        self.object_bgt.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.object_bgt.setFont(font)
        self.object_bgt.setStyleSheet("background-color: rgb(240, 240, 240);")
        self.object_bgt.setCheckable(False)
        self.object_bgt.setObjectName("object_bgt")
        self.gridLayout_4.addWidget(self.object_bgt, 6, 1, 1, 1)
        self.label_add = QtWidgets.QLabel(self.baseobjectFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_add.sizePolicy().hasHeightForWidth())
        self.label_add.setSizePolicy(sizePolicy)
        self.label_add.setMaximumSize(QtCore.QSize(25, 25))
        self.label_add.setText("")
        self.label_add.setPixmap(QtGui.QPixmap(":/plugins/oiv/config_files/png/interface/add.png"))
        self.label_add.setScaledContents(True)
        self.label_add.setObjectName("label_add")
        self.gridLayout_4.addWidget(self.label_add, 0, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(0, 20, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        self.gridLayout_4.addItem(spacerItem, 4, 1, 1, 1)
        self.object_print = QtWidgets.QPushButton(self.baseobjectFrame)
        self.object_print.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.object_print.sizePolicy().hasHeightForWidth())
        self.object_print.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.object_print.setFont(font)
        self.object_print.setStyleSheet("background-color: rgb(240, 240, 240);")
        self.object_print.setCheckable(False)
        self.object_print.setObjectName("object_print")
        self.gridLayout_4.addWidget(self.object_print, 5, 1, 1, 1)
        self.object_inventory = QtWidgets.QPushButton(self.baseobjectFrame)
        self.object_inventory.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.object_inventory.sizePolicy().hasHeightForWidth())
        self.object_inventory.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.object_inventory.setFont(font)
        self.object_inventory.setStyleSheet("background-color: rgb(240, 240, 240);")
        self.object_inventory.setCheckable(False)
        self.object_inventory.setObjectName("object_inventory")
        self.gridLayout_4.addWidget(self.object_inventory, 7, 1, 1, 1)
        self.label_print = QtWidgets.QLabel(self.baseobjectFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_print.sizePolicy().hasHeightForWidth())
        self.label_print.setSizePolicy(sizePolicy)
        self.label_print.setMaximumSize(QtCore.QSize(25, 25))
        self.label_print.setText("")
        self.label_print.setPixmap(QtGui.QPixmap(":/plugins/oiv/config_files/png/interface/print.png"))
        self.label_print.setScaledContents(True)
        self.label_print.setObjectName("label_print")
        self.gridLayout_4.addWidget(self.label_print, 5, 0, 1, 1)
        self.label_bgt = QtWidgets.QLabel(self.baseobjectFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_bgt.sizePolicy().hasHeightForWidth())
        self.label_bgt.setSizePolicy(sizePolicy)
        self.label_bgt.setMaximumSize(QtCore.QSize(25, 25))
        self.label_bgt.setText("")
        self.label_bgt.setPixmap(QtGui.QPixmap(":/plugins/oiv/config_files/png/interface/touch.png"))
        self.label_bgt.setScaledContents(True)
        self.label_bgt.setObjectName("label_bgt")
        self.gridLayout_4.addWidget(self.label_bgt, 6, 0, 1, 1)
        self.label_inventory = QtWidgets.QLabel(self.baseobjectFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_inventory.sizePolicy().hasHeightForWidth())
        self.label_inventory.setSizePolicy(sizePolicy)
        self.label_inventory.setMaximumSize(QtCore.QSize(25, 25))
        self.label_inventory.setText("")
        self.label_inventory.setPixmap(QtGui.QPixmap(":/plugins/oiv/config_files/png/interface/inventory.png"))
        self.label_inventory.setScaledContents(True)
        self.label_inventory.setObjectName("label_inventory")
        self.gridLayout_4.addWidget(self.label_inventory, 7, 0, 1, 1)
        self.gridLayout_3.addWidget(self.baseobjectFrame, 3, 0, 1, 2)
        self.formelenaam = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.formelenaam.sizePolicy().hasHeightForWidth())
        self.formelenaam.setSizePolicy(sizePolicy)
        self.formelenaam.setAcceptDrops(False)
        self.formelenaam.setStyleSheet("background-color: rgb(208, 208, 208);\n"
"border-color: rgba(255, 255, 255, 0);")
        self.formelenaam.setObjectName("formelenaam")
        self.gridLayout_3.addWidget(self.formelenaam, 1, 0, 1, 2)
        self.object_id = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.object_id.sizePolicy().hasHeightForWidth())
        self.object_id.setSizePolicy(sizePolicy)
        self.object_id.setAcceptDrops(False)
        self.object_id.setStyleSheet("background-color: rgb(208, 208, 208);\n"
"border-color: rgba(255, 255, 255, 0);")
        self.object_id.setObjectName("object_id")
        self.gridLayout_3.addWidget(self.object_id, 2, 0, 1, 2)
        self.label_6 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.gridLayout_3.addWidget(self.label_6, 0, 0, 1, 2)
        self.addobjectFrame = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.addobjectFrame.sizePolicy().hasHeightForWidth())
        self.addobjectFrame.setSizePolicy(sizePolicy)
        self.addobjectFrame.setMinimumSize(QtCore.QSize(0, 0))
        self.addobjectFrame.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.addobjectFrame.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.addobjectFrame.setLineWidth(0)
        self.addobjectFrame.setObjectName("addobjectFrame")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.addobjectFrame)
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_5.setObjectName("gridLayout_5")
        spacerItem1 = QtWidgets.QSpacerItem(17, 20, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.gridLayout_5.addItem(spacerItem1, 7, 1, 1, 1)
        self.label_inventory_4 = QtWidgets.QLabel(self.addobjectFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_inventory_4.sizePolicy().hasHeightForWidth())
        self.label_inventory_4.setSizePolicy(sizePolicy)
        self.label_inventory_4.setMaximumSize(QtCore.QSize(25, 25))
        self.label_inventory_4.setText("")
        self.label_inventory_4.setPixmap(QtGui.QPixmap(":/plugins/oiv/config_files/png/interface/georeference.png"))
        self.label_inventory_4.setScaledContents(True)
        self.label_inventory_4.setObjectName("label_inventory_4")
        self.gridLayout_5.addWidget(self.label_inventory_4, 6, 0, 1, 1)
        self.georeferencer = QtWidgets.QPushButton(self.addobjectFrame)
        self.georeferencer.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.georeferencer.sizePolicy().hasHeightForWidth())
        self.georeferencer.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.georeferencer.setFont(font)
        self.georeferencer.setStyleSheet("background-color: rgb(240, 240, 240);")
        self.georeferencer.setCheckable(False)
        self.georeferencer.setObjectName("georeferencer")
        self.gridLayout_5.addWidget(self.georeferencer, 6, 1, 1, 1)
        self.terrein_bewerken = QtWidgets.QPushButton(self.addobjectFrame)
        self.terrein_bewerken.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.terrein_bewerken.sizePolicy().hasHeightForWidth())
        self.terrein_bewerken.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.terrein_bewerken.setFont(font)
        self.terrein_bewerken.setStyleSheet("background-color: rgb(240, 240, 240);")
        self.terrein_bewerken.setCheckable(False)
        self.terrein_bewerken.setObjectName("terrein_bewerken")
        self.gridLayout_5.addWidget(self.terrein_bewerken, 0, 1, 2, 1)
        self.label_inventory_5 = QtWidgets.QLabel(self.addobjectFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_inventory_5.sizePolicy().hasHeightForWidth())
        self.label_inventory_5.setSizePolicy(sizePolicy)
        self.label_inventory_5.setMaximumSize(QtCore.QSize(25, 25))
        self.label_inventory_5.setText("")
        self.label_inventory_5.setPixmap(QtGui.QPixmap(":/plugins/oiv/config_files/png/interface/import_drawing.png"))
        self.label_inventory_5.setScaledContents(True)
        self.label_inventory_5.setObjectName("label_inventory_5")
        self.gridLayout_5.addWidget(self.label_inventory_5, 3, 0, 1, 1)
        self.terug_add = QtWidgets.QPushButton(self.addobjectFrame)
        self.terug_add.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.terug_add.sizePolicy().hasHeightForWidth())
        self.terug_add.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.terug_add.setFont(font)
        self.terug_add.setStyleSheet("background-color: rgb(240, 240, 240);")
        self.terug_add.setCheckable(False)
        self.terug_add.setObjectName("terug_add")
        self.gridLayout_5.addWidget(self.terug_add, 9, 1, 1, 1)
        self.label_inventory_6 = QtWidgets.QLabel(self.addobjectFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_inventory_6.sizePolicy().hasHeightForWidth())
        self.label_inventory_6.setSizePolicy(sizePolicy)
        self.label_inventory_6.setMaximumSize(QtCore.QSize(25, 25))
        self.label_inventory_6.setText("")
        self.label_inventory_6.setPixmap(QtGui.QPixmap(":/plugins/oiv/config_files/png/interface/back.png"))
        self.label_inventory_6.setScaledContents(True)
        self.label_inventory_6.setObjectName("label_inventory_6")
        self.gridLayout_5.addWidget(self.label_inventory_6, 9, 0, 1, 1)
        self.create_grid = QtWidgets.QPushButton(self.addobjectFrame)
        self.create_grid.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.create_grid.sizePolicy().hasHeightForWidth())
        self.create_grid.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.create_grid.setFont(font)
        self.create_grid.setStyleSheet("background-color: rgb(240, 240, 240);")
        self.create_grid.setCheckable(False)
        self.create_grid.setObjectName("create_grid")
        self.gridLayout_5.addWidget(self.create_grid, 4, 1, 1, 1)
        self.import_drawing = QtWidgets.QPushButton(self.addobjectFrame)
        self.import_drawing.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.import_drawing.sizePolicy().hasHeightForWidth())
        self.import_drawing.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.import_drawing.setFont(font)
        self.import_drawing.setStyleSheet("background-color: rgb(240, 240, 240);")
        self.import_drawing.setCheckable(False)
        self.import_drawing.setObjectName("import_drawing")
        self.gridLayout_5.addWidget(self.import_drawing, 3, 1, 1, 1)
        self.label_inventory_3 = QtWidgets.QLabel(self.addobjectFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_inventory_3.sizePolicy().hasHeightForWidth())
        self.label_inventory_3.setSizePolicy(sizePolicy)
        self.label_inventory_3.setMaximumSize(QtCore.QSize(25, 25))
        self.label_inventory_3.setText("")
        self.label_inventory_3.setPixmap(QtGui.QPixmap(":/plugins/oiv/config_files/png/interface/terrein.png"))
        self.label_inventory_3.setScaledContents(True)
        self.label_inventory_3.setObjectName("label_inventory_3")
        self.gridLayout_5.addWidget(self.label_inventory_3, 0, 0, 1, 1)
        self.label_inventory_2 = QtWidgets.QLabel(self.addobjectFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_inventory_2.sizePolicy().hasHeightForWidth())
        self.label_inventory_2.setSizePolicy(sizePolicy)
        self.label_inventory_2.setMaximumSize(QtCore.QSize(25, 25))
        self.label_inventory_2.setText("")
        self.label_inventory_2.setPixmap(QtGui.QPixmap(":/plugins/oiv/config_files/png/interface/kaartblad_grid.png"))
        self.label_inventory_2.setScaledContents(True)
        self.label_inventory_2.setObjectName("label_inventory_2")
        self.gridLayout_5.addWidget(self.label_inventory_2, 4, 0, 1, 1)
        self.terreinFrame = QtWidgets.QFrame(self.addobjectFrame)
        self.terreinFrame.setLineWidth(0)
        self.terreinFrame.setObjectName("terreinFrame")
        self.gridLayout = QtWidgets.QGridLayout(self.terreinFrame)
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SizeConstraint.SetMinimumSize)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.straal_label = QtWidgets.QLabel(self.terreinFrame)
        self.straal_label.setObjectName("straal_label")
        self.gridLayout.addWidget(self.straal_label, 1, 0, 1, 3)
        self.straal_button = QtWidgets.QPushButton(self.terreinFrame)
        self.straal_button.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/plugins/oiv/config_files/png/hulpcirkel.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.straal_button.setIcon(icon)
        self.straal_button.setObjectName("straal_button")
        self.gridLayout.addWidget(self.straal_button, 2, 0, 1, 1)
        self.oppervlakte_label = QtWidgets.QLabel(self.terreinFrame)
        self.oppervlakte_label.setObjectName("oppervlakte_label")
        self.gridLayout.addWidget(self.oppervlakte_label, 0, 3, 1, 2)
        self.oppervlakte = QtWidgets.QDoubleSpinBox(self.terreinFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Ignored, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.oppervlakte.sizePolicy().hasHeightForWidth())
        self.oppervlakte.setSizePolicy(sizePolicy)
        self.oppervlakte.setStyleSheet("background-color: rgb(240, 240, 240);\n"
"border-color: rgba(255, 255, 255, 0);")
        self.oppervlakte.setFrame(False)
        self.oppervlakte.setButtonSymbols(QtWidgets.QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.oppervlakte.setDecimals(1)
        self.oppervlakte.setMaximum(100000.0)
        self.oppervlakte.setObjectName("oppervlakte")
        self.gridLayout.addWidget(self.oppervlakte, 0, 5, 1, 1)
        self.offset_button = QtWidgets.QPushButton(self.terreinFrame)
        self.offset_button.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/plugins/oiv/config_files/png/offset_parallel.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.offset_button.setIcon(icon1)
        self.offset_button.setIconSize(QtCore.QSize(16, 16))
        self.offset_button.setObjectName("offset_button")
        self.gridLayout.addWidget(self.offset_button, 2, 3, 1, 1)
        self.lengte_label = QtWidgets.QLabel(self.terreinFrame)
        self.lengte_label.setObjectName("lengte_label")
        self.gridLayout.addWidget(self.lengte_label, 0, 0, 1, 2)
        self.terrein_tekenen = QtWidgets.QPushButton(self.terreinFrame)
        self.terrein_tekenen.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.terrein_tekenen.sizePolicy().hasHeightForWidth())
        self.terrein_tekenen.setSizePolicy(sizePolicy)
        self.terrein_tekenen.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/plugins/oiv/config_files/png/terrein.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.terrein_tekenen.setIcon(icon2)
        self.terrein_tekenen.setIconSize(QtCore.QSize(28, 28))
        self.terrein_tekenen.setCheckable(False)
        self.terrein_tekenen.setAutoDefault(False)
        self.terrein_tekenen.setDefault(False)
        self.terrein_tekenen.setFlat(False)
        self.terrein_tekenen.setObjectName("terrein_tekenen")
        self.gridLayout.addWidget(self.terrein_tekenen, 3, 0, 1, 1)
        self.delete_f = QtWidgets.QPushButton(self.terreinFrame)
        self.delete_f.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/plugins/oiv/config_files/png/delete.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.delete_f.setIcon(icon3)
        self.delete_f.setIconSize(QtCore.QSize(28, 28))
        self.delete_f.setObjectName("delete_f")
        self.gridLayout.addWidget(self.delete_f, 3, 1, 1, 1)
        self.identify = QtWidgets.QPushButton(self.terreinFrame)
        self.identify.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.identify.sizePolicy().hasHeightForWidth())
        self.identify.setSizePolicy(sizePolicy)
        self.identify.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/plugins/oiv/config_files/png/identify.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.identify.setIcon(icon4)
        self.identify.setIconSize(QtCore.QSize(28, 28))
        self.identify.setCheckable(False)
        self.identify.setAutoDefault(False)
        self.identify.setDefault(False)
        self.identify.setFlat(False)
        self.identify.setObjectName("identify")
        self.gridLayout.addWidget(self.identify, 3, 3, 1, 1)
        self.pan = QtWidgets.QPushButton(self.terreinFrame)
        self.pan.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/plugins/oiv/config_files/png/pan.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pan.setIcon(icon5)
        self.pan.setIconSize(QtCore.QSize(28, 28))
        self.pan.setObjectName("pan")
        self.gridLayout.addWidget(self.pan, 3, 4, 1, 1)
        self.lengte = QtWidgets.QDoubleSpinBox(self.terreinFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Ignored, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lengte.sizePolicy().hasHeightForWidth())
        self.lengte.setSizePolicy(sizePolicy)
        self.lengte.setStyleSheet("background-color: rgb(240, 240, 240);\n"
"border-color: rgba(255, 255, 255, 0);")
        self.lengte.setFrame(False)
        self.lengte.setButtonSymbols(QtWidgets.QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.lengte.setDecimals(1)
        self.lengte.setMaximum(100000.0)
        self.lengte.setObjectName("lengte")
        self.gridLayout.addWidget(self.lengte, 0, 2, 1, 1)
        self.straal = QtWidgets.QDoubleSpinBox(self.terreinFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Ignored, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.straal.sizePolicy().hasHeightForWidth())
        self.straal.setSizePolicy(sizePolicy)
        self.straal.setDecimals(1)
        self.straal.setMaximum(1000.0)
        self.straal.setObjectName("straal")
        self.gridLayout.addWidget(self.straal, 2, 1, 1, 2)
        self.offset = QtWidgets.QDoubleSpinBox(self.terreinFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Ignored, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.offset.sizePolicy().hasHeightForWidth())
        self.offset.setSizePolicy(sizePolicy)
        self.offset.setDecimals(1)
        self.offset.setMinimum(-1000.0)
        self.offset.setMaximum(1000.0)
        self.offset.setObjectName("offset")
        self.gridLayout.addWidget(self.offset, 2, 4, 1, 2)
        self.offset_label = QtWidgets.QLabel(self.terreinFrame)
        self.offset_label.setObjectName("offset_label")
        self.gridLayout.addWidget(self.offset_label, 1, 3, 1, 3)
        self.gridLayout_5.addWidget(self.terreinFrame, 2, 1, 1, 1)
        self.gridLayout_3.addWidget(self.addobjectFrame, 12, 0, 2, 2)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout_2.addWidget(self.scrollArea, 0, 0, 1, 1)
        OivObjectenDockWidgetBase.setWidget(self.dockWidgetContents)

        self.retranslateUi(OivObjectenDockWidgetBase)
        QtCore.QMetaObject.connectSlotsByName(OivObjectenDockWidgetBase)

    def retranslateUi(self, OivObjectenDockWidgetBase):
        _translate = QtCore.QCoreApplication.translate
        self.object_info.setText(_translate("OivObjectenDockWidgetBase", "Info"))
        self.object_draw.setText(_translate("OivObjectenDockWidgetBase", "Tekenen"))
        self.object_delete.setText(_translate("OivObjectenDockWidgetBase", "Verwijderen"))
        self.object_add.setText(_translate("OivObjectenDockWidgetBase", "Toevoegen"))
        self.object_bgt.setText(_translate("OivObjectenDockWidgetBase", "Info BGT"))
        self.object_print.setText(_translate("OivObjectenDockWidgetBase", "Printen"))
        self.object_inventory.setText(_translate("OivObjectenDockWidgetBase", "Werkvoorraad"))
        self.label_6.setText(_translate("OivObjectenDockWidgetBase", "Repressief object:"))
        self.georeferencer.setText(_translate("OivObjectenDockWidgetBase", "Georeferencer"))
        self.terrein_bewerken.setText(_translate("OivObjectenDockWidgetBase", "Terrein"))
        self.terug_add.setText(_translate("OivObjectenDockWidgetBase", "Terug"))
        self.create_grid.setText(_translate("OivObjectenDockWidgetBase", "Maak Kaartblad / Grid"))
        self.import_drawing.setText(_translate("OivObjectenDockWidgetBase", "Importeer tekening"))
        self.straal_label.setText(_translate("OivObjectenDockWidgetBase", "Hulpcirkel (m)"))
        self.oppervlakte_label.setText(_translate("OivObjectenDockWidgetBase", "Oppervlakte (m2)"))
        self.lengte_label.setText(_translate("OivObjectenDockWidgetBase", "Lengte (m)"))
        self.terrein_tekenen.setToolTip(_translate("OivObjectenDockWidgetBase", "teken het terrein"))
        self.delete_f.setToolTip(_translate("OivObjectenDockWidgetBase", "delete object..."))
        self.identify.setToolTip(_translate("OivObjectenDockWidgetBase", "open formulier van een object..."))
        self.pan.setToolTip(_translate("OivObjectenDockWidgetBase", "selecteer de functie Pan..."))
        self.offset_label.setText(_translate("OivObjectenDockWidgetBase", "Offset parallel (m)"))