# -*- coding: utf-8 -*-
"""
/***************************************************************************
 oiv
                                 A QGIS plugin
 place oiv objects
                             -------------------
        begin                : 2017-11-14
        copyright            : (C) 2017 by Joost Deen
        email                : j.deen@safetyct.com
        git sha              : $Format:%H$
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load oiv class from file oiv.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .oiv import oiv
    return oiv(iface)
