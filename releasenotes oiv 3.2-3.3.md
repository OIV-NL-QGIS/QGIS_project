--release notes OIV versie 3.3.0
------------------------------------------------------------------

--3.2.1 - 3.2.4
Toegevoegd: Controle op ingevoerde geometrieën. Als de gebruiker een ongeldige geometrie wil opslaan wordt dit geweigerd. Dit zodat in de database spatial queries geen hinder      ondervinden van deze geometrieën. De gebruiker krijgt een melding dat deze ongeldig is en kan hem opnieuw tekenen.
Toegevoegd: Mogelijkheid om naast SHP en DXF ook GeoPackage te importeren.
Toegevoegd: Lagen halen de "size" voor de styling uit de database i.p.v hardcoded in het QGis project.
Toegevoegd: Complete integratie van de folder bluswater in het project in de objecten folder. Heel veel bestanden waren gedupliceerd in de verschillende folders.
Toegevoegd: Integratie van de installer in het GitHub project

Fix:    ongeldige pad verwijzing van de geoserver.conf file
Fix:    update van veiligheidsregiogrens in dimesie database
Fix:    Autorisatie voor geoserver bij het updaten van de dimensie tabellen werkte niet -> aangepast naar basic authentication in de header in plaats van de url.   
Fix:    Na het opslaan of aanpassen van een geoserver laag heeft QGis een reload nodig. De aanpassingen worden wel gedaan maar niet getoond op het canvas. Dit komt omdat QGis de WFS kaartlagen "cached"
Fix:    in de database wordt niet meer gebruik gemaakt van type_id's voor bouwkundige veiligheidsvoorzieningen. De plugin zag deze id's nog wel voor het importeren van gegevens.       Aangepast naar de daadwerkelijk naam van het type voorziening
Fix:    Indien er een nieuw object wordt aangemaakt geeft de database connectie het nieuwe ID terug. Via WFS-T komt dit niet terug. Voor WFS-T wordt een request gedaan voor het laatst aangemaakte ID. Let op dat de gebruiker dan wel checked of het juist object is geselecteerd. Zo niet, even terug en opnieuw selecteren van het opnieuw aangemaakte object.
Fix:    Tekenen van lagen (alternatief bluswater) niet gekoppeld aan een repressief object.
Fix:    Verschillende linting code verbeteringen


--3.2.5
Toegevoegd: Vernieuwing Alternatief Bluswater SLD
Toegevoegd: Print-omgevingen voor Natuurbrand en update "oude" print-omgeving ojecten
Toegevoegd: Styling op een hoger schaal niveau dan alleen zichtbaar beneden de 1:5000 of 1:2500. Voor alle repressief-object/bluswater lagen is dit aangepast
Toegevoegd: Laag points-of-interest, hierin bevinden zich bijzonder obecten in bijvoorbeeld een natuurgebied. Gebaseerd op de herrijking natuurbrand.

Aangepast:  Grootte van de anchor points (sterretje), deze was veel te groot in sommige gevallen
Aangepast:  Scrollbar in de import widget


--3.2.6
Toegevoegd: Laag gebiedsgericht-aanpak, gebaseerd op de herrijking natuurbrand.
Toegevoegd: Kaartblad als tekenlaag voor het bepalen van het extent van de print-omgeving.
Toegevoegd  Creeren van een Kaartblad met of zonder Grid in de plugin.
Toegeveogd: Preview kaartblad op het canvas in QGis. Zo kan de gebruiker eerst zien welke grootte het kaartblad is gebaseerd op de papiergrootte (A0-A4, liggend en staand) voordat hij daadwerkelijk aangemaakt wordt.

Aangepast:  Laag veiligheidsregio niet meer identificeerbaar in het project. Hierdoor met het i-tje niet meer per-ongeluk aan te klikken, de plugin moet weten of er "geen" laag is aangeklikt en als de laag veiligheidsregio aanklikbaar is dan klikt de gebruiker altijd een laag aan.
Aangepast:  Kleur Anchorpoint op labels was niet zichtbaar. Aangepast naar een andere kleur als zwart.
Aangepast:  Overslaan van pop-up van de geometrie-check bij het importeren. Aan het einde rapporteren als er fouten waren bij de import. Het aantal fouten wordt geteld.


--3.2.7
Toegevoegd: Indien het grid groter is dan het kaartblad -> maak de laatste grid vakken kleiner en gelijk aan het extent van het kaartblad.
Toegevoegd: Default settings voor grid, kaartblad en schaal

Kaartblad aanmaken en grid aanmaken op basis van de volgende besrijving:
    Aanmaken tabel kaartbladen in dimensie-database en als laag toevoegen, styling rode rand stippellijn
    Tekenen van kilometergrid koppelen aan GRID evenementen
    Keuze aan gebruiker 1:25.000 of overig
    Bij 1:25.000 afstand grid-lijnen standaard instellen op 1000m, niet aanpasbaar
    Onderstaande geldt zowel voor 1:25k als overig
    Keuze voor het print formaat
    Keuze portrait of landscape
    Plaatsen tijdelijk kader op het canvas, kader valt altijd gelijk met kilometergrid (linksonder)
    Gebruiker kan de kaart slepen naar de gewenste positie, tijdelijk kader verspringt mee.
    Daarna aanmaken grid en kaartblad

Aangepast:  Laag "Kaartblad" geintegreerd met de laag "Grid". Deze 2 komen zo overeen dat het veel logischer is om dit in één kaartlaag en database-tabel te stoppen.


--3.2.8
Toegevoegd: Print-omgevingen voor alle papierformaten
Toegevoegd: Nieuwe installer gemaakt waarin zowel WFS als database-koppeling prallel kunnen worden aangemaakt. Dit resulteert ook in extra snelkoppelingen op het bureaublad. OP deze manier kan er bijvoorbeeld aan een productie geoserver worden gekoppeld en aan een test-database. De keuze kan worden gemaakt in de installer.
Toegevoegd: CoPI en UGS aan opstelplaatsen
Toegevoegd: Kaartblad zonder grid tekenen.
Fix:        Snappunt 0,0 (RD grid) niet toestaan
Fix:        Labelling van het grid, links in de onderhoek. Deze is bedoeld voor de labeling in GIS-applicatie, dus niet in het printen.
Fix:        n.a.v. testen aanpassingen aan de styling van de kaartlagen t.b.v. het printen
Fix:        Ook via de import functie onder repressief object de mogelijkheid om een GeoPackage te importeren. Bleek niet te werken.


--3.2.9
Toegevoegd: Mogelijk om meerdere kaartbladen en grids te tekenen bij één repressief object
Toegeveogd: Bij verwijderen van het GRID de mogelijheid om één grid te selecteren en niet direct alle grids te verwijderen welke bij dat object horen
Fix:        UI-formulier dreiging werkte niet
Fix:        Tekenen losstaand grid zonder kaartblad werkte niet meer
Fix:        Bij tekenen op bouwlagen en er wordt niet op een pand of bouwlaag geklikt, ontstond een python melding. Deze in de plugin afgevangen.
Toegevoegd: Readme.md
Aangepast:  Bereikbaarheid.sld, isolijnen.sld, labels_ruimtelijk.sld, labels_bouwlaag.sld
Toegevoegd: BAG vanuit de PDOK, via de plugin (configure, in het plugin menu) kan ingesteld worden welke BAG standaard wordt gebruikt. Dit wordt opgeslagen bij de plugin. De gebruiker kan zelf nog wel switchen van BAG-laag.


--3.3.0
Toegevoegd: Installer versie vernoemd naar een STAD -> Eindhoven
Toegevoegd: Label bij een opstelplaats
Toegevoegd: Kleine doorkijk naar multi-planvorming. In het IMROI model is het mogelijk om ook een multiplan op te slaan. Misschien zijn nog niet alle tekenmogelijkheden aanwezig in de plugin, maar het datamodel volstaat wel. Hiervoor alvast toegeveogd opstelplaats "politie" en sector "werkingsgebied RBP". Wordt nog niet aangeboden in de plugin.
Toegevoegd: Top10NL en Top25 aan achtergrondkaartlagen, afhankelijk van de print schaal is één van beide zichtbaar, vandaar dat ze in een groep staan.
Toegeveogd: 2 knoppen (help en float) op elke widget. Bij klikken op de help-button wordt de GitHub handleidingspagina geopend. Met de float-button kun je de dockwidget laten "zweven" en bijvoorbeedl op een 2e scherm zetten. Door ge help knop is dezelfde oude knop verdwenen.
Aanpassing: Zie database project, update scripts voor alle veiligheidsregio's en gemeenten
Fix:        Terrein UI, klopte niet


3.2.0-3.3.0 Verbeteren Plugin code
Gedurende de ontwikkeling van deze versie is er heel veel aangepast aan de structuur van de plugin.
- Constanten uit de code zijn verplaatst naar een apart constanten bestand
- Messages naar gebruikers zijn allemaal verplaatst naar een message bestand
- methods welke niet direct in de hoofdstructuur hoeven of vaak worden gebruikt zijn verplaatsts naar helper bestanden
- Queries naar de configdatabase zijn verzamelt in één bestand en worden aangeroepen vanuit de class waar nodig
- Veel linting aanpassingen zijn doorgevoerd op basis van PEP8
- logica vanuit oiv.py (main) is verplaatst naar oiv_basewidget.py. Hier hoort het ook thuis.
- meer gebruik gemaakt van parent-child relaties in de plugin voor de verschillende widgets
- child-widget calls parent variables inplaats van andersom. Hierdoor meer controle.
- GPL 3.0 licentie is toegevoegd
