/**
 * Copyright (c) 2020 SafetyCT - https://www.safetyct.com
 * Copyright (c) 2016-2017 Baas geo-information - www.baasgeo.com

 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *    http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 *
 * Author: Bart Baas <info@baasgeo.com> and Joost Deen <j.deen@safetyct.com>
 */
 
; Define your application name
!define APPNAME "OIV"
!define STAD "Zaandam"
!define BUILDTYPE ""
!define APPTITLE "Operationele Informatie Voorziening"
!define COMPANY "Safety Consulting and Technology"

!define VERSION 3.4.3
!define PLUGINVERSION 3.4.3
!define QGISVERSION "QGIS322"

!define APPNAMEANDVERSION "${APPNAME} ${VERSION} ${BUILDTYPE}"
!define WEBSITE "https://www.safetyct.com"
!define REG_APPSETTINGS "Software\SafetyCT\${APPNAME}"
!define REG_UNINSTALL "Software\Microsoft\Windows\CurrentVersion\Uninstall\${APPNAME}"
!define REG_ENVIRONMENT "SYSTEM\CurrentControlSet\Control\Session Manager\Environment"

; Might be the same as !define
Var Host
Var Dbname
Var Port
Var GeoserverUrl
Var GeoserverBron
Var DbUser
Var DbPassword
Var GeoserverUser
Var GeoserverPassword
Var HostTest
Var DbnameTest
Var PortTest
Var DbUserTest
Var DbPasswordTest
Var PluginInstallDir
Var PluginDir

; Main Install settings
Name "${APPNAMEANDVERSION}"
BrandingText "${WEBSITE}"
;InstallDir "$APPDATA\${APPNAME}-${VERSION}"
OutFile "output\${QGISVERSION}-${APPNAME}-${VERSION}${BUILDTYPE}-${STAD}.exe"

; Compression options
CRCCheck on

; For Vista
RequestExecutionLevel admin

; Plugins
!include MUI2.nsh ; Modern interface
!include StrFunc.nsh ; String functions
; Need to load this manually from StrFunc
${StrRep}
!include LogicLib.nsh ; ${If} ${Case} etc.
!include nsDialogs.nsh ; For Custom page layouts (Radio buttons etc)
!include winmessages.nsh ; Include for some of the windows messages defines
!include TextFunc.nsh ; For ConfigWrite functions
!include Sections.nsh

; Version Information (Version tab for EXE properties)
VIProductVersion "${VERSION}.0"
VIAddVersionKey ProductName "${APPTITLE}"
VIAddVersionKey FileDescription "${APPNAME} Installer"
VIAddVersionKey ProductVersion "${VERSION}"
VIAddVersionKey FileVersion "${VERSION}"
VIAddVersionKey CompanyName "${COMPANY}"
VIAddVersionKey LegalCopyright "${COMPANY}"
VIAddVersionKey Comments "${WEBSITE}"

; Interface Settings
!define MUI_ICON "pictogram.ico"
!define MUI_UNICON "${NSISDIR}\Contrib\Graphics\Icons\win-uninstall.ico"
!define MUI_HEADERIMAGE
!define MUI_HEADERIMAGE_RIGHT
!define MUI_HEADERIMAGE_BITMAP header.bmp
!define MUI_WELCOMEFINISHPAGE_BITMAP side_left.bmp

; "Are you sure you wish to cancel" popup.
!define MUI_ABORTWARNING

; Optional text settings here
!define MUI_FINISHPAGE_LINK " Installer created and maintained by ${COMPANY}"
!define MUI_FINISHPAGE_LINK_LOCATION "${WEBSITE}"

; Install Page order
; This is the main list of installer things to do 
!insertmacro MUI_PAGE_WELCOME                                 ; Hello
Page custom CheckUserType                                     ; Die if not admin
!insertmacro MUI_PAGE_LICENSE "license.txt"                   ; Show license
!insertmacro MUI_PAGE_COMPONENTS							                ; Components page
Page custom nsDialogHost nsDialogHostLeave					          ; Set db prod server connection
Page custom nsDialogHostTest nsDialogHostTestLeave					  ; Set db test server connection
Page custom nsDialogWFS nsDialogWFSLeave					            ; Set wfs server connection
Page custom nsDialogPluginDir nsDialogPluginDirLeave					; Set plugin install directory
Page custom Ready                                             ; Summary page
!insertmacro MUI_PAGE_INSTFILES                               ; Actually do the install
!insertmacro MUI_PAGE_FINISH                                  ; Done

; Uninstall Page order
!insertmacro MUI_UNPAGE_CONFIRM   ; Are you sure you wish to uninstall?
!insertmacro MUI_UNPAGE_INSTFILES ; Do the uninstall

; Set languages (first is default language)
!insertmacro MUI_LANGUAGE "English"
!insertmacro MUI_RESERVEFILE_LANGDLL

; Install options page headers
LangString TEXT_READY_TITLE ${LANG_ENGLISH} "Ready to Install"
LangString TEXT_READY_SUBTITLE ${LANG_ENGLISH} "${APPNAME} is ready to be installed"
LangString TEXT_CREDS_TITLE ${LANG_ENGLISH} "${APPNAME} Administrator"
LangString TEXT_CREDS_SUBTITLE ${LANG_ENGLISH} "Set administrator credentials"
LangString TEXT_HOST_TITLE ${LANG_ENGLISH} "${APPNAME} Web Server Host"
LangString TEXT_HOST_SUBTITLE ${LANG_ENGLISH} "Set the host that ${APPNAME} will respond on"

; Check the user type, and quit if it's not an administrator.
; Taken from Examples/UserInfo that ships with NSIS.
Function CheckUserType
  ClearErrors
  UserInfo::GetName
  IfErrors Win9x
  Pop $0
  UserInfo::GetAccountType
  Pop $1
  StrCmp $1 "Admin" Admin NoAdmin

  NoAdmin:
    MessageBox MB_ICONSTOP "Sorry, you must have administrative rights in order to install ${APPNAME}."
    Quit

  Win9x:
    MessageBox MB_ICONSTOP "This installer is not supported on Windows 9x/ME."
    Quit
		
  Admin:
  StrCpy $1 "" ; zero out variable
	
FunctionEnd

!macro setVars

  ReadRegStr $Host HKLM "${REG_APPSETTINGS}" "Host"
  ReadRegStr $Dbname HKLM "${REG_APPSETTINGS}" "Dbname"
  ReadRegStr $Port HKLM "${REG_APPSETTINGS}" "Port"
  ReadRegStr $GeoserverUrl HKLM "${REG_APPSETTINGS}" "GeoserverUrl"
  ReadRegStr $GeoserverBron HKLM "${REG_APPSETTINGS}" "GeoserverBron"
  ReadRegStr $DbUser HKLM "${REG_APPSETTINGS}" "DbUser"
  ReadRegStr $DbPassword HKLM "${REG_APPSETTINGS}" "DbPassword" 
  ReadRegStr $GeoServerUser HKLM "${REG_APPSETTINGS}" "User"
  ReadRegStr $GeoServerPassword HKLM "${REG_APPSETTINGS}" "Password"

  ReadRegStr $Host HKLM "${REG_APPSETTINGS}" "HostTest"
  ReadRegStr $Dbname HKLM "${REG_APPSETTINGS}" "DbnameTest"
  ReadRegStr $Port HKLM "${REG_APPSETTINGS}" "PortTest"
  ReadRegStr $DbUser HKLM "${REG_APPSETTINGS}" "DbUserTest"
  ReadRegStr $DbPassword HKLM "${REG_APPSETTINGS}" "DbPasswordTest" 

  ; Populates defaults on first display, and resets to default user blanked any of the values
  ${If} $Host == ""
	StrCpy $Host "localhost"
  ${EndIf}
  ${If} $Dbname == ""
	StrCpy $Dbname "oiv_prod"
  ${EndIf}
  ${If} $Port == ""
	StrCpy $Port "5432"
  ${EndIf}  
  ${If} $GeoserverUrl == ""
	StrCpy $GeoserverUrl "http://localhost:8080/geoserver/OIV/wfs?"
  ${EndIf}
  ${If} $GeoserverBron == ""
	StrCpy $GeoserverBron "OIV"
  ${EndIf}
  ${If} $DbUser == ""
	StrCpy $DbUser "username"
  ${EndIf}
  ${If} $GeoServerUser == ""
	StrCpy $GeoServerUser "username"
  ${EndIf}
  ${If} $HostTest == ""
	StrCpy $HostTest "localhost"
  ${EndIf}
  ${If} $DbnameTest == ""
	StrCpy $DbnameTest "oiv_test"
  ${EndIf}
  ${If} $Port == ""
	StrCpy $Port "5432"
  ${EndIf}  
  ${If} $DbUserTest == ""
	StrCpy $DbUserTest "username"
  ${EndIf}
  ${If} $PluginDir == ""
	StrCpy $PluginDir ""
  ${EndIf}

!macroend

Function .onInit

	; This is needed to set programdata dir
	setShellVarContext all
	StrCpy $INSTDIR "$APPDATA\${APPNAME}-${VERSION}"
	
	Call VersionCheck
	!insertmacro setVars
	
FunctionEnd

; The main install section
Section "${APPNAME} (required)" SectionMain
	SectionIn RO ; Makes this install mandatory
	SetOverwrite on
	
	; Uninstall old version first
	Call RemovePrevious 

	; Section Files
	CreateDirectory "$INSTDIR"
	SetOutPath "$INSTDIR"
	File /a license.txt
	File /a dos2unix.exe

	; Registry
	DetailPrint "Write ${APPNAME} settings to registry"
	WriteRegStr HKLM "${REG_APPSETTINGS}" "" "$INSTDIR"
	WriteRegStr HKLM "${REG_APPSETTINGS}" "Name" "${APPTITLE}"
	WriteRegStr HKLM "${REG_APPSETTINGS}" "Version" "${VERSION}"
	WriteRegStr HKLM "${REG_APPSETTINGS}" "Publisher" "${COMPANY}"
	WriteRegStr HKLM "${REG_APPSETTINGS}" "WebSite" "${WEBSITE}"
	WriteRegStr HKLM "${REG_APPSETTINGS}" "Host" "$Host"
	WriteRegStr HKLM "${REG_APPSETTINGS}" "Dbname" "$Dbname"
  WriteRegStr HKLM "${REG_APPSETTINGS}" "Port" "$Port"
  WriteRegStr HKLM "${REG_APPSETTINGS}" "GeoserverUrl" "$GeoserverUrl"
  WriteRegStr HKLM "${REG_APPSETTINGS}" "GeoserverBron" "$GeoserverBron"
	WriteRegStr HKLM "${REG_APPSETTINGS}" "HostTest" "$HostTest"
	WriteRegStr HKLM "${REG_APPSETTINGS}" "DbnameTest" "$DbnameTest"
  WriteRegStr HKLM "${REG_APPSETTINGS}" "PortTest" "$PortTest"

	; User settings
	WriteRegStr HKCU "Software\QGIS\QGIS3\Qgis" "askToSaveProjectChanges" "false"
SectionEnd

Section "WFS" SectionWFS
  File /a ..\qgis_project\objecten\geoserver.conf
	; Section Files
	CreateDirectory "$INSTDIR"
	SetOutPath "$INSTDIR"

  ;geoserver wfs config file
  ${IfNot} $GeoserverUrl == ""
    FileOpen $4 "$INSTDIR\geoserver.conf" w
    FileWrite $4 "$GeoserverUrl"
    FileWrite $4 "$\r$\n"
    FileWrite $4 "$GeoserverBron"
    FileWrite $4 "$\r$\n"
    FileWrite $4 "$GeoServerUser"
    FileWrite $4 "$\r$\n"
    FileWrite $4 "$GeoServerPassword"        
    FileClose $4
  ${EndIf}

	SetShellVarContext all

  AccessControl::GrantOnFile "$INSTDIR\db" "(S-1-5-32-545)" "GenericRead + GenericWrite"

SectionEnd

Section "Database" SectionDB
  File /a ..\qgis_project\objecten\pg_service.conf
	
	; set variable
	DetailPrint "Set windows variable PGSERVICEFILE to $INSTDIR\pg_service.conf"
	WriteRegStr HKLM "${REG_ENVIRONMENT}" "PGSERVICEFILE" "$INSTDIR\pg_service.conf"
	; make sure windows knows about the change
	SendMessage ${HWND_BROADCAST} ${WM_WININICHANGE} 0 "STR:Environment" /TIMEOUT=5000
	; convert eol to unix 
	nsExec::ExecToLog "$INSTDIR\dos2unix.exe $INSTDIR\pg_service.conf"

  ;Create db-connection service file
  ${IfNot} $Dbname == ""
    FileOpen $4 "$INSTDIR\pg_service.conf" a
    FileSeek $4 0 END
    FileWrite $4 "$\r$\n"
    FileWrite $4 "[oiv]"
    FileWrite $4 "$\r$\n"
    FileWrite $4 "host=$Host"
    FileWrite $4 "$\r$\n"
    FileWrite $4 "port=$Port"
    FileWrite $4 "$\r$\n"
    FileWrite $4 "dbname=$Dbname"
    FileWrite $4 "$\r$\n"  
    FileWrite $4 "user=$DbUser"
    FileWrite $4 "$\r$\n"
    FileWrite $4 "password=$DbPassword"
    FileWrite $4 "$\r$\n"
    FileWrite $4 "application_name=oiv"
    FileClose $4
  ${EndIf}

  File /a ..\qgis_project\objecten\pg_service_prod.conf

  ;Create db-connection service file prod
  ${IfNot} $Dbname == ""
    FileOpen $4 "$INSTDIR\pg_service_prod.conf" a
    FileSeek $4 0 END
    FileWrite $4 "$\r$\n"
    FileWrite $4 "[oiv]"
    FileWrite $4 "$\r$\n"
    FileWrite $4 "host=$Host"
    FileWrite $4 "$\r$\n"
    FileWrite $4 "port=$Port"
    FileWrite $4 "$\r$\n"
    FileWrite $4 "dbname=$Dbname"
    FileWrite $4 "$\r$\n"  
    FileWrite $4 "user=$DbUser"
    FileWrite $4 "$\r$\n"
    FileWrite $4 "password=$DbPassword"
    FileWrite $4 "$\r$\n"
    FileWrite $4 "application_name=oiv"
    FileClose $4
  ${EndIf}

  AccessControl::GrantOnFile "$INSTDIR\pg_service_prod.conf" "(S-1-5-32-545)" "FullAccess"
  AccessControl::GrantOnFile "$INSTDIR\pg_service.conf" "(S-1-5-32-545)" "FullAccess"

  SetRegView 64
SectionEnd

Section "DatabaseTest" SectionDBTest
  File /a ..\qgis_project\objecten\pg_service_test.conf
  
  ${If} ${SectionIsSelected} ${SectionDBTest}
    ;Create db-connection service file test
    ${IfNot} $DbnameTest == ""
      FileOpen $4 "$INSTDIR\pg_service_test.conf" a
      FileSeek $4 0 END
      FileWrite $4 "$\r$\n"
      FileWrite $4 "[oiv]"
      FileWrite $4 "$\r$\n"
      FileWrite $4 "host=$HostTest"
      FileWrite $4 "$\r$\n"
      FileWrite $4 "port=$PortTest"
      FileWrite $4 "$\r$\n"
      FileWrite $4 "dbname=$DbnameTest"
      FileWrite $4 "$\r$\n"  
      FileWrite $4 "user=$DbUserTest"
      FileWrite $4 "$\r$\n"
      FileWrite $4 "password=$DbPasswordTest"
      FileWrite $4 "$\r$\n"
      FileWrite $4 "application_name=oiv"
      FileClose $4
    ${EndIf}
  ${EndIf}

  AccessControl::GrantOnFile "$INSTDIR\pg_service_test.conf" "(S-1-5-32-545)" "FullAccess"
  
  SetRegView 64
SectionEnd

Section "Objecten" SectionObjecten
	; Section Files
	CreateDirectory "$INSTDIR"
	SetOutPath "$INSTDIR"
	File /a ..\qgis_project\objecten\OIV_Objecten.qgs
  File /a ..\qgis_project\objecten\update_dimension_tables_proj.py
	File /a ..\qgis_project\objecten\objecten.ico
	File /r ..\qgis_project\objecten\ui
	File /r ..\qgis_project\objecten\svg
  File /r ..\qgis_project\objecten\qpt
  File /r ..\qgis_project\objecten\db
 
	; Create desktop shortcuts
	;ReadRegStr $R0 HKLM "Software\QGIS" "InstallPath"
	ReadRegStr $R0 HKCR "QGIS Project\Shell\open\command" ""

	SetShellVarContext all

  AccessControl::GrantOnFile "$INSTDIR\db" "(S-1-5-32-545)" "GenericRead + GenericWrite"

  ${If} ${SectionIsSelected} ${SectionDB}
    CreateShortCut "$desktop\${APPNAME} Objecten-DB.lnk" "$INSTDIR\OIV_Objecten.qgs" "" "$INSTDIR\objecten.ico" 0
  ${EndIf}

  ${If} ${SectionIsSelected} ${SectionWFS}
    ;Convert standard PostGres project to geoserver WFS project
    SetRegView 64
    ReadRegStr $R2 HKLM "SOFTWARE\QGIS 3.22" "InstallPath"
    File /a ..\qgis_project\objecten\convert_objecten_to_wfs.py
    ExecWait "$R2\apps\Python37\python.exe $INSTDIR\convert_objecten_to_wfs.py"
    CreateShortCut "$desktop\${APPNAME} Objecten-WFS.lnk" "$INSTDIR\OIV_Objecten_WFS.qgs" "" "$INSTDIR\objecten.ico" 0
  ${EndIf}
SectionEnd
 
Section "Bluswater" SectionBluswater
	; Section Files
	CreateDirectory "$INSTDIR"
	SetOutPath "$INSTDIR"
	File /a ..\qgis_project\objecten\Bluswater_Beheer.qgs
	File /a ..\qgis_project\objecten\bluswater.ico
 
	; Create desktop shortcuts
	;ReadRegStr $R0 HKLM "Software\QGIS" "InstallPath"
	ReadRegStr $R0 HKCR "QGIS Project\Shell\open\command" ""

	SetShellVarContext all

  ${If} ${SectionIsSelected} ${SectionDB}
    ${StrRep} $R1 $R0 "%1" "$INSTDIR\Bluswater_Beheer.qgs"
    CreateShortCut "$desktop\${APPNAME} Bluswater-DB.lnk" "$INSTDIR\Bluswater_Beheer.qgs" "" "$INSTDIR\bluswater.ico" 0
  ${EndIf}

  ${If} ${SectionIsSelected} ${SectionWFS}
    SetRegView 64
    ReadRegStr $R2 HKLM "SOFTWARE\QGIS 3.22" "InstallPath"
    File /a ..\qgis_project\objecten\convert_bluswater_to_wfs.py
    ExecWait "$R2\apps\Python37\python.exe $INSTDIR\convert_bluswater_to_wfs.py"
    CreateShortCut "$desktop\${APPNAME} Bluswater-WFS.lnk" "$INSTDIR\Bluswater_Beheer_WFS.qgs" "" "$INSTDIR\bluswater.ico" 0
  ${EndIf}
SectionEnd

Section "Plugin ${PLUGINVERSION}" SectionPlugin
	; Get install path
	SetRegView 64

	; Section Files
  RMDir /r "$PluginDir\oiv"
	CreateDirectory "$PluginDir"
	SetOutPath "$PluginDir"
	File /r ..\plugin\oiv
	
	SetRegView 32
	WriteRegStr HKLM "${REG_APPSETTINGS}" "PluginDir" "$R1\oiv"

  AccessControl::GrantOnFile "$R1\oiv\config_files" "(S-1-5-32-545)" "GenericRead + GenericWrite"
  AccessControl::GrantOnFile "$R1\oiv\config_files\plugin_settings.json" "(S-1-5-32-545)" "GenericRead + GenericWrite"
SectionEnd

; Set the web server host
Function nsDialogHost
  ${If} ${SectionIsSelected} ${SectionDB}
    
    !insertmacro MUI_HEADER_TEXT "$(TEXT_HOST_TITLE)" "$(TEXT_HOST_SUBTITLE)"
    nsDialogs::Create 1018

    ;Syntax: ${NSD_*} x y width height text
    ${NSD_CreateLabel} 0 0 100% 36u "Set the database production host and name that ${APPNAME} will respond on."

    ${NSD_CreateLabel} 20u 40u 60u 14u "Host database:"  
    ${NSD_CreateText} 80u 38u 160u 14u $0
    Pop $0
    ${NSD_SetText} $0 $Host
    
    ${NSD_CreateLabel} 20u 60u 60u 14u "Database name:"  
    ${NSD_CreateText} 80u 58u 160u 14u $1
    Pop $1
    ${NSD_SetText} $1 $Dbname

    ${NSD_CreateLabel} 20u 80u 60u 14u "Port:"  
    ${NSD_CreateText} 80u 78u 160u 14u $1
    Pop $6
    ${NSD_SetText} $6 $Port

    ${NSD_CreateLabel} 20u 100u 60u 14u "Username:"  
    ${NSD_CreateText} 80u 98u 160u 14u $4
    Pop $4
    ${NSD_SetText} $4 $DbUser

    ${NSD_CreateLabel} 20u 120u 60u 14u "Password:"  
    ${NSD_CreatePassword} 80u 118u 160u 14u $5
    Pop $5

    ${NSD_CreateLabel} 20u 140u 100% 14u "Example valid database hosts are: localhost, demo.safetymaps.nl"

    nsDialogs::Show  

  ${EndIf}
FunctionEnd

Function nsDialogHostLeave
	# Read form
	${NSD_GetText} $0 $Host
	${NSD_GetText} $1 $Dbname
  ${NSD_GetText} $4 $DbUser
  ${NSD_GetText} $5 $DbPassword
  ${NSD_GetText} $6 $Port
FunctionEnd

; Set the web server host
Function nsDialogHostTest
  ${If} ${SectionIsSelected} ${SectionDBTest}
    
    !insertmacro MUI_HEADER_TEXT "$(TEXT_HOST_TITLE)" "$(TEXT_HOST_SUBTITLE)"
    nsDialogs::Create 1018

    ;Syntax: ${NSD_*} x y width height text
    ${NSD_CreateLabel} 0 0 100% 36u "Set the database test host and name that ${APPNAME} will respond on."

    ${NSD_CreateLabel} 20u 40u 60u 14u "Host database:"  
    ${NSD_CreateText} 80u 38u 160u 14u $0
    Pop $0
    ${NSD_SetText} $0 $Host
    
    ${NSD_CreateLabel} 20u 60u 60u 14u "Database name:"  
    ${NSD_CreateText} 80u 58u 160u 14u $1
    Pop $1
    ${NSD_SetText} $1 $Dbname

    ${NSD_CreateLabel} 20u 80u 60u 14u "Port:"  
    ${NSD_CreateText} 80u 78u 160u 14u $1
    Pop $6
    ${NSD_SetText} $6 $Port

    ${NSD_CreateLabel} 20u 100u 60u 14u "Username:"  
    ${NSD_CreateText} 80u 98u 160u 14u $4
    Pop $4
    ${NSD_SetText} $4 $DbUser

    ${NSD_CreateLabel} 20u 120u 60u 14u "Password:"  
    ${NSD_CreatePassword} 80u 118u 160u 14u $5
    Pop $5

    ${NSD_CreateLabel} 20u 140u 100% 14u "Example valid database hosts are: localhost, demo.safetymaps.nl"

    nsDialogs::Show  

  ${EndIf}
FunctionEnd

Function nsDialogHostTestLeave
	# Read form
	${NSD_GetText} $0 $HostTest
	${NSD_GetText} $1 $DbnameTest
  ${NSD_GetText} $4 $DbUserTest
  ${NSD_GetText} $5 $DbPasswordTest
  ${NSD_GetText} $6 $PortTest
FunctionEnd

Function nsDialogWFS
  ${If} ${SectionIsSelected} ${SectionWFS}
    
    !insertmacro MUI_HEADER_TEXT "$(TEXT_HOST_TITLE)" "$(TEXT_HOST_SUBTITLE)"
    nsDialogs::Create 1018

    ;Syntax: ${NSD_*} x y width height text
    ${NSD_CreateLabel} 0 0 100% 14u "Set the geoserver WFS host and source that ${APPNAME} will respond on."

    ${NSD_CreateLabel} 20u 40u 60u 14u "Geoserver URL:"
    ${NSD_CreateText} 80u 38u 160u 14u $2
    Pop $2
    ${NSD_SetText} $2 $GeoserverUrl

    ${NSD_CreateLabel} 20u 60u 60u 14u "Geoserver bron:"  
    ${NSD_CreateText} 80u 58u 160u 14u $3
    Pop $3
    ${NSD_SetText} $3 $GeoserverBron

    ${NSD_CreateLabel} 20u 80u 60u 14u "Username:"  
    ${NSD_CreateText} 80u 78u 160u 14u $4
    Pop $4
    ${NSD_SetText} $4 $GeoServerUser

    ${NSD_CreateLabel} 20u 100u 60u 14u "Password:"  
    ${NSD_CreatePassword} 80u 98u 160u 14u $5
    Pop $5

    ${NSD_CreateLabel} 20u 120u 100% 14u "Example valid geoserver url are: http://localhost:8080/geoserver/OIV/wfs?"  

    nsDialogs::Show

  ${EndIf}
FunctionEnd

Function nsDialogWFSLeave
	# Read form
  ${NSD_GetText} $2 $GeoserverUrl
  ${NSD_GetText} $3 $GeoserverBron
  ${NSD_GetText} $4 $GeoServerUser
  ${NSD_GetText} $5 $GeoServerPassword
FunctionEnd

Function OnDirBrowse
  ${NSD_GetText} $PluginInstallDir $0
  nsDialogs::SelectFolderDialog "Selecteer directory" "$0"
  Pop $0
  ${If} $0 != error
      ${NSD_SetText} $PluginInstallDir "$0"
      StrCpy $PluginDir "$0"
  ${EndIf}
FunctionEnd

Function nsDialogPluginDir
  ${If} ${SectionIsSelected} ${SectionPlugin}
    
    !insertmacro MUI_HEADER_TEXT "$(TEXT_HOST_TITLE)" "$(TEXT_HOST_SUBTITLE)"
    nsDialogs::Create 1018
 
    StrCpy $R1 "$PROFILE\AppData\Roaming\QGIS\QGIS3\profiles\default\python\plugins"
    ;Syntax: ${NSD_*} x y width height text
    ${NSD_CreateLabel} 0 0 100% 14u "Standaard installatie-pad voor de plugin:"
    ${NSD_CreateLabel} 0 18u 100% 14u "$R1" 
    StrCpy $PluginDir "$R1"
    
    ${NSD_CreateGroupBox} 0 86u 100% 34u "Plugin Install Path"
    Pop $0

        ${NSD_CreateDirRequest} 5% 100u 80% 12u "$R1"
        Pop $PluginInstallDir

        ${NSD_CreateBrowseButton} 85% 100u 10% 12u "..."
        Pop $0
        ${NSD_OnClick} $0 OnDirBrowse

    nsDialogs::Show

  ${EndIf}
FunctionEnd

Function nsDialogPluginDirLeave
FunctionEnd

; Summary page before install
Function Ready

  nsDialogs::Create 1018
  !insertmacro MUI_HEADER_TEXT "$(TEXT_READY_TITLE)" "$(TEXT_READY_SUBTITLE)"

  ;Syntax: ${NSD_*} x y width height text
  ${NSD_CreateLabel} 0 0 100% 24u "Please review the settings below and click the Back button if \
                                   changes need to be made.  Click the Install button to continue."

  ; Directory
  ${NSD_CreateLabel} 10u 25u 35% 24u "Installation directory:"
  ${NSD_CreateLabel} 40% 25u 60% 24u "$INSTDIR"

  ${If} ${SectionIsSelected} ${SectionWFS}
    ; Install type
    ${NSD_CreateLabel} 10u 45u 35% 24u "GeoServer URL settings:"
    ${NSD_CreateLabel} 10u 55u 35% 24u "URL:"
    ${NSD_CreateLabel} 40% 55u 60% 24u $GeoserverUrl

    ; Data dir
    ${NSD_CreateLabel} 10u 65u 35% 24u "GeoServer bron:"
    ${NSD_CreateLabel} 40% 65u 60% 24u $GeoserverBron
    
    ; Data dir
    ${NSD_CreateLabel} 10u 75u 35% 24u "Username:"
    ${NSD_CreateLabel} 40% 75u 60% 24u $GeoServerUser

  ${Else}
    ; Install type
    ${NSD_CreateLabel} 10u 45u 35% 24u "Database settings:"
    ${NSD_CreateLabel} 10u 55u 35% 24u "Host:"
    ${NSD_CreateLabel} 40% 55u 60% 24u $Host

    ; Data dir
    ${NSD_CreateLabel} 10u 65u 35% 24u "Database name:"
    ${NSD_CreateLabel} 40% 65u 60% 24u $Dbname
    
    ; Data dir
    ${NSD_CreateLabel} 10u 75u 35% 24u "User:"
    ${NSD_CreateLabel} 40% 75u 60% 24u $DbUser

    ; Port
    ${NSD_CreateLabel} 10u 85u 35% 24u "Port:"
    ${NSD_CreateLabel} 40% 85u 60% 24u $Port

    ; Plugin directory
    ${NSD_CreateLabel} 10u 85u 35% 24u "PluginDir:"
    ${NSD_CreateLabel} 40% 85u 60% 24u $PluginDir
  ${EndIf}

  nsDialogs::Show

FunctionEnd


; What happens at the end of the install.
Section -FinishSection

	; For the Add/Remove programs area
	WriteRegStr HKLM "${REG_UNINSTALL}" "DisplayName" "${APPTITLE}"
	WriteRegStr HKLM "${REG_UNINSTALL}" "Version" "${VERSION}"
	WriteRegStr HKLM "${REG_UNINSTALL}" "UninstallString" "$INSTDIR\uninstall.exe"
	WriteRegStr HKLM "${REG_UNINSTALL}" "InstallLocation" "$INSTDIR"
	WriteRegStr HKLM "${REG_UNINSTALL}" "DisplayIcon" "$INSTDIR\pictogram.ico"
	WriteRegStr HKLM "${REG_UNINSTALL}" "HelpLink" "${WEBSITE}"
	WriteRegStr HKLM "${REG_UNINSTALL}" "Publisher" "${COMPANY}"
	
	WriteUninstaller "$INSTDIR\uninstall.exe"

SectionEnd

Function VersionCheck

	ReadRegStr $R0 HKLM "${REG_UNINSTALL}" "UninstallString"
	ReadRegStr $R1 HKLM "${REG_UNINSTALL}" "Version"

	StrCmp $R1 ${VERSION} uninst done
  
;Run the uninstaller
uninst:
	ClearErrors
	Exec "$R0" ; Run the uninstaller
	Quit
  
done:
	StrCpy $R0 "" ; zero out variable
	StrCpy $R1 "" ; zero out variable

FunctionEnd

Function RemovePrevious

	ReadRegStr $R0 HKLM "${REG_UNINSTALL}" "UninstallString"

	StrCmp $R0 "" done
		nsExec::ExecToLog "$R0 /S" ; uninstall silently
  
done:
	StrCpy $R0 "" ; zero out variable

FunctionEnd

; Uninstall section
Section Uninstall

  ; delete variable
  DeleteRegValue "HKLM" "${REG_ENVIRONMENT}" "PGSERVICEFILE"
  ; make sure windows knows about the change
  SendMessage ${HWND_BROADCAST} ${WM_WININICHANGE} 0 "STR:Environment" /TIMEOUT=5000

  ; Delete plugin
  ReadRegStr $R0 HKLM "${REG_APPSETTINGS}" "PluginDir"
  RMDir /r "$R0"
  
  ; Delete Shortcuts
  SetShellVarContext all
  Delete "$desktop\${APPNAME} *.lnk"
  
  ;Remove from registry...
  DeleteRegKey HKLM "${REG_UNINSTALL}"
  DeleteRegKey HKLM "${REG_APPSETTINGS}"

  ; Delete self
  Delete "$INSTDIR\uninstall.exe"

  ; Delete files/folders
  RMDir /r "$INSTDIR\ui"
  RMDir /r "$INSTDIR\db"  
  RMDir /r "$INSTDIR\ini"
  RMDir /r "$INSTDIR\svg"
  RMDir /r "$INSTDIR\qpt"
  RMDir /r "$INSTDIR\__pycache__"
  Delete "$INSTDIR\*.*"

  RMDir "$INSTDIR\" ; no /r!

SectionEnd

; The End

