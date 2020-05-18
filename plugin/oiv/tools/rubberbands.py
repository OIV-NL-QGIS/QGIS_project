from math import cos, sin, radians
from qgis.gui import QgsRubberBand
from qgis.core import QgsPointXY

def init_rubberband(color, lineStyle, alphaF, width, bandType, canvas):
    """initiate the rubberbands"""
    rubberBand = QgsRubberBand(canvas, bandType)
    rubberBand.setStrokeColor(color)
    color.setAlpha(alphaF)
    rubberBand.setFillColor(color)
    rubberBand.setLineStyle(lineStyle)
    rubberBand.setWidth(width)
    return rubberBand

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
