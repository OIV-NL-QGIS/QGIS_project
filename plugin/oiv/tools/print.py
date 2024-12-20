import os
import qgis.core as QC
from PyQt5.QtXml import QDomDocument

import oiv.helpers.messages as MSG

def load_composer(output_folder, objectOfBouwlaag, filterString, fileName):
    layoutName = None
    reply = check_if_file_exists(output_folder, fileName)
    if reply == 'resume':
        project = QC.QgsProject.instance()
        if objectOfBouwlaag == 'object':
            layoutName = 'print_object_pdf_A4'
            layout, atlas = load_layout(layoutName, project, filterString)
        else:
            layoutName = 'print_bouwlagen_pdf_A4'
            layout, atlas = load_layout(layoutName, project, filterString)
            layout.itemById('title').setText("Bouwlaag: {}".format(fileName.split('_')[2]))
        print_atlas(layout, atlas, output_folder, fileName)
    return 'print_canceld', ''

def print_atlas(layout, atlas, output_folder, fileName):
    if atlas.beginRender():
        while atlas.next():
            exporter = QC.QgsLayoutExporter(layout)
            settings = QC.QgsLayoutExporter.PdfExportSettings()
            fileName = fileName + '.pdf'
            filePath = output_folder + '/' + fileName
            exporter.exportToPdf(filePath, settings)
        atlas.endRender()
    return "print_finished", output_folder

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
        return 'resume'

def load_layout(layoutName, project, filterString):
    layout = QC.QgsPrintLayout(project)
    absolutePath = project.readPath("./")
    templateFile = absolutePath + '/qpt/' + layoutName + '.qpt'
    with open(templateFile) as f:
        templateContent = f.read()
    f.close()
    doc = QDomDocument()
    doc.setContent(templateContent)
    items, ok = layout.loadFromTemplate(doc, QC.QgsReadWriteContext())
    atlas = layout.atlas()
    atlas.setFilterExpression(filterString)
    atlas.filterFeatures()
    atlas.updateFeatures()
    return layout, atlas
