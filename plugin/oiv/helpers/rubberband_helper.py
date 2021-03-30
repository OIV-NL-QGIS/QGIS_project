"""RubberBand style helpers"""
from math import sin, cos, radians
from qgis.gui import QgsRubberBand, QgsVertexMarker
from qgis.core import QgsPointXY
from qgis.PyQt.QtGui import QColor
from .qt_helper import getQtLineStyle, getWKBType

# RubberBand styles
RBSTYLES = {
    "grid": {
        'strokecolor': QColor('red'),
        'fillcolor': QColor('red'),
        'linestyle': getQtLineStyle('solid'),
        'alphaF': 10,
        'strokewidth': 1,
    },
    # maptool rubberband styles
    "drawn": {
        'strokecolor': QColor('red'),
        'fillcolor': QColor('red'),
        'linestyle': getQtLineStyle('solid'),
        'alphaF': 50,
        'strokewidth': 1,
    },
    "newpoint": {
        'strokecolor': QColor('red'),
        'fillcolor': QColor('red'),
        'linestyle': getQtLineStyle('dash'),
        'alphaF': 25,
        'strokewidth': 1,
    },
    "drawinghelpers": {
        'strokecolor': QColor('blue'),
        'fillcolor': QColor('blue'),
        'linestyle': getQtLineStyle('dash'),
        'alphaF': 255,
        'strokewidth': 1,
    },
    # move and rotate points rubberband styles
    "moveandrotatepoint": {
        'strokecolor': QColor('black'),
        'fillcolor': QColor('black'),
        'linestyle': getQtLineStyle('dash'),
        'alphaF': 25,
        'strokewidth': 1,
    },
}

VERTEXMARKERSTYLES = {
    "movepoint": {
        'color': QColor('blue'),
        'iconsize': 5,
        'icontype': QgsVertexMarker.ICON_X,
        'penwidth': 3,
    },
    "snappoint": {
        'color': QColor('255, 0, 255'),
        'iconsize': 8,
        'icontype': QgsVertexMarker.ICON_X,
        'penwidth': 5,
    },
}

def init_rubberband(styleName, canvas, rbType):
    """initiate the rubberbands"""
    rbStyle = RBSTYLES[styleName]
    rubberBand = QgsRubberBand(canvas, getWKBType(rbType))
    rubberBand.setStrokeColor(rbStyle["strokecolor"])
    rbStyle["fillcolor"].setAlpha(rbStyle["alphaF"])
    rubberBand.setFillColor(rbStyle["fillcolor"])
    rubberBand.setLineStyle(rbStyle["linestyle"])
    rubberBand.setWidth(rbStyle["strokewidth"])
    return rubberBand

def init_vertexmarker(styleName, canvas):
    vmStyle = VERTEXMARKERSTYLES[styleName]
    vertexmarker = QgsVertexMarker(canvas)
    vertexmarker.setColor(vmStyle["color"])
    vertexmarker.setIconSize(vmStyle["iconsize"])
    vertexmarker.setIconType(vmStyle["icontype"])
    vertexmarker.setPenWidth(vmStyle["penwidth"])
    vertexmarker.show()
    return vertexmarker

def calculate_perpendicularbands(point, angle):
    """bereken de haakse lijnen op basis van de gesnapte feature"""
    length = 100
    x1 = point.x() + length * sin(radians(angle))
    y1 = point.y() + length * cos(radians(angle))
    x2 = point.x() + length * sin(radians(angle + 180))
    y2 = point.y() + length * cos(radians(angle + 180))
    x3 = point.x() + length * sin(radians(angle + 90))
    y3 = point.y() + length * cos(radians(angle + 90))
    x4 = point.x() + length * sin(radians(angle + 270))
    y4 = point.y() + length * cos(radians(angle + 270))
    return QgsPointXY(x1, y1), QgsPointXY(x2, y2), QgsPointXY(x3, y3), QgsPointXY(x4, y4)
