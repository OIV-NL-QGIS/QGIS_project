--release notes OIV versie 3.1.1
------------------------------------------------------------------
Uitbreiding van de CAD functionaliteiten.

Binnen de applicatie is het nu mogelijk om op verschillende plekken extra CAD functionaliteiten te gebruiken. Deze functionaliteiten zijn te gebruiken op alle plaatsen waar er lijnen en/ of vlakken worden getekend. In de plugin is ingesteld op welke lagen er gesnapd kan worden. Dit zijn eigenlijk altijd de lijn en polygoon tekenlagen.
De totaliteit aan CAD functies is nu als volgt:

- Haakse hulplijnen. als er gesnapd wordt op een object dan wordt er gekeken of het een lijn of een hoek betreft. Indien het een lijn betreft verschijnt er een orthogonale hulplijn t.o.v. gesnapte lijn en één evenwijdig. Hetzefde geldt voor hoeken. De applicatie geeft de voorkeur op snappen op de hoek.

- Hulpcirkel, op het laatst getekende punt verschijn er een cirkel indien er in de plugin bij de hulpcirkel een straal is ingesteld en de knop actief is. Deze straal kan ingesteld worden tot 1 decimaal achter de komma, dus een equivalent van 10 cm. Indien de cirkel op bijvoorbeeld 5 meter is ingesteld kan er in een omtrek van 360 graden een volgende punt op exct 5 meter worden gezet.

- Parallel, indien de knop parallel wordt aangeklikt en een afstand wordt ingesteld kan gebruikt worden gemaakt van 2 functionaliteiten. Na het aanklikken van de knop is het mogelijk om een andere lijn/polygoon aan te klikken waaraan je evenwijdig wilt gaan tekenen. Er verschijnt een hulplijn evenwijdig aan de aangeklikte lijn op het laatst getekende punt en op een "offset" vanaf de aangeklikte lijn. Zo kan er bijvoorbeeld een afstand vanaf een bepaalde lijn worden gekozen om verder te gaan met tekenen. Na het selecteren van de evenwijdige lijn, wordt automatisch deze functie weer uitgeschakeld en kan worden verder gegaan met tekenen.

- Verlengde, zodra er een punt is getekend zal er een "verlengde" hulplin zichtbaar zijn. Door deze hulplijn is het mogelijk om te richten op een ander object, bijvoorbeeld een hoek van een pand. Deze hulplijn is altijd 50 meter langer dan de lijn die je wilt gaan tekenen.


--release notes OIV versie 3.1.2
------------------------------------------------------------------
Meerdere polygonen (terreinen) koppelen aan 1 repressief object (i-tje)

Het terrein wat te tekenen was bij een repressief object was een 1-1 relatie. In de database is dit vlak verplaatst naar een aparte tabel waardoor er een 1-n relatie is ontstaan. Bij het repressief object in de plugin is er een knop gekomen om het terrein te bewerken. Indien deze aan wordt geklikt verschijnen er teken functionaliteiten. Je kunt een terrein toevoegen aan een object, verwijderen, attribute-gegevens opvragen (aan elk terrein kan een eigen omschrijving worden meegegeven). Ook hier zijn de CAD functionaliteiten weer terug te vinden.

Daarnaast is er een "pan" knop om eventueel de tekenfunctionaliteit weer "uit" te zetten als je toch niet wilt gaan tekenen. Ten aanzien van het "in gebruik" zetten voor de voertuigviewer van Bouwlaag gegevens geldt de bij het object opgegeven historie voor alle bij het object behorende terreinen.

Het verwijderen van een terrein heeft niet tot gevolg dat de binnen het terrein liggende andere objecten verwidjerd worden. Dit moet via "tekenen". Dit om ongewenste verwijderingen te voorkomen. Indien je wel alles wilt verwijderen, kan dit door het complete object te verwijderen. Dit geldt dan weer niet voor de bouwlaag-gegegens.


--release notes OIV versie 3.1.3
------------------------------------------------------------------
Om meer invloed te kunnen hebben op de styling is er in de database een "styles" tabel toegevoegd. In deze tabel kunnen van alle lijnen en polygonen de stijl worden beheerd. Behalve van de lijnstijlen die een symbolenlijn zijn of uit meerdere lijnen bestaan zoals een weg op eigen terrein.

De te bewerken onderdelen van een stijl zijn:
- lijnkleur
- lijntransparantie
- lijndikte
- lijnstijl
- lijn eindstijl
- verbindingsstijl
- vlakkleur
- vlaktransparantie
- vlakstijl

Er is bewust voor gekozen om deze alleen voor de regionaal beheerder aanpasbaar te maken om uniformiteit te behouden. Let wel, een aangepast stijl geldt voor alle objecten in die tekenlaag en dus niet alleen voor één object.

Een repressief object is weer te koppelen aan een BAG Object. Let op als er bouwlagen en/of ruimten over het bag pand heen liggen wordt dit niet herkent en zal er een melding komen dat een verkeerd pand is aangeklikt.

--release notes OIV versie 3.1.4
------------------------------------------------------------------
Aan de plugin en in de database zijn de evenemente pictogrammen en stijlen toegevoegd. Dit betreffen de volgende:
- Symbolen -> Attractie, Feesttent, Straattheater, Kleedkamer, Vuurwerkafsteekplaats, Restaurant, Tijdelijke wegafsluiting
Daarnaast zijn de bestaande symbolen voor braadkraam_elektra en braadkraam_gas vervangen door respectievelijk kraam_elektra en kraam_gas.
- Lijnen -> Evenementenroute
- Vlak -> Parkeerzone
Verder zijn op het evenemeten tabblad bij het tekenen de symbolen nooduitgang en brandblusser toegevoegd. Deze bestonden al op het industrie tabblad.

In deze release is de styling in het Qgis project aangepast van hard-coded naar dynamisch. De symbool naam voor bijvoorbeeld een pictogram wordt uit de database gehaald en via die naam wordt het symbool uitgelezen uit de svg map.

--release notes OIV versie 3.1.5
------------------------------------------------------------------
Ten behoeve van evenementen en eventueel ook natuurbrand is het vanaf deze versie mogelijk om een grid toe te voegen aan een repressief object.
Op het repressief object tabblad is een knop gekomen om deze functionaliteit te openen. Indien deze wordt geopend kan er een grid worden aangemaakt. Het grid dat wordt aangemaakt is net zo groot als het extent van de kaart op dat moment, pas voordat je het grid gaat maken de kaart zo aan dat het overeenkomt met de grootte van het gewenste grid. Doe dit eventueel door in QGis onderin de balk het zoomniveau handmatig aan te passen. Let op: Het grid wordt gebaseerd op het kilometergrid van het Rijksdriehoekstelsel, waarbij het grid wordt ingesteld op basis van het extent en de gewenste grid spreiding.

Volg hierna de volgende stappen:
1. Stel de gewenste grid spreiding in in het invoervak. Bijvoorbeeld 100m. Dit houdt in dat de zowel de verticale als horizontale afstand tussen de gridlijnen 100m wordt.
2. Klik op aanmaken van het grid. De plugin gaat nu alle grid vakken aanmaken als polygonen in de database. Hierbij worden horizontaal de onderste vakken gelabeld met letters en de linker verticale vakken met cijfers. Indien er meer dan 26 (aantal letters) aan horizontale vakken zijn wordt er met dubbele letters gewerkt.

Per repressief object is het mogelijk om eventueel meerdere grids aan te maken.

Als laatste is er een knop om alle, let op ALLE, grids in 1x weer te verwijderen welke gekoppeld zijn aan het repressief object.

--release notes OIV versie 3.1.6
------------------------------------------------------------------
Het was al mogelijk om DXF en Shape bestanden in te lezen voor lijn- en/of vlakobjecten bij de bouwlagen. Vanaf deze versie is het ook mogelijk om deze bestanden in te lezen voor een repressief object. Deze functionaliteit is aan te roepen via een knop op de repressief object pagina in de plugin. 

Na het kiezen voor deze functionaliteit zijn er volgens een worklfow een aantal stappen te ondernemen:
1. Kies het juiste bestanden
1a. bij een DXF moet worden aangegeven welke soort geometrie er moet worden ingelezen vanuit de DXF, voor een Shape is dit niet relevant aangezien deze maar 1 soort bevat.
2. Na het laden van het bestand moet er een keuze gemaakt worden in welk veld de types te vinden zijn. Voor OIV is het noodzakelijk dat alles een type heeft, bijvoorbeeld "rookwerendescheiding".
3. Nadat dit veld is gekozen kan er een mapping worden aangemaakt. Dit houdt in dat ale types uit het bronbestand moeten worden gekoppeld aan een target type uit OIV.
3a. Om deze mapping te maken opent een pop-up. Hier kan achtereenvolgens worden aangegeven welk type naar welke OIV laag moet worden gemapt en daarna het type uit die laag. Nij de laatste stap is het ook mogelijk om er voor te kiezen om een bepaald import-type 'niet in te lezen'.
3b Gedurende het maken van een mapping kan er altijd een stap terug worden gedaan om nog aanpassingen te maken. Dit houdt wel in dat instellingen gedaan in een "volgende" stap weer worden overschreven.
3c Als de mapping gereed is kan er op OK worden geklikt.
3d Indien er toch wordt besloten om niet te importeren kan de actie worden eëindigd via "Cancel"

LET OP: Voor nu is het in de eerste stap nog niet mogelijk om een conversie te doen van Lijn naar Vlak of viceversa, deze functionaliteit is daarom uitgegrijsd en er kan alleen op volgende worden geklikt.

4. Nadat de mapping is gemaakt kan het inlezen worden gestart.

--release notes OIV versie 3.1.7
------------------------------------------------------------------
Vanaf 3.1.7 is het mogelijk om het project te koppelen met GeoServer naast de database-koppeling.
Hiervoor is de installer aangepast, waar er een keuze gemaakt kan worden om WFS te installeren. Dit houdt in dat in plaats van de database-koppeling alle datakoppelingen in het QGIS-project worden vervangen door WFS koppelingen. Belangrijk hiervoor is dat vooraf natuurlijk de geoserver goed is ingesteld.

De volgende instellingen zijn van belang:
- Instellingen GeoServer
    - Maak een aparte omgeving aan voor OIV
    - Maak voor de schema's algemeen, bluswater en objecten aparte bronnen aan
    - Vul bij elke bron in het veld gt_pk_metadata_table -> "gt_pk_metadata_table" in zonder "
    - Maak een autorisatie aan per bron op basis van Basic authentication
- De volgende database tabellen moeten worden geserveerd als WFS, waarbij de laagnaam exact hetzelfde dient te zijn als de database tabelnaam:
    Ook al zijn bepaalde tabellen niet gevuld of worden ze niet gebruikt.
    TABELLEN (schema algemeen):
        - applicatie
        - bag_extent
        - styles
        - styles_symbols_type
        - teamlid
    VIEW (schema algemeen):
        - veiligheidsregio_huidig
    TABELLEN (schema bluswater):
        - brandkranen
        - leidingen
        - alternatieve
        - alternatieve_type
    TABELLEN (schema objecten):
        - alle type tabellen "..._type"
        - alle overige tabellen behalve:
            - afw_binnendekking
            - gt_pk_metadata_table
            - pictogram_zonder_object
            - pictogram_zonder_object_type
            - ruimten
            - veiligh_bouwk
            - veiligh_install
    VIEWS (schema objecten, alle views niet voorafgegaan door "view_":
        - managementlagen (4x stavaza_... views en status_objectgegevens), 
        - alle views voorgegaan door "bouwlaag_", bluswater lagen
        - object_bgt
        - ruimtelijk_sleutelkluis
        - schade_cirkel_calc
        - veiligh_bouwk_types
    In totaal komt het neer op 64 gepubliceerde lagen, exclusief de "view_" voor de externe publicatie van de gegevens.
- Laat bij de installatie het WFS vinkje aan staan. Vul de URL, omgevingnaam, gebruikersnaam en wachtwoord in.
- Op de type tabellen na zijn nu alle koppelingen, WFS koppelingen en OIV kan gewoon gestart worden vanaf het bureablad met de snelkoppeling
- Voor de type tabellen is het voldoende om deze eens per sessie te verversen en op te halen ipv alle keren te bevragen. Dit komt de performance enorm ten goede. Bij het opstarten van het project en van de plugin worden voor beide alle gegevens bij gewerkt door een éénmalige WFS bevraging. Duurt ongeveer 2 seconden en dit heeft de gebruiker niet door.
- Handmatige verversing is tevens ingebouwd in de plugin onder het menu "Plugin", "OIV Objecten", "Ververs types".

WFS en database projecten zijn lokaal niet door elkaar te gebruiken. Het is het één of het ander. Per organsatie kan dit wel prima door elkaar heen worden gebruikt.

--release notes OIV versie 3.1.8
------------------------------------------------------------------
De plugin moet synchroon zijn met de database. Afhankelijk van de connectie (db/wfs) wordt bij het laden van de plugin en dus qgis de dimensie tabel geupdatet.
Als het project connectie maakt via de wfs koppeling dan wordt bij het opstarten van het project ook de dimesnie tabellen van het project geupdatet.

Indien de plugin bij opstarten niet heeft kunnen updaten of men wil tijdens het werken een aanpassing doorvoeren (bijvoorbeeld de stijl) kan via het plugin menu (OIV Objecten) handmatige synchronisatie worden gestart. Dit geldt dan alleen voor het QGIS oiv project en wordt alleen uitgevoerd indien gebruik wordt gemaakt van de WFS koppeling. Het is niet noodzakelijk voor de plugin en wordt voor de plugin dan ook niet uitgevoerd.

Daarnaast is de installer aangepast zodat bij elke installatie, zowel bij db- als wfs koppeling de gebruikersnaam en wachtwoord moeten worden opgegeven. In het gehele project wordt nu nergens meer de connectie parameters opgeslagen. Deze worden pas opgeslagen in de pg_service.cong of de geoserver.conf na installatie.

De mogelijkheid is toegevoegd om te filteren op repressief object op basis van type, datum_vanaf en datum_tot. Deze filtering staat op de hoofdpagina van de plugin. Door de filtering in te vullen en de vinkjes voor de filter aan te zetten zullen de repressief objecten worden gefilterd. Om een filtering ongedaan te maken -> zet de vinkjes uit en klik nogmaals op filteren, hiermee wordt de filter "geleegd".
Het instellen van het object type kan worden gedaan bij de historie en de datums bij de objectgegevens.

--release notes OIV versie 3.1.9
------------------------------------------------------------------
De i-tjes zijn visueel aangepast naar 4 verschillende iconen. Hierdoor is direct zichtbaar welke type het betreft.
Daarnaast is het symbool "schacht" toegevoegd aan de bouwlagen tekenen.

--release notes OIV versie 3.2.0
------------------------------------------------------------------
Updaten van dimesie table zowel mogelijk via database connectie als via WFS
Symbool (styling) voor brandkraan toegevoegd indien capaciteit niet gevuld is -> standaard blauwe rondje
Niet meer mogelijk om een GEOS ongeldige geometrie op te slaan. Gebruiker krijgt een waarschuwing en de geometrie wordt verworpen. Dit gebeurd vaak door een dubbel punt op dezelfde plaats of door self-intersecting polygons/lines