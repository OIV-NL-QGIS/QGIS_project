import os
import qgis.PyQt.QtCore as PQtC
import qgis.core as QC
import qgis.gui as QG

def load_composer():
    project = QC.QgsProject.instance()
    
    layout_name = 'print_pdf_A3'
    output_folder = 'D:/testprint/'
    layout = project.layoutManager().layoutByName(layout_name)

    atlas = layout.atlas()
    atlas.setFilterExpression('"object_id"=1004')
    atlas.filterFeatures()
    atlas.updateFeatures()
    
    print_atlas(layout, atlas, output_folder)

def print_atlas(layout, atlas, output_folder):
    if atlas.beginRender():
        while atlas.next():
            exporter = QC.QgsLayoutExporter(layout)
            settings = QC.QgsLayoutExporter.PdfExportSettings()
            fileName = atlas.currentFilename() + '.pdf'
            print(fileName)
            filePath = output_folder + fileName
            exporter.exportToPdf(filePath, settings)
        atlas.endRender()