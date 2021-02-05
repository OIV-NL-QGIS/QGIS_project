"""all string messages in the plugin"""
from qgis.PyQt.QtWidgets import QMessageBox #pylint: disable=import-error

def showMsgBox(msgName, extraBody=''):
    msgSettings = MESSAGES[msgName]
    if msgSettings["type"] == 'information':
        return QMessageBox.information(None, msgSettings["header"], msgSettings["body"] + extraBody, QMessageBox.Ok)
    if msgSettings["type"] == 'warning':
        return QMessageBox.warning(None, msgSettings["header"], msgSettings["body"] + extraBody)
    if msgSettings["type"] == 'critical':
        return QMessageBox.critical(None, msgSettings["header"], msgSettings["body"] + extraBody)
    if msgSettings["type"] == 'question':
        return QMessageBox.warning(None, msgSettings["header"], msgSettings["body"] + extraBody, QMessageBox.Yes, QMessageBox.No)

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
    'bouwlaagcreated': {
        "type": 'information',
        "header": 'Gereed!',
        "body": 'Alle bouwlagen zijn succesvol aangemaakt!'
    },
    'nobouwlaagselected': {
        "type": 'information',
        "header": 'Geen bouwlaag!',
        "body": 'U heeft geen bouwlaag aangeklikt!\n\nKlik a.u.b. op de juiste locatie.'
    },
    'importchecksok': {
        "type": 'information',
        "header": 'Checks ok!',
        "body": 'Alle checks uitgevoerd u kunt doorgaan met importeren!'
    },
    'importerrorrdstelsel': {
        "type": 'warning',
        "header": 'Geen RD stelsel!',
        "body": 'Het coordinatenstelsel is geen RD!<br><br>\
                 Pas dit aan voordat je verder gaat met inlezen!'
    },
    'importerrorgeometrie': {
        "type": 'warning',
        "header": 'Geometrie komt niet overeen!',
        "body": 'De geometrie in het bestand komt niet overeen met de geselecteerde laag!<br><br>'
                'Pas dit aan voordat je verder gaat met inlezen!'
    },
    'importsuccesfull': {
        "type": 'information',
        "header": 'Gereed!',
        "body": 'Alle feature zijn succesvol geimporteerd!'
    },
    'importpartiallysuccesfull': {
        "type": 'information',
        "header": 'Gereed!',
        "body": 'Features zijn geimporteerd.\n'
                'Aantal features dat niet is geïmporteerd vanwege ongeldige geometrie:<br><br>'
    },
    'bouwlaagvolgorde': {
        "type": 'warning',
        "header": 'Let op!',
        "body": 'De hoogste bouwlaag kan niet lager zijn als de laagste, vul opnieuw in!.'
    },
    'noidentifiedobject': {
        "type": 'information',
        "header": 'Geen tekenlaag!',
        "body": 'U heeft geen feature op een tekenlaag aangeklikt!\n\nKlik a.u.b. op de juiste locatie.'
    },
    'invalidgeometry': {
        "type": 'warning',
        "header": 'Ongeldige geometrie!',
        "body": 'Vermoedelijk heeft u 2x op hetzelfde punt geklikt of doorkruist de geometrie zichzelf.\n\n'
                'De geometrie wordt niet opgeslagen.'
    },
    'noparentfeature': {
        "type": 'warning',
        "header": 'Let op!',
        "body": 'Geen object gevonden om aan te koppelen.\n\n'
                'Zorg dat het te koppelen object in het kaartbeeld zichtbaar is.'
    },
    'invaliddatabaseversion': {
        "type": 'critical',
        "header": 'Let op!',
        "body": 'De plugin of het project komt niet overeen met database versie!\n'
                'Vraag aan uw regionaal beheerder om een database update.\n\n'
                'Excuses voor het ongemak.'
    },
    'unsavedchanges': {
        "type": 'warning',
        "header": 'Niet opgeslagen',
        "body": 'Om van bouwlaag te veranderen moet u eerst de bewerkingen opslaan!\n\nVoer daarna de actie opnieuw uit!'
    },
}
