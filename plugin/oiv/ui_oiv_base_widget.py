# Form implementation generated from reading ui file 'c:\Users\JoostDeen\AppData\Roaming\QGIS\QGIS3\profiles\default\python\plugins\oiv\oiv_base_widget.ui'
#
# Created by: PyQt6 UI code generator 6.3.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_OivObjectenDockWidgetBase(object):
    def setupUi(self, OivObjectenDockWidgetBase):
        OivObjectenDockWidgetBase.setObjectName("OivObjectenDockWidgetBase")
        OivObjectenDockWidgetBase.resize(386, 876)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setBold(True)
        font.setWeight(75)
        OivObjectenDockWidgetBase.setFont(font)
        OivObjectenDockWidgetBase.setFeatures(QtWidgets.QDockWidget.DockWidgetFeature.DockWidgetFloatable|QtWidgets.QDockWidget.DockWidgetFeature.DockWidgetMovable)
        self.dockWidgetContents = QtWidgets.QWidget()
        self.dockWidgetContents.setObjectName("dockWidgetContents")
        self.gridLayout = QtWidgets.QGridLayout(self.dockWidgetContents)
        self.gridLayout.setObjectName("gridLayout")
        self.scrollArea = QtWidgets.QScrollArea(self.dockWidgetContents)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 366, 834))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.info_of_interest = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.info_of_interest.setObjectName("info_of_interest")
        self.gridLayout_2.addWidget(self.info_of_interest, 22, 2, 1, 2)
        self.label_info_of_interest = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_info_of_interest.sizePolicy().hasHeightForWidth())
        self.label_info_of_interest.setSizePolicy(sizePolicy)
        self.label_info_of_interest.setMaximumSize(QtCore.QSize(25, 25))
        self.label_info_of_interest.setText("")
        self.label_info_of_interest.setPixmap(QtGui.QPixmap(":/plugins/oiv/config_files/png/interface/info_of_interest.png"))
        self.label_info_of_interest.setScaledContents(True)
        self.label_info_of_interest.setObjectName("label_info_of_interest")
        self.gridLayout_2.addWidget(self.label_info_of_interest, 22, 1, 1, 1)
        self.done_png = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.done_png.sizePolicy().hasHeightForWidth())
        self.done_png.setSizePolicy(sizePolicy)
        self.done_png.setMaximumSize(QtCore.QSize(25, 25))
        self.done_png.setText("")
        self.done_png.setPixmap(QtGui.QPixmap(":/plugins/oiv/config_files/png/interface/done.png"))
        self.done_png.setScaledContents(True)
        self.done_png.setObjectName("done_png")
        self.gridLayout_2.addWidget(self.done_png, 2, 1, 1, 1)
        self.label_filter = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_filter.sizePolicy().hasHeightForWidth())
        self.label_filter.setSizePolicy(sizePolicy)
        self.label_filter.setMaximumSize(QtCore.QSize(25, 25))
        self.label_filter.setText("")
        self.label_filter.setPixmap(QtGui.QPixmap(":/plugins/oiv/config_files/png/interface/filter.png"))
        self.label_filter.setScaledContents(True)
        self.label_filter.setObjectName("label_filter")
        self.gridLayout_2.addWidget(self.label_filter, 20, 1, 1, 1)
        self.filter_objecten = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.filter_objecten.setObjectName("filter_objecten")
        self.gridLayout_2.addWidget(self.filter_objecten, 20, 2, 1, 2)
        self.pan = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pan.sizePolicy().hasHeightForWidth())
        self.pan.setSizePolicy(sizePolicy)
        self.pan.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/plugins/oiv/config_files/png/pan.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pan.setIcon(icon)
        self.pan.setIconSize(QtCore.QSize(25, 25))
        self.pan.setObjectName("pan")
        self.gridLayout_2.addWidget(self.pan, 3, 3, 1, 1)
        self.filterframe = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.filterframe.sizePolicy().hasHeightForWidth())
        self.filterframe.setSizePolicy(sizePolicy)
        self.filterframe.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.filterframe.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.filterframe.setObjectName("filterframe")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.filterframe)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.checkVanaf = QtWidgets.QCheckBox(self.filterframe)
        self.checkVanaf.setObjectName("checkVanaf")
        self.gridLayout_3.addWidget(self.checkVanaf, 2, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.filterframe)
        self.label_2.setObjectName("label_2")
        self.gridLayout_3.addWidget(self.label_2, 0, 0, 1, 3)
        self.datum_vanaf = QtWidgets.QDateEdit(self.filterframe)
        self.datum_vanaf.setCalendarPopup(True)
        self.datum_vanaf.setObjectName("datum_vanaf")
        self.gridLayout_3.addWidget(self.datum_vanaf, 2, 1, 1, 2)
        self.filterBtn = QtWidgets.QPushButton(self.filterframe)
        self.filterBtn.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/plugins/oiv/config_files/png/filter.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.filterBtn.setIcon(icon1)
        self.filterBtn.setIconSize(QtCore.QSize(16, 16))
        self.filterBtn.setObjectName("filterBtn")
        self.gridLayout_3.addWidget(self.filterBtn, 5, 0, 1, 3)
        self.datum_tot = QtWidgets.QDateEdit(self.filterframe)
        self.datum_tot.setCalendarPopup(True)
        self.datum_tot.setObjectName("datum_tot")
        self.gridLayout_3.addWidget(self.datum_tot, 3, 1, 1, 2)
        self.checkSoort = QtWidgets.QCheckBox(self.filterframe)
        self.checkSoort.setObjectName("checkSoort")
        self.gridLayout_3.addWidget(self.checkSoort, 1, 0, 1, 1)
        self.checkTot = QtWidgets.QCheckBox(self.filterframe)
        self.checkTot.setObjectName("checkTot")
        self.gridLayout_3.addWidget(self.checkTot, 3, 0, 1, 1)
        self.objecttype = QtWidgets.QComboBox(self.filterframe)
        self.objecttype.setObjectName("objecttype")
        self.gridLayout_3.addWidget(self.objecttype, 1, 1, 1, 2)
        self.gridLayout_2.addWidget(self.filterframe, 8, 2, 1, 2)
        self.close_png = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.close_png.sizePolicy().hasHeightForWidth())
        self.close_png.setSizePolicy(sizePolicy)
        self.close_png.setMaximumSize(QtCore.QSize(25, 25))
        self.close_png.setText("")
        self.close_png.setPixmap(QtGui.QPixmap(":/plugins/oiv/config_files/png/interface/mode_off_on.png"))
        self.close_png.setScaledContents(True)
        self.close_png.setObjectName("close_png")
        self.gridLayout_2.addWidget(self.close_png, 0, 1, 1, 1)
        self.done = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.done.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.done.sizePolicy().hasHeightForWidth())
        self.done.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.done.setFont(font)
        self.done.setCheckable(True)
        self.done.setObjectName("done")
        self.gridLayout_2.addWidget(self.done, 2, 2, 1, 2)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        self.gridLayout_2.addItem(spacerItem, 5, 1, 1, 1)
        self.close_btn = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.close_btn.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.close_btn.sizePolicy().hasHeightForWidth())
        self.close_btn.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.close_btn.setFont(font)
        self.close_btn.setCheckable(True)
        self.close_btn.setObjectName("close_btn")
        self.gridLayout_2.addWidget(self.close_btn, 0, 2, 1, 2)
        self.tabWidget = QtWidgets.QTabWidget(self.scrollAreaWidgetContents)
        self.tabWidget.setEnabled(True)
        self.tabWidget.setToolTip("")
        self.tabWidget.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.tabWidget.setIconSize(QtCore.QSize(124, 48))
        self.tabWidget.setTabBarAutoHide(False)
        self.tabWidget.setObjectName("tabWidget")
        self.object = QtWidgets.QWidget()
        self.object.setObjectName("object")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.object)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.statusregelObject = QtWidgets.QLabel(self.object)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.statusregelObject.sizePolicy().hasHeightForWidth())
        self.statusregelObject.setSizePolicy(sizePolicy)
        self.statusregelObject.setWordWrap(True)
        self.statusregelObject.setObjectName("statusregelObject")
        self.verticalLayout_3.addWidget(self.statusregelObject)
        self.objectFrame = QtWidgets.QFrame(self.object)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.objectFrame.sizePolicy().hasHeightForWidth())
        self.objectFrame.setSizePolicy(sizePolicy)
        self.objectFrame.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.objectFrame.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.objectFrame.setLineWidth(0)
        self.objectFrame.setObjectName("objectFrame")
        self.verticalLayout_3.addWidget(self.objectFrame)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/plugins/oiv/config_files/png/repressief_object.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.tabWidget.addTab(self.object, icon2, "")
        self.bouwlaag = QtWidgets.QWidget()
        self.bouwlaag.setObjectName("bouwlaag")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.bouwlaag)
        self.verticalLayout.setObjectName("verticalLayout")
        self.statusregelBouwlaag = QtWidgets.QLabel(self.bouwlaag)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.statusregelBouwlaag.sizePolicy().hasHeightForWidth())
        self.statusregelBouwlaag.setSizePolicy(sizePolicy)
        self.statusregelBouwlaag.setWordWrap(True)
        self.statusregelBouwlaag.setObjectName("statusregelBouwlaag")
        self.verticalLayout.addWidget(self.statusregelBouwlaag)
        self.bouwlaagFrame = QtWidgets.QFrame(self.bouwlaag)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bouwlaagFrame.sizePolicy().hasHeightForWidth())
        self.bouwlaagFrame.setSizePolicy(sizePolicy)
        self.bouwlaagFrame.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.bouwlaagFrame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.bouwlaagFrame.setLineWidth(0)
        self.bouwlaagFrame.setObjectName("bouwlaagFrame")
        self.verticalLayout.addWidget(self.bouwlaagFrame)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/plugins/oiv/config_files/png/bouwlagen.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.tabWidget.addTab(self.bouwlaag, icon3, "")
        self.fakeTab = QtWidgets.QWidget()
        self.fakeTab.setObjectName("fakeTab")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.fakeTab)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.statusregel = QtWidgets.QLabel(self.fakeTab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.statusregel.sizePolicy().hasHeightForWidth())
        self.statusregel.setSizePolicy(sizePolicy)
        self.statusregel.setWordWrap(True)
        self.statusregel.setObjectName("statusregel")
        self.verticalLayout_4.addWidget(self.statusregel)
        spacerItem1 = QtWidgets.QSpacerItem(20, 0, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_4.addItem(spacerItem1)
        self.tabWidget.addTab(self.fakeTab, "")
        self.gridLayout_2.addWidget(self.tabWidget, 4, 1, 1, 3)
        self.verticalLayout_2.addLayout(self.gridLayout_2)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout.addWidget(self.scrollArea, 0, 0, 1, 1)
        OivObjectenDockWidgetBase.setWidget(self.dockWidgetContents)

        self.retranslateUi(OivObjectenDockWidgetBase)
        self.tabWidget.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(OivObjectenDockWidgetBase)

    def retranslateUi(self, OivObjectenDockWidgetBase):
        _translate = QtCore.QCoreApplication.translate
        OivObjectenDockWidgetBase.setWindowTitle(_translate("OivObjectenDockWidgetBase", "OIV"))
        self.info_of_interest.setText(_translate("OivObjectenDockWidgetBase", "Info of interest"))
        self.filter_objecten.setText(_translate("OivObjectenDockWidgetBase", "Filter"))
        self.checkVanaf.setText(_translate("OivObjectenDockWidgetBase", "Vanaf:"))
        self.label_2.setText(_translate("OivObjectenDockWidgetBase", "Filter op datum"))
        self.datum_vanaf.setDisplayFormat(_translate("OivObjectenDockWidgetBase", "dd-MM-yyyy"))
        self.datum_tot.setDisplayFormat(_translate("OivObjectenDockWidgetBase", "dd-MM-yyyy"))
        self.checkSoort.setText(_translate("OivObjectenDockWidgetBase", "Soort:"))
        self.checkTot.setText(_translate("OivObjectenDockWidgetBase", "Tot:"))
        self.done.setText(_translate("OivObjectenDockWidgetBase", "Gereed"))
        self.close_btn.setText(_translate("OivObjectenDockWidgetBase", "Sluit OIV"))
        self.statusregelObject.setText(_translate("OivObjectenDockWidgetBase", "{......Statusregel.....}"))
        self.tabWidget.setTabToolTip(self.tabWidget.indexOf(self.object), _translate("OivObjectenDockWidgetBase", "Klik voor planvorming Object / terrein / gebied"))
        self.statusregelBouwlaag.setText(_translate("OivObjectenDockWidgetBase", "{......Statusregel.....}"))
        self.tabWidget.setTabToolTip(self.tabWidget.indexOf(self.bouwlaag), _translate("OivObjectenDockWidgetBase", "Klik voor planvorming Bouwlaag / pand"))
        self.statusregel.setText(_translate("OivObjectenDockWidgetBase", "{......Statusregel.....}"))