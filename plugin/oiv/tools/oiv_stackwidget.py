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
from qgis.PyQt.QtWidgets import QDockWidget
from qgis.gui import QgsAttributeEditorContext, QgsAttributeForm
from qgis.core import QgsFeatureRequest
from qgis.utils import iface

FORM_CLASS, _ = uic.loadUiType(os.path.join(
    os.path.dirname(__file__), 'oiv_stackwidget.ui'))

class oivStackWidget(QDockWidget, FORM_CLASS):
    """open any feature form as stackwidget in OOIV pluging"""
    attributeForm = None
    parentWidget = None

    def __init__(self, parent=None):
        """Constructor."""
        super(oivStackWidget, self).__init__(parent)
        self.iface = iface
        self.setupUi(self)

    def open_feature_form(self, ilayer, ifeature):
        """"open feature form based on clicked object on the canvas"""
        ilayer.startEditing()
        context = QgsAttributeEditorContext()
        context.setVectorLayerTools(self.iface.vectorLayerTools())        
        self.attributeForm = QgsAttributeForm(ilayer, ifeature, context)
        self.stackedWidget.addWidget(self.attributeForm)
        self.stackedWidget.setCurrentWidget(self.attributeForm)
        self.iface.setActiveLayer(ilayer)        
        self.terug.clicked.connect(lambda: self.close_stacked(ilayer, ifeature))

    def close_stacked(self, ilayer, ifeature):
        """close feature form and save changes"""
        self.attributeForm.save()
        self.terug.clicked.disconnect()
        ilayer.commitChanges()
        self.attributeForm.close()
        del self.attributeForm
        self.attributeForm = None
        if ilayer.name() == "Objecten":
            request = QgsFeatureRequest().setFilterExpression("id = " \
                             + str(ifeature["id"]))
            objectFeature = next(ilayer.getFeatures(request))
            self.parentWidget.formelenaam.setText(objectFeature["formelenaam"])
        self.close()
        try:
            self.parentWidget.show()
            self.iface.actionPan().trigger()
        except: # pylint: disable=bare-except
            pass
        del self
