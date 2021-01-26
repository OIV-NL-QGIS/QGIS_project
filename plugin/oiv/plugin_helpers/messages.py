"""all string messages in the plugin"""
from qgis.PyQt.QtWidgets import QMessageBox #pylint: disable=import-error

def showMsgBox(msgName):
    msgSettings = MESSAGES[msgName]
    if msgSettings["type"] == 'information':
        return QMessageBox.information(None, msgSettings["header"], msgSettings["body"], QMessageBox.Ok)
    if msgSettings["type"] == 'warning':
        return QMessageBox.warning(None, msgSettings["header"], msgSettings["body"])
    if msgSettings["type"] == 'question':
        return QMessageBox.warning(None, msgSettings["header"], msgSettings["body"], QMessageBox.Yes, QMessageBox.No)

#All messages
MESSAGES = {
    'gridcreated': {
        "type": 'information',
        "header":'Het grid is succesvol aangemaakt!',
        "body":'Het grid is succesvol aangemaakt!'
    },
    'deletegrid': {
        "type": 'question',
        "header": 'Continue?',
        "body": 'Weet u zeker dat u het bestaande grid wilt weggooien?'
    },
    'selectgrid': {
        "type": 'information',
        "header": 'Selecteer grid!',
        "body": 'Selecteer het grid dat u wilt weggooien op de kaart.'
    },
    'nogridselected': {
        "type": 'information',
        "header": 'Geen tekenlaag!',
        "body": 'U heeft geen grid of kaartblad aangeklikt!\n\nKlik a.u.b. op de juiste locatie.'
    },
    'newobjectslowanswer': {
        "type": 'warning',
        "header": 'Server antwoord te traag',
        "body": 'Geoserver antwoord te traag. Object is wel geplaatst.\n\nOpen het object door terug te gaan en hem te selecteren.'
    },
    'deleteobject': {
        "type": 'question',
        "header": 'Continue?',
        "body": 'Weet u zeker dat u de geselecteerde feature wilt weggooien?'
    },
    'deletedobject': {
        "type": 'information',
        "header": 'Succesvol!',
        "body": 'Het object is succesvol verwijderd.'
    },
    'noselectedtodelete': {
        "type": 'information',
        "header": 'Geen tekenlaag!',
        "body": 'U heeft geen feature op een tekenlaag aangeklikt!\nKlik a.u.b. op de juiste locatie.\n\nWeet u zeker dat u iets wilt weggooien?'
    },
}
