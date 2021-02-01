from qgis.PyQt.QtCore import Qt #pylint: disable=import-error
from qgis.core import QgsWkbTypes #pylint: disable=import-error

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
    return Qt.RightDockWidgetArea
