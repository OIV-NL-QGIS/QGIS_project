from qgis.PyQt.QtCore import QPoint
import qgis.core as QC

import oiv.helpers.constants as PC
import oiv.helpers.rubberband_helper as RH

#repressief object constants
ROSNAPSYMBOLS = ['32', '47', '148', '150', '152', '301',
                 'Algemeen', 'Voorzichtig', 'Waarschuwing', 'Gevaar']
ROSNAPLAYERS = ["Object terrein", "Isolijnen", "Bereikbaarheid", "Sectoren"]

#bouwlaag constants
BLSNAPLAYERS = [PC.PAND["bouwlaaglayername"], "Bouwkundige veiligheidsvoorzieningen", "Ruimten"]
BLSNAPSYMBOLS = ['1', '10', '32', '47', '148', '149', '150', '151', '152', '701', '702', '703', '704',
                 '1011', 'Algemeen', 'Voorzichtig', 'Waarschuwing', 'Gevaar']

def calcTolerance(mapTool, pos):
    """calculate snap tolerance"""
    pt1 = QPoint(pos.x(), pos.y())
    pt2 = QPoint(pos.x() + 20, pos.y())
    layerPt1 = mapTool.toLayerCoordinates(mapTool.layer, pt1)
    layerPt2 = mapTool.toLayerCoordinates(mapTool.layer, pt2)
    tolerance = layerPt2.x() - layerPt1.x()
    return tolerance

def snap_to_point(mapTool, pos, layerPt):
    """calculate if there is a point to snap to within the tolerance"""
    tolerance = pow(calcTolerance(mapTool, pos), 2)
    minDist = tolerance
    snapPoint = None
    if mapTool.vertexmarker is None:
        mapTool.vertexmarker = RH.init_vertexmarker("identify", mapTool.canvas)
    for geom in mapTool.possibleSnapFeatures:
        closestPoint = layerPt.distance(geom.asPoint())
        if closestPoint < minDist and closestPoint >= 0:
            minDist = closestPoint
            snapPoint = geom.asPoint()
    if snapPoint and snapPoint != QC.QgsPointXY(0, 0):
        return snapPoint
