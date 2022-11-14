import qgis.core as QC
from PyQt5.QtXml import QDomDocument

def load_composer(output_folder, objectOfBouwlaag, filterString, fileName):
    layoutName = None
    project = QC.QgsProject.instance()
    if objectOfBouwlaag == 'object':
        layoutName = 'print_object_pdf_A4'
        #layout = project.layoutManager().layoutByName(layoutName)
    else:
        layoutName = 'print_bouwlagen_pdf_A4'
        #layout = project.layoutManager().layoutByName(layoutName)
        #layout.itemById('title').setText("Bouwlaag: {}".format(fileName.split('_')[2]))
    layout, atlas = load_layout(layoutName, project, filterString)
    print_atlas(layout, atlas, output_folder, fileName)

def print_atlas(layout, atlas, output_folder, fileName):
    if atlas.beginRender():
        while atlas.next():
            exporter = QC.QgsLayoutExporter(layout)
            settings = QC.QgsLayoutExporter.PdfExportSettings()
            fileName = fileName + '.pdf'
            filePath = output_folder + '/' + fileName
            exporter.exportToPdf(filePath, settings)
        atlas.endRender()
    return "print_finished"

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
