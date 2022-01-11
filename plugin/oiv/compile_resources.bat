@echo off
call "C:\Program Files\QGIS 3.16\bin\o4w_env.bat"
call "C:\Program Files\QGIS 3.16\bin\qt5_env.bat"
call "C:\Program Files\QGIS 3.16\bin\py3_env.bat"

pyrcc5.bat -o resources.py resources.qrc
pause