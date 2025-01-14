import os
import qgis.core as QC
import qgis.PyQt.QtCore as PQtC
from PyQt5.QtXml import QDomDocument


import oiv.helpers.utils_core as UC
import oiv.helpers.messages as MSG
import oiv.helpers.constants as PC

def load_composer(output_folder, objectOfBouwlaag, fileName, byWhichLayer, rotation, legenda):
    layoutName = None
    reply = check_if_file_exists(output_folder, fileName)
    suffix = ''
    if legenda:
        suffix = '_legenda'
    if reply == 'resume':
        project = QC.QgsProject.instance()
        if objectOfBouwlaag == 'object':
            layoutName = 'print_object_pdf_A4' + suffix
            layout, atlas = load_layout(layoutName, project, byWhichLayer, rotation, legenda)
        else:
            layoutName = 'print_bouwlagen_pdf_A4' + suffix
            layout, atlas = load_layout(layoutName, project, byWhichLayer, rotation, legenda)
            layout.itemById('title').setText("Bouwlaag: {}".format(fileName.split('_')[2]))
        rep = print_atlas(layout, atlas, output_folder, fileName)
        return rep, output_folder
    elif reply == 'stop':
        return 'print_canceld', ''

def print_atlas(layout, atlas, output_folder, fileName):
    if atlas.beginRender():
        while atlas.next():
            exporter = QC.QgsLayoutExporter(layout)
            settings = QC.QgsLayoutExporter.PdfExportSettings()
            settings.flags = QC.QgsLayoutRenderContext.Flag(QC.QgsLayoutRenderContext.FlagHideCoverageLayer |                              
                        QC.QgsLayoutRenderContext.FlagAntialiasing |
                        QC.QgsLayoutRenderContext.FlagUseAdvancedEffects)
            fileName = fileName + '.pdf'
            filePath = output_folder + '/' + fileName
            exporter.exportToPdf(filePath, settings)
        atlas.endRender()
    return "print_finished"

def check_if_file_exists(output_folder, fileName):
    fileName = fileName + '.pdf'
    filePath = output_folder + '/' + fileName
    if os.path.isfile(filePath):
        reply = MSG.showMsgBox('fileAlreadyExists')
        if reply:
            try:
                os.remove(filePath)
                return 'resume'
            except OSError: 
                return 'stop'
        else:
            return 'stop'
    else:
        return 'resume'

def load_layout(layoutName, project, byWhichLayer, rotation, legenda):
    layout = QC.QgsPrintLayout(project)
    if byWhichLayer == 'polygon':
        coverageLayer = UC.getlayer_byname('tempPrintCoverage')
    else:
        coverageLayer = UC.getlayer_byname(PC.OBJECT["terreinlayername"])
    absolutePath = project.readPath("./")
    templateFile = absolutePath + '/qpt/' + layoutName + '.qpt'
    with open(templateFile) as f:
        templateContent = f.read()
    f.close()
    doc = QDomDocument()
    doc.setContent(templateContent)
    items, ok = layout.loadFromTemplate(doc, QC.QgsReadWriteContext())
    for item in layout.items():
        try:
            if item.id() == 'legenda':
                item.setPicturePath(absolutePath + '/qpt/' + legenda + '_legenda.pdf')
        except:
            None
        if isinstance(item, QC.QgsLayoutItemMap):
            item.setMapRotation(rotation)
    atlas = layout.atlas()
    atlas.setCoverageLayer(coverageLayer)
    atlas.filterFeatures()
    atlas.updateFeatures()
    return layout, atlas

def create_temp_print_layer(identifier):
    tempPrintLayer = QC.QgsVectorLayer("Polygon?crs=epsg:28992", "tempPrintCoverage", "memory")
    if identifier == 'pand_id':
        field = QC.QgsField(identifier, PQtC.QVariant.String)
    else:
        field = QC.QgsField(identifier, PQtC.QVariant.Int)
    tempPrintLayer.dataProvider().addAttributes([field])
    tempPrintLayer.updateFields()
    QC.QgsProject.instance().addMapLayer(tempPrintLayer, True)
    return tempPrintLayer
