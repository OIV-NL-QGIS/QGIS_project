import qgis.core as QC

def load_composer(output_folder, objectOfBouwlaag, filterString, fileName):
    project = QC.QgsProject.instance()
    if objectOfBouwlaag == 'object':
        layoutName = 'print_object_pdf_A4'
        layout = project.layoutManager().layoutByName(layoutName)
    else:
        layoutName = 'print_bouwlagen_pdf_A4'
        layout = project.layoutManager().layoutByName(layoutName)
        layout.itemById('title').setText("Bouwlaag: {}".format(fileName.split('_')[2]))
    atlas = layout.atlas()
    atlas.setFilterExpression(filterString)
    atlas.filterFeatures()
    atlas.updateFeatures()
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
