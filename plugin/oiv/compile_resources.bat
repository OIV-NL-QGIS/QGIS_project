@echo off
call "D:\ProgramFiles\QGIS340\bin\o4w_env.bat"
call "D:\ProgramFiles\QGIS340\bin\qt5_env.bat"
call "D:\ProgramFiles\QGIS340\bin\py3_env.bat"

@echo on
"D:\ProgramFiles\QGIS340\apps\Python312\Scripts\pyrcc5.exe" -o resources.py resources.grc
pause