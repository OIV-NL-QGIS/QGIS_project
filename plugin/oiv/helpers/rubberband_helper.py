"""RubberBand style helpers"""
from math import sin, cos, radians
from qgis.gui import QgsRubberBand, QgsVertexMarker
import qgis.core as QC
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

PRINTLAYERSTYLE = {
    'strokecolor': QColor('red'),
    'fillcolor': QColor('red'),
    'linestyle': getQtLineStyle('dash'),
    'alphaF': 0.10,
    'strokewidth': 1,
}

VERTEXMARKERSTYLES = {
    "movepoint": {
        'color': QColor('magenta'),
        'iconsize': 5,
        'icontype': QgsVertexMarker.ICON_X,
        'penwidth': 3,
    },
    "snappoint": {
        'color': QColor('magenta'),
        'iconsize': 8,
        'icontype': QgsVertexMarker.ICON_X,
        'penwidth': 5,
    },
    "centroid": {
        'color': QColor('magenta'),
        'iconsize': 12,
        'icontype': QgsVertexMarker.ICON_X,
        'penwidth': 5,
    },
    "identify": {
        'color': QColor('magenta'),
        'iconsize': 6,
        'icontype': QgsVertexMarker.ICON_CIRCLE,
        'penwidth': 5,
    },
}

def resetRB(rubberBand, WKBtype):
    rubberBand.reset(WKBtype)

def set_printcoverage_style(iface, layer):
    single_symbol_renderer = layer.renderer()
    symbol = single_symbol_renderer.symbol()
    color = PRINTLAYERSTYLE["fillcolor"]
    color.setAlpha(10)
    symbol.setColor(color)
    symbol.symbolLayer(0).setStrokeColor(PRINTLAYERSTYLE["strokecolor"])
    symbol.symbolLayer(0).setStrokeWidth(PRINTLAYERSTYLE["strokewidth"])
    layer.triggerRepaint()
    iface.layerTreeView().refreshLayerSymbology(layer.id())

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
    return QC.QgsPointXY(x1, y1), QC.QgsPointXY(x2, y2), QC.QgsPointXY(x3, y3), QC.QgsPointXY(x4, y4)
