from qgis.PyQt.QtCore import Qt, QSize
from qgis.PyQt.QtGui import QIcon, QFont
from qgis.core import QgsWkbTypes
import qgis.PyQt.QtWidgets as PQtW
from .constants import PLUGIN

def getQtLineStyle(style):
    """translate to Qt linestyle"""
    allLineStyles = {
        'solid': Qt.SolidLine,
        'dash': Qt.DashLine,
        'dot': Qt.DotLine
    }
    return allLineStyles[style]

def getWKBType(wkbType):
    """translate text to WKBType"""
    allTypes = {
        'point': QgsWkbTypes.PointGeometry,
        'line': QgsWkbTypes.LineGeometry,
        'polygon': QgsWkbTypes.PolygonGeometry
    }
    return allTypes[wkbType]

def getWidgetType():
    """get QtWidgetType for new Widget"""
    return Qt.RightDockWidgetArea

def getTitleBar():
    """create titlebar for dockwidget"""
    titleBar = PQtW.QWidget()
    layout = PQtW.QHBoxLayout()
    font = QFont("Arial", 10, QFont.Bold)
    label = create_label(PLUGIN["name"], layout, font)
    titleBar.setLayout(layout)
    titleBar.setWindowFlag(Qt.WindowMaximizeButtonHint, True)
    return titleBar

def create_label(labelText, layout, font=None, row=None, column=None):
    """create QLabel and add it to layout"""
    tempLabel = PQtW.QLabel()
    tempLabel.setText(labelText)
    if isinstance(font, QFont):
        tempLabel.setFont(font)
    if isinstance(layout, PQtW.QGridLayout):
        layout.addWidget(tempLabel, row, column)
    else:
        layout.addWidget(tempLabel)
    return tempLabel

def create_combobox(items, layout, row=None, column=None):
    """create QComboCox and add it to layout"""
    tempCombo = PQtW.QComboBox()
    tempCombo.addItems(items)
    if isinstance(layout, PQtW.QGridLayout):
        layout.addWidget(tempCombo, row, column)
    else:
        layout.addWidget(tempCombo)
    return tempCombo

def create_spacer():
    """create QSpacer and add it to layout"""
    verticalSpacer = PQtW.QSpacerItem(0, 0, PQtW.QSizePolicy.Minimum, PQtW.QSizePolicy.Expanding)
    return verticalSpacer

def create_radio_button(labelText, layout, row=None, column=None):
    """create QRadioButton and add it to layout"""
    tempRadioB = PQtW.QRadioButton()
    tempRadioB.setText(labelText)
    if isinstance(layout, PQtW.QGridLayout):
        layout.addWidget(tempRadioB, row, column)
    else:
        layout.addWidget(tempRadioB)
    return tempRadioB

def create_pushbutton(typeBtn, content, layout, size=None, row=None, column=None):
    """create QPushButton with Icon or Text and add it to layout"""
    tempBtn = PQtW.QPushButton()
    if typeBtn == "Icon":
        tempBtn.setIcon(QIcon(content))
    else:
        tempBtn.setText(content)
    if size:
        tempBtn.setFixedSize(QSize(size, size))
    if isinstance(layout, PQtW.QGridLayout):
        layout.addWidget(tempBtn, row, column)
    else:
        layout.addWidget(tempBtn)
    return tempBtn

def create_line_edit(layout, row=None, column=None):
    """create QLineEdit and add it to layout"""
    tempLine = PQtW.QLineEdit()
    if isinstance(layout, PQtW.QGridLayout):
        layout.addWidget(tempLine, row, column)
    else:
        layout.addWidget(tempLine)
    return tempLine