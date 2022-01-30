--release notes OIV versie 3.3.5 - 3.3.9
------------------------------------------------------------------

--3.3.5 - 3.3.6------------------------------------
#179 - Aangepast:
    Telefoonnummer van contactpersonen is aangepast naar meerdere karakters dan 11 -> 100 karakters geworden zodat er meerdere telefoonnummers gerigistreerd kunnen worden.

#185 - Fix:    
    luchtfoto URL PDOK is aangepast in het project
    Toegevoegd: 
---------------------------------------------------------

--3.3.6 - 3.3.7------------------------------------------
#147 - Aangepast:
    Min en Max bouwlaag terug als tekstuele velden bij een repressief object

#180 - Aangepast:
    Default type object omgezet naar "Gebouw"

#109 - Aangepast:
    Symbool te water laat plaats is veranderd, waardoor deze duidelijker is dan het oude symbool

#183 - Fix:    
    Verwijderen van een laatste object geeft een Stop-Iteration error. In code afgevangen zodat deze melding niet meer zou moeten verschijnen.

#188 - Fix:
    Aantal symbolen hadden een verkeerde naamgeving zodat deze knoppen het niet deden in de plugin.
--------------------------------------------------------

--3.3.7 - 3.3.8-----------------------------------------
#193 - Aangepast:
    Aan het OIV data-model is een "werkvoorraad" schema toegeveogd. Indien een 3e applicatie tegen de database gaat praten (direct of via WFS-T) wordt dit afgevangen en in een werkvoorraad tabel geplaatst.

    Deze zijn in OIV beschikbaar en in de plugin is de mogelijkheid gecreerd om deze werkvoorraad wijzigingen goed te keuren of af te wijzen.

    Goedgekeurde wijzigingen worden verwerkt in de "echte" tabellen en afwijzingen worden verwijderd. Alle aanpassingen worden opgeslagen in een log tabel.

    Aan alle "views" is een kolom 'applicatie' toegevoegd. Zodra in bij opslaan 'OIV' als applicatie wordt meegegeven worden de wijzigingen direct verwerkt, is dit niet het geval komen ze in de werkvoorraad terecht.

    Werkvoorraad verwerken is alleen mogelijk via de database-koppeling en niet via WFS.

    Alle rules in de database zijn aangepast naar functies en triggers, waardoor er meer controle is over wat er gebeurd.


#140 - Aangepast:
    3 losse lagen toegevoegd aan de datbase - of_interest, punten lijnen en vlakken. Dit maakt het mogelijk om in de plugin symbolen op de kaart te plaatsen welke niet zijn gekoppeld aan een repressief object of een bouwlaag.

    Hiervoor is in de database een apart schema aangemaakt, namelijk info_of_interest. Vanaf nu is het mogelijk om losse symbolen, labels en linen te tekenen. In de plugin is dit te vinden op de eerste widget via een nieuwe knop.

    Alle bestaande symbolen in de tabellen "pictogrammen_zonder_object" zijn overgezet naar de nieuwe tabellen.
    Nadat dit goed is getest moet er nog een script worden gemaakt om de "pictogrammen zonder object" op te ruimen.

#199 - Aangepast
    De styling van een hekwerk is aangepast naar dezelfde styling als afrastering vanuit natuur.

#186 - Aangepast:
    Print omgeving ingericht voor het printen naar PDF van de bouwlagen. Via een knop in de plugin worden alle bouwlagen van een Pand automatisch geprint. De gebruiker moet hierin de locatie (map) opgeven waar de PDF's moeten worden opgeslagen.

#184 - Aangepast:
    Alle functies in het tekenen widget worden nu vastgehouden totdat de gebruiker een andere functie selecteert. Voorheen was dit alleen voor het tekenen. Maar nu ook voor verwijderen/roteren en verplaatsen.

#172 - Aangepast:
    Op alle widgets is de terug knop verplaats naar de bovenkant van de widget. Zo is hij altijd op dezelfde plek te vinden.

#192 - Fix:
    De automatisch opslaan scripts waren verouderd en bevatte onnodige code waardoor er soms een python fout optrad. Deze scripts zijn opgeschoon.

#129 - Fix:
    Sommige widget in de plugin hadden nog geen "scroll-area", waardoor het schem buiten het beeld kon worden geduwd. Aan alle widget is nu een scrool-area toegevoegd en zou dit niet meer moeten kunnen voorkomen.

#116 - Fix:
    Het was mogelijk door onnauwkeurigheid in het nearest neighbour algoritme dat bepaalde zaken aan een verkeerde bouwlaag werd gekoppeld. Dit kwam doordat nearest neighbout eigenlijk niet geschikt is voor punt of lijn naar polygoon afstand berekening.

    Vanaf nu kan er alleen worden gekoppeld aan een bouwlaag welke bij het BAG-pand hoort en wordt daarna gekeken welk centroide van de polygoon (bouwlaag) het dichtsbij de nieuw te plaatsen symbool/lijn/vlak ligt.

--------------------------------------------------------

--3.3.8 - 3.3.9-----------------------------------------

#211 - Aangepast:
    Vanaf deze versie is het mogelijk om een scenario een locatie op de kaart te geven. Hierbij wordt er een pdf/url gekoppeld aan een punt op de kaart. Door de feature-info op te vragen kan er op deze manier media worden geopend in de afnemende applicaties.

    Hiervoor moet de regio zelf een url beschikbaar maken waar deze scenario's worden geserveerd.

    Aan het schema algemeen is een settings tabel toegevoegd. Hier kunnen voor de plugin settings worden opgeslagen, maar dus ook de basis URL waar de scenario's te vinden zijn.

    In de scenario type tabel kunnen een aantal default voorbereide scenario's inclusief URL worden opgenomen, welke de gebruiker via een dropdown kan koppelen aan een scenario-locatie. Indien het een apart scenario betreft kan de gebruiker handmatig het specifieke gedeelte van de URL opnemen.

    Voor de scenario's zijn er views gemaakt welke net als andere lagen de scenario's serveren en de basis-url met de specifieke url is samengevoegd, waardoor deze kan worden geopend bij opvraging.

#160 - Aangepast:
    Tijdens het importeren van een DXF tekening is de mogelijkheid toegevoegd om een lijn te converteren naar een deur pictogram. Hiervoor kan de gebruiker kiezen tijdens het maken van een mapping.

#196 - Aangepast:
    Het is nu mogelijk om een slagboom op een bouwlaag te tekenen. Om dit in het IMROI model te laten passen is dit toegevoegd aan de bouwkundige veiligheidsvoorzieningen.

#143 - Aangepast:
    Een delete vanuit OIV of vanuit elders wordt afgevangen. Er wordt een datum_deleted timestamp gegeven in de tabel. Hiervoor is aan elke tabel deze kolom toegevoegd.

    De views filteren op basis van de datum_deleted. Is er iets ongewenst weggegooid kan in de database bij het betreffende object de datum worden weggehaald. Dan is hij weer zichtbaar.

#145 - Aangepast:
    Aan alle tabellen welke zowel op een bouwlaag als een repressief object kunnen bestaan is een size-object toegevoegd. Hierdoor is de controle over de symbool-grootte onafhankelijk gemaakt van bouwlaag of repressief object.

#144 - Aangepast:
    Aan ruimten is het type afbrandscenario toegevoegd.

#146 - Aangepast:
    Aan bereikbaarheid is "terrein niet begaanbaar" toegevoegd

#163 - Aangepast:
    Hulplijn en contour zijn verplaatst in de teken widget naar het kopje bereikbaarheid

#187 - Aangepast:
    Bij het printen zijn ook alle gerelateerd attributen tabellen opgenomen en het printen van het repressief object zelf is hiervoor aangepast.

#148 - Fix:
    Snapfunctie van het tekenen is verbeterd, waardoor snappen op hoeken en segementen makkelijker wordt. Dit werkte al goed echter was de tolerantie niet groot genoeg om voorkeur te geven aan de hoekpunten ten opzichte van de segmenten.

#213 - Fix:
    Soms werd een snappunt op 0,0 geplaast. Dit mag nooit voorkomen en er is een bug ontdekt in het berekenen van het dichtsbijzijnde snappunt. Dit is aangepast en zou niet meer voor mogen komen.

