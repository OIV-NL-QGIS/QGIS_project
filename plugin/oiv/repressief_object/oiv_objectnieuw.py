"""
/***************************************************************************
 oiv
                                 A QGIS plugin
 place oiv objects
                              -------------------
        begin                : 2019-08-15
        git sha              : $Format:%H$
        copyright            : (C) 2019 by Joost Deen
        email                : j.deen@safetyct.com
        versie               : 2.9.93
 ***************************************************************************/
/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""

import os

from qgis.PyQt import uic
from qgis.PyQt.QtCore import Qt
from qgis.PyQt.QtWidgets import QDockWidget

from qgis.core import QgsFeatureRequest, QgsFeature, QgsGeometry
from qgis.utils import iface

from ..tools.utils_core import user_input_label, getlayer_byname, write_layer, read_settings

FORM_CLASS, _ = uic.loadUiType(os.path.join(
    os.path.dirname(__file__), 'oiv_objectnieuw_widget.ui'))

class oivObjectNieuwWidget(QDockWidget, FORM_CLASS):

    canvas = None
    newObject = None
    drawLayer = None
    basewidget = None
    objectwidget = None
    mapTool = None

    def __init__(self, parent=None):
        """Constructor."""
        super(oivObjectNieuwWidget, self).__init__(parent)
        self.setupUi(self)
        self.iface = iface
        self.opslaan.clicked.connect(self.run_tekenen)
        self.terug.clicked.connect(self.close_objectnieuw_show_base)

    def close_objectnieuw_show_base(self):
        self.close()
        try:
            del self.objectwidget
        except: # pylint: disable=bare-except
            pass
        self.basewidget.show()
        del self

    #place new object (i-tje)
    def run_tekenen(self):
        if self.bron.text() == 'BAG':
            runLayer = "Objecten"
        else:
            runLayer = "Objecten BGT"
        self.drawLayer = getlayer_byname(runLayer)
        self.canvas.setMapTool(self.mapTool)
        self.mapTool.canvasClicked.connect(self.place_feature)

    #construct the feature and save
    def place_feature(self, point):
        childFeature = QgsFeature()
        self.iface.setActiveLayer(self.drawLayer)
        #set geometry from the point clicked on the canvas
        childFeature.setGeometry(QgsGeometry.fromPointXY(point))
        foreignKey = self.identificatienummer.text()
        buttonCheck = self.get_attributes(foreignKey, childFeature)
        #return of new created feature id
        if buttonCheck != 'Cancel':
            newFeatureId = write_layer(self.drawLayer, childFeature)
            tempFeature = QgsFeature()
            self.newObject = newFeatureId
            request = QgsFeatureRequest().setFilterExpression('"id" = ' + str(self.newObject))
            tempFeature = next(self.drawLayer.getFeatures(request))
            #with new created feature run existing object widget
            self.run_objectgegevens(tempFeature, newFeatureId)
        else:
            self.iface.actionPan().trigger()

    #get the right attributes from user
    def get_attributes(self, foreignKey, childFeature):
        query = "SELECT foreign_key, input_label, question, label_required\
             FROM config_object WHERE child_layer = '{}'".format(self.drawLayer.name())
        attrs = read_settings(query, False)
        labelTekst = user_input_label(attrs[3], attrs[2])
        if labelTekst != 'Cancel':
            fields = self.drawLayer.fields()
            childFeature.initAttributes(fields.count())
            childFeature.setFields(fields)
            if attrs[1] != '':
                childFeature[attrs[1]] = labelTekst
            if attrs[0] != '':
                childFeature[attrs[0]] = foreignKey
            childFeature["bron"] = self.bron.text()
            childFeature["bron_tabel"] = self.bron_table.text()
            return childFeature
        else:
            return 'Cancel'

    def run_objectgegevens(self, tempFeature, objectId):
        """continue to existing object woth the newly created feature and already searched address"""
        self.objectwidget.drawLayer = getlayer_byname('Objecten')
        self.objectwidget.object_id.setText(str(objectId))
        self.objectwidget.formelenaam.setText(tempFeature["formelenaam"])
        self.iface.addDockWidget(Qt.RightDockWidgetArea, self.objectwidget)
        self.objectwidget.initActions()
        self.objectwidget.show()
        self.iface.actionPan().trigger()
        self.close()
        del self.objectwidget
        del self
