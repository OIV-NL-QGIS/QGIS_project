import qgis.PyQt.QtCore as PQtC
import qgis.core as QC
import qgis.gui as QG

def load_composer(layout_name, output_folder):
    project = QC.QgsProject.instance()
    layout = project.layoutManager().layoutByName(layout_name)
    exporter = QC.QgsLayoutExporter(layout)
    settings = QC.QgsLayoutExporter.ImageExportSettings()
    exporter.exportToPdf(layout.atlas(), output_folder, 'tif', settings)