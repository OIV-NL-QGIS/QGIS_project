@echo off
call "C:\Program Files\QGIS 3.22\bin\o4w_env.bat"
call "C:\Program Files\QGIS 3.22\bin\qt5_env.bat"
call "C:\Program Files\QGIS 3.22\bin\py3_env.bat"

pyrcc5.bat -o resources.py resources.qrc
pause