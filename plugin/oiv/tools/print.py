import os
import qgis.PyQt.QtCore as PQtC
import qgis.core as QC
import qgis.gui as QG

def load_composer(output_folder, layout_name, filterString):
    project = QC.QgsProject.instance()
    
    layout = project.layoutManager().layoutByName(layout_name)

    atlas = layout.atlas()
    atlas.setFilterExpression(filterString)
    atlas.filterFeatures()
    atlas.updateFeatures()
    
    print_atlas(layout, atlas, output_folder)

def print_atlas(layout, atlas, output_folder):
    if atlas.beginRender():
        while atlas.next():
            exporter = QC.QgsLayoutExporter(layout)
            settings = QC.QgsLayoutExporter.PdfExportSettings()
            fileName = atlas.currentFilename() + '.pdf'
            filePath = output_folder + '/' + fileName
            exporter.exportToPdf(filePath, settings)
        atlas.endRender()
