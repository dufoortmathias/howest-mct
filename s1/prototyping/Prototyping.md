*Auteur: Tuur Vanhoutte*
# Hoofdstuk 1: Spanning
Een goede stroomkring heeft...
1) Bron
2) Verbruiker
3) Geleiders


## Bron
* AC (wisselspanning)
* DC (gelijkspanning)

## Verbruiker (=belasting)
* **Spanning** die een verbruiker aankan mag **nooit overschreden** zijn door de bronspanning
* **Stroom** die een verbruiker nodig heeft **moet groter** zijn dan de maximale stroom die een verbruiker nodig heeft.
* Heeft een interne weerstand (= de moeilijkheid dat de elektriciteit heeft om door de verbruiker te geraken)

## Geleiders
* Meestal koperen draden waar stroom kan doorvloeien
* Soms geisoleerd met plastiek, rubber, of onzichtbaar geisoleerd met doorzichtige vernis
* Kern van de geleider kan soepel of vast zijn
* Dikte: uitgedrukt in $mm^2$ of carré. Hoe dikker, hoe meer stroom er door kan
* Verschillende metalen (Cu, Al, ...) hebben verschillende geleidingscoefficienten
* Sommige geleiders worden gebruikt als zekerheid: dunne koperdraad die doorsmelt als er te veel stroom doorgaat

|Woord|Definitie|
|--|--|
|Netstroom adapter|**AC-DC converter**: zet wisselspanning om naar kleinere wisselspanning en daarna naar gelijkspanning|
|Gestabiliseerde bron|Bron die **continu dezelfde uitgangsspanning** heeft, onafhankelijk van de belasting. <br>Vb niet-gestabiliseerde DC bron: **batterij** (minder spanning na verloop van tijd, spanning afhankelijk van belasting)|
|Kortsluitstroom|In een elektrische kring: **geen verbruiker maar wel stroom**|
|Isolator|Materiaal dat geen elektronen geleid: kunststof, rubber, (droge) lucht. Dikte van het materiaal bepaalt de maximale spanning die kan geisoleerd worden|
|Zwerfstromen|Elektrische stromen die een andere weg nemen dan de gewenste stroomkring|
|Serie-schakeling|Na elkaar schakelen: 1 gemeenschappelijke verbinding|
|Parallel|Naast elkaar: 2 gemeenschappelijke verbindingen


## Controleren of een kring gesloten is
* Met multimeter op continuiteitstest (buzzer symbool), **zonder spanning**
* Bij gesloten kring: multimeter maakt piepgeluid en toont $0\Omega$
* Als er weerstand in de kring zit, kan dit (afhankelijk van het type meter) aangeduid worden door de multimeter

## Gevaren bij het werken met elektriciteit
* **Zwerfstromen van gelijkspanning** veel gevaarlijker dan van wisselspanning
* Weinig gevaar in hoogte spanning, vooral in grootte **stroom**

## Spanning meten
Waarom?
* Om te weten of een **spanningsbron gepast** is om de schakeling te voeden
* Om te weten of de **spanningsbron nog juist werkt**
* Om te weten of er AC of DC uit de bron komt
* Met Voltmeter/Multimeter
	* Heeft grote interne weerstand ($\approx 10M\Omega$) omdat de meter de schakeling niet mag beinvloeden door een extra stroom te laten vloeien door het meettoestel
* Altijd parallel meten: over het component

## Absolute Fout (AF)
= het verschil tussen een gemeten waarde en de exacte waarde

**Gegeven:**
* Bereik van 40V
* Resolutie 10 mV
* +/- 0.5% reading + 5dgt
* 17.35V afgelezen

**Gevraagd:**
De absolute fout
**Oplossing:**
$0.005 \cdot 17.35 V = 0.08675 V$
5dgt $=$ 5x resolutie $=5 \cdot 10mV = 50mV = 0.05V$
Totale fout: $0,08675V + 0,05V = 0,13675V$
Meting: tussen de $17,21$ en de $17,49V$  

## Procentuele fout
$= AF \cdot \frac{100\%}{meting}$
$= 0,13675 \cdot \frac{100\%}{17.35} = 0,78\%$

## Spanningswet van Kirchoff
De **som van de elektrische potentiaalverschillen** (rekening houdend met de richting) in elke gesloten lus is **gelijk aan 0**.


## Spanningsdelers
Wanneer we weerstanden in serie plaatsen zal er een spanningsdeler ontstaan (= de spanning zal zich verdelen over de 2 weerstanden)
Formule:
$V_{out} = V_{in}\cdot \frac{R_2}{R_1 + R_2}$

*Voorbeeld:*
We meten met de Arduino met pin A0 de spanning tussen R1 en R2 (de NTC). Als de NTC de waarde $10k\Omega$ aanneemt (bv bij $25\degree C$), dan zal de spanning gelijk verdeelt zijn over de 2 weerstanden:
$V_{out} = 5V \cdot \frac{10k\Omega}{10k\Omega + 10k\Omega} = 2.5V$
![enter image description here](https://i.imgur.com/QMKN3JU.png)

# Hoofdstuk 2: Stroom & wet van Ohm
* Stroom is afhankelijk van de spanningsbron en van de belasting in de kring:
	* Hoe **groter** de **spanningsbron**, hoe **groter** de stroom
	* Hoe **kleiner** de **weerstand** van de belasting, hoe **groter** de stroom
* Stroom is overal gelijk, tenzij ze opgesplitst wordt en later terug samenkomt.

## Stroom meten
* Om ervoor te zorgen dat de stroom door een component niet groter is dan de maximale stroom
* Amperemeter in serie plaatsen
	* Afzonderlijke poort voor stroom, maar nog altijd met COM-poort
* Zeer kleine weerstand, oppassen voor kortsluitingen
* Kan ook gemeten worden door een extra weerstand in serie te plaatsen. Dan gebruiken we de wet van Ohm om de stroom uit te rekenen aan de hand van de gemeten spanning
* Kan ook met een 'stroomspoel' zoals een stroomtang-meter (gemakkelijker maar duurder)

## Wet van Ohm
$R=\frac{U}{I}$
* Om de stroom op voorhand uit te rekenen
* Om maximale of minimale weerstand uit te rekenen
* Om spanning te berekenen wanneer de stroom en weerstand gekend zijn

Serieweerstand uitrekenen met wet van Ohm:
![enter image description here](https://i.imgur.com/jwd5m02.png)
$R=\frac{U}{I}$ met:
* $U= U_{bron} - U_{led}$
* $I=$ opgegeven stroom $=7$ mA
* $R=\frac{5V-1.8V}{0,007A} = 457 \Omega$ 

**!!! Opgelet !!!**
Als $U_{bron} - U_{led}$ heel klein wordt ten opzichte van de $U_{bron}$, kan een kleine afwijking van $U_{bron}$ of $U_{led}$ een grote afwijking in stroom veroorzaken.

# Hoofdstuk 3: Weerstanden
## Soorten weerstanden:
* **Gewone** weerstand
* **Temperatuur**-gevoelige weerstanden ("Thermistors")
	* NTC: Negatieve Temperatuur Coefficient
		* Kouder $\rightarrow$ hogere weerstandswaarde
	* PTC: Positieve Temperatuur Coefficient
		* Warmer $\rightarrow$ hogere weerstandswaarde
* **Licht**gevoelige weerstanden (LDR)
	* Voordelen
		* Goedkoop
		* Verdragen in sper spanningen tot 100V+
	* Nadelen
		* Snelle veroudering
		* Grote toleranties op de elektrische waarden
* **Rek**gevoelige weerstanden (rekstrookje)

## Weerstand vastmaken aan een PCB:
* **Through-hole / thru-hole**:  weerstand gaat door gaten in het PCB, onderaan vastgemaakt
* **Surface mounted (smd)**: weerstand wordt vastgemaakt op de bovenkant van het PCB

## Aanduiding weerstandwaarde
* Met kleurencode:
	* 4/5/6 banden
	* Soms is de waarde op de weerstand gedrukt
* Weerstand altijd **spanningsloos** meten, met de weerstand los uit de kring

## Vermogen
= verbruik (dissipatie) van een toestel of onderdeel
Bij weerstanden:
= maximale warmte die verbruikt kan worden door een weerstand (gespecifieerd door fabrikant)

$P=U\cdot I$ (bij DC)
$P=U\cdot I \cdot \cos(\phi)$ bij AC


### Voorbeeld 1
**Gegeven:**
* $R=470\Omega$
* $U_{R}=3.2V$
* $I=6.80mA$

**Gevraagd:**
$P_{max}$

**Oplossing:**
$P_{max}$
$= U \cdot I$
$= 3.2V \cdot 0.0068A$
$= 0.021W$
$= 21mW$

---

### Voorbeeld 2
**Gegeven:**
$R=100\Omega$
$U=12V$

**Gevraagd:**
$P$

**Oplossing:**
$R = \frac{U}{I}$
$\Leftrightarrow I = \frac{U}{R}$
$I = \frac{12V}{100\Omega} = 0.12A$
$P = U \cdot I$
$=12V \cdot 0.12A$
$=1.44W$

## Serieschakelen van weerstanden
$R_{totaal} = R_1 + R_2$

## Parallelschakelen van weerstanden
$\frac{1}{R_{totaal}} = \frac{1}{R_1} + \frac{1}{R_2}$

Of bij 2 weerstanden:

$R_{totaal}=\frac{R_1 \cdot R_2}{R_1+R_2}$

### Voorbeeld: vereenvoudig volgende schakeling
![enter image description here](https://i.imgur.com/1JIhnXR.png)

* $R_3$ en $R_4$ samennemen:

$\frac{1}{R_{34}} = \frac{1}{R_3} + \frac{1}{R_4}$
$= \frac{1}{12} + \frac{1}{6}$
$= \frac{1}{4}$
$R_{34}=\frac{1}{\frac{1}{4}} = 4\Omega$ 

* $R_1$ en $R_{34}$ samennemen:

$R_{134}=8\Omega+4\Omega$
$=12\Omega$

* $R_2, R_5$ en $R_6$ samennemen:

$R_{256}=7\Omega+6\Omega+5\Omega$
$=18\Omega$

* $R_{134}$ en $R_{256}$ samennemen:

$\frac{1}{R_{123456}}=\frac{1}{R_{134}} + \frac{1}{R_{256}}$
$=\frac{1}{12} + \frac{1}{18}$
$=\frac{5}{36}$

$R_{123456}=7.2\Omega$

---

# Hoofdstuk 4: Diodes
### Vermogen van een adapter
DC vermogen $\neq$ AC vermogen

## De diode
= geleider in 1 richting, te vergelijken met een terugslagklep voor water
* Heeft een anode en een kathode (KNAP: Kathode Negatief, Anode Positief)
* Heeft altijd een opgegeven maximale stroom. Hoger $\rightarrow$ ontploft/kortsluiting!
* Spanning: meestal $0.7V$
* Kan gebruikt worden om logische poorten te maken (AND-gate, OR-gate, ...)
* Diode meten: **Altijd spanningsloos met het component uit de kring**

### Zenerdiode
= halfgeleiderdiode die zo geconstrueerd is dat er ook spanning mogelijk is in sperrichting, wanneer de spanning groter is dan de zenerspanning. De spanning blijft dan constant over een relatief groot bereik van stroomsterkte.
![enter image description here](https://upload.wikimedia.org/wikipedia/commons/thumb/5/5a/Diode-Zener-EN_A-K.svg/250px-Diode-Zener-EN_A-K.svg.png)
![enter image description here](https://upload.wikimedia.org/wikipedia/commons/thumb/4/4a/3.4V_Zener_diode_V-A_characteristic.svg/300px-3.4V_Zener_diode_V-A_characteristic.svg.png)

De zenerspanning in bovenstaande figuur bedraagt dus $3.4V$. Dit will zeggen dat als de zenerdiode in sper staat, hij toch stroom zal doorlaten vanaf de spanning 3.4V bedraagt. De zenerdiode zal, net zoals een gewone diode, in doorlaat stroom geven vanaf $0.65V$.
Toepassing zenerdiode: stabiliseren van een spanningsbron

## LEDs
= Light-Emitting Diode
* Elektronische halfgeleidercomponent die licht uitzendt als er een elektrische stroom **in doorlaatrichting** doorheen loopt.
* Ingebouwd in een kleine doorzichtige behuizing, die als lens werkt.
* Heeft ook een **anode en kathode**: laat alleen stroom door in 1 richting
* Stroom moet begrensd worden door een weerstand


# Hoofdstuk 5: Batterijen

## 2 soorten
|Oplaadbaar|Niet-oplaadbaar|
|--|--|
|Ecologisch||
|Duurder in aankoop|Goedkoper in aankoop|
|Goedkoper in gebruik||
|Veel zelfontlading|Weinig zelfontlading|

## Chemische opbouw
* Chemische reacties $\Rightarrow$ elektrische stroom
* 2 polen van verschillend soort materiaal, gescheiden door laag elektrolyt
* **Droge** batterijen
	* Volledig gesloten
	* Onderhoudsvrij
	* Levert energie in alle standen
* **Natte** batterijen
	* Vloeibare stof = elektrolyt
	* Niet volledig gesloten $\rightarrow$ kan uitlopen als batterij niet vlak staat
* Spanning zakt naarmate er vermogen uitgehaald is, door de interne weerstand van de batterij
* Verschillende spanning tussen gelijke vormen bij wel- of niet-oplaadbare batterijen

## Zelfontlading
= afname in capaciteit bij een accu zonder dat er belasting op aangesloten is
* Bij natte accu: 15% per maand
* Bij AGM accu: 3% per maand
* Bij gel accu: 2% per maand
* Alkaline: 7 jaar houdbaar (2% per jaar)
* Lithium: 10 jaar houdbaar (1% per jaar)
* Oplaadbare batterijen: **1% per dag**

### Factoren voor meer zelfontlading:
* Hoge temperatuur
* Kruip (sluip) stromen
* Sterke vervuiling/vocht tussen de polen

## Capaciteit van een batterij
Uitgedrukt in mAh of Ah: milli-Ampere-uur of Ampere-uur
**Vb:**
* Een batterij van 2400mAh levert...
	* 1 uur lang 2400mA
	* 2 uur lang 1200mA
	* 4 uur lang 600mA
	* ...

### Meten capaciteit
Gebeurt door rustig een batterij te belasten tot hij leeg is
* Manieren om een batterij te belasten:
	* Stroom variëren
	* Periodieke belasting (continue belasting) = geleidelijk ontladen

## Serie/parallel-schakelen van batterijen
* Serie
	* Hogere spanning
	* Zelfde maximale stroom
	* Meer energie
	* **Vb:** elektrische auto's
* Parallel
	* Eventuele verschillen in interne weerstand van batterij
	* Altijd met 2 identieke batterijen, anders vermogensverlies
	* Kan wel met diodes, maar dan met *klein* vermogensverlies van diode

## Geheugeneffect oplaadbare batterijen
= negatief effect bij opladen batterijen voor ze volledig leeg zijn.

|Batterij|Eigenschappen|
|--|--|
|Nickel-Cadmium|<ul><li>onstaan van klontjes van kristal in de batterij</li><li>kristallen klitten samen tot een steeds dikkere laag $\Rightarrow$ beschikbare energie wordt kleiner</li></ul>|
|Nickel-Hydride|Geen last van dit geheugeneffect $\Rightarrow$ op elk moment probleemloos oplaadbaar|
|Li-Lion|<ul><li>geen geheugeneffect</li><li>duurder in aanschaf</li></ul>|

## UPS
= Uninterruptable Power Supply
* Soort grote batterij
* Kan het elektriciteitsnet niet semipermanent vervangen, dus UPS is geen noodstroomvoeding
* Kan een maximaal vermogen afgeven (vb 2000VA)
* Tijdsduur is afhankelijk van de capaciteit van de batterij
* Betrouwbaarste methode: **double-conversion**-methode:
	1. De netspannning (AC) wordt altijd omgezet in DC. 
	2. De gelijkspanning (DC) laadt de accu's op.
	3. De gelijkspanning van de accu's wordt weer omgezet in wisselspanning. De beveiligde apparatuur werkt dus altijd op de stroom van de accu's die continu worden bijgeladen.

### Nobreak-installatie
* **Noodstroominstallatie** die de netspanning kan overnemen **zonder onderbreking**
* Gebruikt een combinatie van **UPS en een noodstroomaggregaat**
* UPS verzorgt voeding tijdens eerste minuten
* Noodstroomaggregaat neemt dan semipermanent over en laadt de UPS weer op.


# Hoofdstuk 6: Condensator
= een elektrische component die elektrische lading (energie) opslaat. 
## Eigenschappen
* Opgebouwd uit twee geleiders met een relatief groot oppervlak, die zich dicht bij elkaar bevinden en gescheiden zijn door een niet-geleidend materiaal of vacuum, het dieëlectrum
* Als de ene geleider positief geladen wordt tov de andere $\bold\Rightarrow$  moleculen die verbonden zijn aan elektronen in het dieëlectrum verplaatsen verplaatsen zich een beetje naar de positief geladen geleider.
* Heeft een maximum spanning
* Wordt soms 'minibatterij' genoemd

## Capaciteit van een condensator
= vermogen van een condensator om lading op te slaan
= coulomb per volt = $\frac{q}{U}$

* Meer lading in een condensator $\Rightarrow$ meer spanning over de condensator
* Eenheid: Farad $(F)$, soms in $nF$, $\mu F$ of in $pF$

Capaciteit is afhankelijk van:
* oppervlakte van de geleiders (grotere oppervlakte $\Rightarrow$ meer capaciteit)
* Afstand tussen de geleiders (grotere afstand $\Rightarrow$ meer capaciteit)
* Dieëlectrum (het materiaal of het vacuum) tussen de geleiders

### Dieëlectrum
= Het niet-geleidend gedeleelte of vacuum tussen de geleiders
* Laat in de praktijk toch een kleine lekstroom door
* In schakelschemas wordt dit in rekening gebracht middels een grote weerstand die parallel staat aan de condensator
* Er is een bovengrens aan de sterkte van het elektrisch veld dat tussen de geleiders van een condensator kan worden aangelegd: de **doorslagspanning**

## Formule voor het opladen van de condensator op DC
$U_c = U_b \cdot (1-e^{\frac{-t}{RC}})$

Waarbij:
* $U_c =$ spanning over de condensator
* $t =$ tijdstip van meting
* $R =$ weerstandswaarde in $\Omega$
* $R\cdot C = \tau$ (tau) $=$ tijdsconstante
* $U =$ bronspanning

### Conclusie
* Hoe kleiner de weerstand, hoe sneller opgeladen
* Hoe groter de condensator, hoe trager opgeladen

$R\cdot C = \tau$ noemt men de tijdsconstante:
* 1 tijdsconstante =  de tijd nodig om 63% van de maximum spanning te bekomen
* Men zegt dat een condensator na 5 tijdsconstanten "$\tau$" volledig geladen is
* $\Rightarrow$ Logaritmische functie

## Formule voor het ontladen van de condensator op DC
$U_c = U_b \cdot (e^{\frac{-t}{\tau}})$
## Stroom naar en van de condensator
* Bij het opladen gaat er in het begin een grote stroom naar de condensator, die dan na verloop van tijd afneemt
* Hierbij is de weerstand $R$ bepalend voor de initiële stroom

## Serie en parallel schakelen van de condensator
= omgekeerde als bij weerstanden
### Serie
* Waarde wordt kleiner
* $\frac{1}{C_{totaal}} = \frac1{C_1} + \frac1{C_2}$

### Parallel
* Waarde wordt groter
* $C_{totaal} = C_1 + C_2$

## Polariteit
* Sommige elektrolitische condensatoren hebben een polariteit
* Bij deze is de isolatielaag tussen de 2 platen zo opgebouwd dat deze dikker wordt bij de juiste, en dunner bij de verkeerde polarisatie
* Deze laag kan zo dun worden dat de condensator in kortsluiting gaat en ontploft

## Gebruik van de condensator
* Om gelijkstroom te blokkeren maar wisselstroom door te laten (bij bv luidsprekers, anders zal de luidspreker misschien te veel stroom krijgen en doorbranden)
* Om spanningsschommelingen af te vlakken, bijvoorbeeld in gelijkrichters
* Samen met een weerstand als tijdbepalend element in een geintegreerde schakeling zoals de NE555, in elektrische klokken, wekkers, timers
* In frequentiefilters, bijvoorbeeld in audiotoepassingen
* In de vorm van een condensatormicrofoon
* Om de positie van een vinger te bepalen bij de meeste moderne touchscreens. De vinger verandert in een capacitief veld
* Om vermogen gepulst af te geven, zoals bij de flits van een camera, gepulste lasers, elektromagnetische wapens (railgun), ontstekingen van kernwapens. Hierbij wordt de condensator als extra energiebuffer gebruikt: traag opladen, snel energie afgeven
* Als impedantie in een wisselspanningschakeling met als voordeel geen of minder ohms te verliezen door warmte. Bv: een condensator in serie met een AC motor om het toerental te verminderen
* Ontdenderen van een knop

# Hoofdstuk 7: Solderen
## Solderen
* Met soldeertin (= legering van metalen)
## Desolderen
* Desoldeerpomp
* Desoldeerlint (litze)
* Desoldeerbout (duur)
## Andere methodes
* Kroonsteentje "suikerke"
* Rond elkaar draaien en beetje tape erover
* Krokodillenklem
## Krimpkous
= Plastiek dat krimpt bij warmte

# Hoofdstuk 8: Electronische schakelaars
* Transistor
* Relais
* Optocoupler
* Solid state relais

## Transistor
= halfgeleidercomponent dat dient om elektronische singalen te versterken of te schakelen. 
* De transistor is de fundamentele bouwsteen van computers en vele andere elektronische schakelingen
* Soms gebruikt als afzonderlijke componenten, maar hoofdzakelijk komen ze voor als fundamentele bouwstenen van geintegreerde schakelingen
### Transistor als schakelaar of stroomversterker
* Om met een kleine stroom een grotere stroom in of uit te schakelen
* Voorbeeld NPN-transistor: 
![enter image description here](https://i.imgur.com/JntBIEW.png)
* Bij een PNP transistor staat de pijl gericht van emitter $\rightarrow$ base, ipv base $\rightarrow$ emitter
* 5V - resistor - led = collector
* 5V stuursignaal  = base 
* GND = emitter

#### Voordelen transistor als schakelaar
* Met een kleine stroom een grotere stroom inschakelen
* Het schakelen gaat heel snel (bv. kan PWM volgen)
* Transistor is redelijk klein, dus gemakkelijk toe te voegen

#### Nadelen transistor als schakelaar
* Maximum stroom van de transistor mag niet overschreden worden
* Massa's hangen aan elkaar (met NPN-transistor) $\rightarrow$ geen elektrisch gescheiden kring
* Klein spanningsverlies over de uitgang $\rightarrow$ opwarming van het component
* Kan enkel DC spanning schakelen

### Open collector uitgang met een interne transistor
= combinatie van verschillende transistoren
* Geeft voordeel dat de voedingsspanning van het stuurbordje en van de aangestuurde belasting verschillend zijn (kan lager of hoger zijn, bv met 5V een belasting van 12V inschakelen)
* Maximale uitgangsstroom wordt gespecifieerd door fabrikant van de IC (Integrated Circuit), bv 1A

![enter image description here](https://i.imgur.com/hyhfEgA.png)
### De FET
= spanningsgestuurde transistor (in plaats van stroom)

Transistors hebben drie aansluitingen met elk een eigen functie en een eigen naam.
* Voor een bipolaire transistor zijn dat:
	1.  basis (B),
	2.  emitter (E),
	3.  collector $\text{(C)}$
* Voor een veldeffecttransistor (FET) zijn dat:
	1.  gate (G),
	2.  source (S),
	3.  drain (D)
## Relais
* Met een relais kan je met een kleine spanning en stroom een grotere spanning en stroom inschakelen
* Voordeel: galvanische scheiding tussen de 2 circuits
* Vb: Arduino (5V DC) die 230V netspanning schakelt
* Spoel meestal aangestuurd met een transistor, omdat de spoel rare overgangsverschijnselen heeft bij het in/uit-schakelen, en kan daardoor de arduino/RPi beschadigen.

![enter image description here](https://i.imgur.com/GQkzkSB.png)

### Voordelen relais als schakelaar
* Met een kleine stroom een grote stroom schakelen
* Met een kleine spanning een grote spanning schakelen
* Er kunnen verschillende kringen in 1 keer geschakeld worden, zowel NO (Normal Open) als NC (Normal Closed)
* Veiligheid door elektrische isolatie tussen de stuurkring en het schakelgedeelte
* Kan zowel AC als DC schakelen

### Nadelen
* Werkt niet zo snel (mechanische beweging)
* Kan verslijten door vonken wanneer er op een verkeerd moment ingeschakeld wordt
* Maakt lawaai
* Kan door vonken effecten hebben op de omgeving

## Solid State Relais (SSR) of halfgeleiderrelais
* Werkt zoals een gewone relais: heeft een in/uitgangskant, geisoleerd
* Geen mechanisch bewegende delen ("halfgeleiderrelais")
* Schakelt AC in bij de nuldoorgangen

![enter image description here](https://www.phidgets.com/docs/images/d/df/SSR_Internals.png)

### Voordelen SSR als schakelaar
* Een SSR dooft steeds bij het nulpunt. Dankzij het triggerblok, of nulpuntschakelaar, zal de SSR weer ontsteken bij de volgende nuldoorgang. Zo ontstaan er geen plotse inschakelstromen, die bvb hoogfrequentiestoringen kunnen veroorzaken, die op hun beurt het net vervuilen.
* Bevat geen bewegende delen, alles gebeurt elektronisch $\Rightarrow$ onmogelijk om vonken te veroorzaken $\Rightarrow$ kan gebruikt worden in ruimten waar explosiegevaar dreigt
* Verlengde levensduur (door ontbreken mechanische wrijving)
* Geluidloos
* Aanstuurvermogen is zeer beperkt (komt rechtstreeks vanuit een logische schakeling)
* Snelheid SSR veel hoger dan van een gewone relais

### Nadelen SSR als schakelaar
* De nulpuntschakelaar zorgt voor een in-en uitschakelvertraging. Kan relatief groot zijn: maximaal de helft van de periode (bij een frequentie van 50Hz: $\frac{\frac1{50}}{2} = 10$ms
* Prijs is recht evenredig met de stroom die het component kan schakelen. 
* Kan slechts 1 circuit schakelen, terwijl goedkopere mechanische relais meerdere kunnen schakelen
* Bij deels inductieve (of capacitieve) belasting het SSR problemen kan krijgen met op het juiste moment te schakelen. Dat komt omdat de het SSR (type AC) schakelt op de nuldoorgangen van de sinusvormige spanning en stroom. Deze nuldoorgangen kunnen als gevolg van faseverschuivingen uit elkaar liggen.
* Een SSR kan dus niet onvoorwaardelijk (inductieve) elektromotoren schakelen. Een (Mono-/Bi-stabiele) relais met schakelcontacten heeft hier geen last van.

## Optocoupler / opto-isolator
= kleine geintegreerde schakeling waarin zich een LED en een lichtgevoelige transistor bevinden
* Door een bepaalde spanning over de LED zal de transistor geleiden
* Zorgt voor een galvanische scheiding die gemakkelijk toe te passen is in kleine elektronische schakelingen
* Kan zowel als input en output gebruikt worden

### Intern schema
![enter image description here](https://i.imgur.com/g0oIZUO.png)
* Links: de LED
* Rechts: de transistor uitgang
* De LED is dus de base van de transistor.

### Voordelen optocoupler als schakelaar
* Met een kleine stroom, een grote stroom schakelen
* Elektrische isolatie tussen stuurkring en schakelgedeelte
* Kan als input gebruikt worden (met extra weerstand)

### Nadelen optocoupler als schakelaar
* Kleine spanningsverlies over uitgang $\Rightarrow$ de optocoupler ontwikkelt warmte
* Beperkte uitgangsstroom, volgens component
* Grotere ingangsspanning nodig om LED te laten branden
* Enkel DC

# Hoofdstuk 9:  Motor + motorsturing
### Soorten motors
* DC
* AC
* Servo motor
* Stappen motor (=Stepper motor)

## DC Motor
* Werkt enkel op DC
* Spanning is gedefinieerd volgens de fabrikant
* Kan meestal in 2 richtingen draaien, door omkeren van polariteit van de bron tov de motor
* **Toerental / vermogen / koppel is afhankelijk van de uitvoering**. 
	* Er bestaan types met een reductie op de hoofdas
	* Om het toerental te weten, dien je een sensor op de motor te plaatsen
		* Magnetisch zoals op een fietswiel voor de km teller (=Hall sensor)
		* Optisch
* Heeft meestal borstels (kooltjes) om de spanning over te brengen naar de rotor in het midden. Op deze borstels kan slijtage optreden
* Zit ook in smartphone (trilmotor)

### Sturing draairichting
![enter image description here](https://i.imgur.com/3yzuG2v.png)
### Arduino motor stuurbord
* Meestal wordt er gebruik gemaakt van een PCB met een L398 op om een arduino DC motors te laten sturen
* Deze print is voorzien voor 2 motoren in een H-brug te schakelen, en heeft ook een PWM ingang om de snelheid te regelen
* Tevens heeft deze PCB ook een spanningsregelaar aan boord, zodat er 5V kan afgetakt worden, om bv de arduino te voeden. 
* Opgepast: de motoren zijn niet gevoed na de spanningsregelaar, zodat de snelheid ook afhankelijk is van de toegevoerde spanning

![enter image description here](https://cdn.instructables.com/F93/HPKM/ID2XEAO7/F93HPKMID2XEAO7.MEDIUM.jpg)

## AC motor
* Werkt op AC (230V, 400V, ...)
* Draairichting is bij enkelfasige wisselspanningsmotoren niet te veranderen, wel bij driefasige motoren
* **Toerental afhankelijk van frequentie** dat de stroom gestuurd wordt
* Ofwel aan/uit met relais
* Ofwel in toerental met frequentieregelaar
* Er dient zeker een tussen bord gebruikt te worden met een Arduino of RPi. Rechtstreeks aansturen kan niet


## Servo motor
* Zorgt niet voor een volledig ronddraaiende beweging, maar voor een **180 graden beweging**, met juiste positie
* Er bestaan soorten servo motoren met verschillend koppel(kracht)
* Is in principe een DC motor met terugkoppeling, zodat deze weet waar hij staat.
* Door de 3-draad aansluiting van de servo kunnen we deze direct door een arduino/RPi aansturen. De energie komt van de voedingspin van de servo
* Wordt aangestuurd met PWM, maar wel met een specifieke timing. Met een periode van 20ms en een puls tussen de 0.7 en 2ms. De gewone analoge output van de Arduino lukt moeilijk.
* De voeding kan van een externe voeding komen, of van de Arduino zelf als er bvb maar 1 servo gebruikt wordt

![enter image description here](https://i.imgur.com/Be2mvUN.png)

### Toepassingen servo
* Modelbouw vliegtuig (flappen, roer)
* Arduino auto's (vb sensor ultrasoon)
* Grotere servo motoren worden in vb lasautomaten en inpakmachines gebruikt.

## Stappenmotor
= borstelloze, synchrone elektromotor, waarvan de hoekverdraaiing nauwkeurig te beheersen is. 
* De rotor bevat permanente magneten, de stator is opgebouwd uit elektromagneten
* De hoge resolutie wordt bereikt door zowel de stator als de rotor van een aantal polen te voorzien, zodat zij geen gemeenschappelijke factor bezitten. 
* Telkens als er een wikkeling bekrachtigd wordt, komt een pool in de rotor recht tegenover een pool in de stator te staan, waardoor de rotor een klein stukje draait.
* Een nog hogere resolutie kan worden bereikt door naast elkaar gelegen wikkelingen gelijktijdig en verschillend te bekrachtigen
* De belangrijkste karakteristieke eigenschap van een stappenmotor is het koppel dat hij kan leveren. De motor kan ook koppel leveren als hij stilstaat en kan daarom als standrem fungeren.
### Aansturing 
* Net als een synchrone wisselspanningsmotor wordt de stappingsmotor in het ideale geval aangestuurd met zuivere sinusvormige stromen.
* Hierdoor is een vloeiende beweging mogelijk, maar dit is bezwaarlijk voor de besturing: een analoge vermogingsschakeling heeft hoge verliezen.
* In de praktijk: vaak een digitale aansturing, die gebruik maakt van pulsebreedtemodulatie (PWM). 
* Eenvoudigere besturingen maken slechts 1 puls per stap.

Gezien de lage weerstand van 1 spel van de stappenmotor, mag deze niet rechtstreeks aangesloten worden op de Arduino of RPi. Dit dient zeker te gebeuren met een transistor of transistorarray (zoals in labo's)

### Toepassingen van de stappenmotor
Vooral de preciese positionering is handig:
* Scanners / copy machine / printer
* 3D printers, lasercutters
* Harde schijven
* Lichteffecten (moving head scanners)


## Gelijkrichterschakelingen / gelijkrichters
= eenvoudige schakelingen die de wisselspanning omvormen naar een zuivere gelijkspanning
*Voorbeeld:* gelijkrichters combineren met een transformator die de 230V omzet naar 12V wisselspanning, en die dan met behulp van de gelijkrichter DC wordt
* 2 soorten: enkelzijdige en dubbelzijdige gelijkrichting
* Oppassen met de spanningswaardes, bij wisselspanning is de opgegeven waarde de RMS waarde:

![enter image description here](https://i.imgur.com/LiH4WDu.png)
### Enkelzijdige gelijkrichting
Gebeurt met behulp van een diode die de positieve of negatieve zijde van een wisselstroom doorlaat en de andere zin tegenhoudt. De rimpel bij deze vorm van gelijkrichting is redelijk groot en de resulterende effectieve spanning zal bij enige belasting relatief laag zijn.

![enter image description here](https://upload.wikimedia.org/wikipedia/commons/thumb/5/58/Halfwave.rectifier.en.svg/1024px-Halfwave.rectifier.en.svg.png)
### Dubbelzijdige gelijkrichting
Bij dubbelzijdige gelijkrichting worden zowel de positieve als de negatieve componenten van de ingangsspanning benut. De rimpel is hier kleiner dus de resulterende effectieve spanning zal hoger zijn.

![enter image description here](https://upload.wikimedia.org/wikipedia/commons/thumb/d/d5/Gratz.rectifier.en.svg/1024px-Gratz.rectifier.en.svg.png)
Anders getekend: 
![enter image description here](https://i.imgur.com/11T1s7A.png)
Uitgangsspanning, en eronder afgevlakt met condensator:
![enter image description here](https://i.imgur.com/0P45vp7.png)

* Zeker rekening houden met de waardes van de spanningen van AC en DC
* Dubbelzijdige gelijkrichting met condensator: 
	* AC spanning = 12V $\rightarrow$ DC spanning = $(12 * \sqrt2) - (2\cdot0.7)=15.57V$


# Hoofdstuk 10: Sampling, buffers
## Sampling van audio signalen
* Om geluid of andere in de tijd varieerende analoge signalen in te lezen in de computer wordt gebruik gemaakt van sampling
* *sample* = 'voorbeeldexemplaar', 'steekproef' of 'monster'. 
* De term wordt gebruikt bij digitale signaalbemonstering en in de context van digitale muziek/geluid.
* In digitale signaalbemonstering: sample = de momentane waarde van het betrokken signaal: een signaalmonster genomen op 1 tijdstip. 
* Door bemonstering (sampling) van het signaal op opeenvolgende tijdstippen, ontstaat een digitaal signaal.

## Bemonsteringfrequentie
* De bemonsteringfrequentie geeft aan, hoeveel van deze samples per seconde worden genomen. 
	* Bij de compact disc is dit 44.1kHz: 44.100 monsters per seconde. 
	* Hogere samplingfrequenties: in professionele en hoogkwalitatieve toepassingen gebruikelijk: 48kHz, 96kHz, 192kHz en zelfs 2.8MHz
* Een sample wordt gekwantiseerd en daarbij gecodeerd met een bepaald aantal bits. Veelgebruikte aantallen bits per sample zijn 8, 16, 24, of 32 bits.
* Er kunnen geen frequenties hoger dan de helft van de samplefrequentie gereproduceerd worden, daarom mogen deze ook niet gesampled worden, anders bekom je verkeerde signalen

## Informatieverlies door sampling
* Heeft niets te maken met compressie
	* Daar worden in software bewerkingen uitgevoerd om minder data te hebben

## Geluid reproduceren
* Met behulp van een luidspreker of piezo element kan geluid gemaakt worden vanuit een toestel zoals de Arduino of RPi
* Werking luidspreker:
![enter image description here](https://stefano357.files.wordpress.com/2012/10/werking_luidspreker2.jpg)
1. Stroom vloeit door de spoel bij een audiosignaal
2. Dat creeërt een magnetisch veld dat interactief zal zijn met het veld van de permantente luidsprekermagneet
3. Bij een alternerende stroomdoorgang de conus permanent oscilleren met een ritme gelijk an de frequentie van het toegevoerde elektrische signaal
4. De versterker zal constant de polariteit van het elektrische audiosignaal wijzigen waardoor de conus van de luidspreker naar voor en achter beweegt.

## 'Level' problemen
* Logische niveaus van IC (Integrated Circuits), verschillende spanningen die verwacht worden

### Spanningen die te hoog zijn
* Kan soms ongemerkt fout zijn
* Arduino: 5V in/out
* RPi: 3.3V in/out
* Extra modules: 5V of 3.3V, nooit beide samen
* Vb: 
	* 5V module uitgang naar 3.3V input
	* Gevolg: 3.3V input kan defect gaan
* Soms is de ingang beveiligd, maar soms niet op een voor ons bruikbare beveiliging

### Spanningen die te laag zijn
* Opgepast om te lage spanningen aan te bieden aan inputs
* Vb: 3.3V module die 5V input stuurt
* De input kan mogelijks geen digitale 1 van de 3.3V module zien (kan gelukkig geen defecten veroorzaken)

### Oplossing: Level Shifter

![enter image description here](https://www.superdroidrobots.com/images/TE/TE-298-000-A.png)
* Gaat van ene niveau naar andere
* Soorten:
	* Unidirectioneel: werkt in 1 richting bvb van 3.3V naar 5V
	* Bidirectioneel: $\text{I}^2\text{C}$ bus (werkt in beide richtingen gelijktijdig)
		* $\text{I}^2\text{C}$= Inter-Integrated Circuit
## Schmitt-trigger
= de oplossing voor trage overgangssignalen
= een comparatorschakeling die twee spanningsdrempels heeft:
1. Wanneer de ingangsspanning het bovenste niveau overschrijdt, krijgt de uitgang het logische niveau 'hoog'
2. Wanneer de ingangsspanning zakt onder het onderste niveau, wordt de uitgang weer laag
Figuur: A = gewone comparator, B = schmitt-trigger.
![enter image description here](https://upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Smitt_hysteresis_graph.svg/250px-Smitt_hysteresis_graph.svg.png)
* Er bestaan ook geinverteerde Schmitt-triggers: 
	* de uitgang van de geinverteerde trigger geeft het omgekeerde logische niveau aan de uitgang
	* wordt in de meeste toepassingen gebruikt

### Symbolen
![enter image description here](https://upload.wikimedia.org/wikipedia/commons/thumb/b/b3/Schmitttrigger_NL.svg/260px-Schmitttrigger_NL.svg.png)


## Opamp
= analoge buffer/versterker
= *operational amplifier* (=operationele versterker)
* Kan gebruikt worden om te versterken (hoge versterkingsfactor)
* Kan gebruikt worden om te bufferen, zodat de voorgaande schakeling geen invloed heeft 
* Kan gebruikt worden om wiskundige bewerkingen uit te voeren
* Kan zowel analoge als digitale signalen bufferen
* Opgepast: opamp heeft ook voedingsspanning nodig, enkel of dubbel, staat dikwijls niet op schema
* Heeft 2 inputs: de inverterende input (-) en niet inverterende input (+) en 1 output.

### Schema buffer:
![enter image description here](https://upload.wikimedia.org/wikipedia/commons/a/a8/OP_Impedanzwandler.png)
* Bij een buffer schakeling geldt er een versterkingsfactor van 1
* Hij werkt als impedantie-omvormer: van een hoge (ingangs)impedantie naar een lage (uitgangs)impedantie. Op die manier wordt vermeden dat een signaalbron belast wordt door een daaropvolgende schakeling.

### Halve voedingsspanning
* De weerstandsdeling zorgt ervoor dat de spanning gehalveerd wordt
* De buffer zorgt ervoor dat de halve spanning niet afwijkt als er een extra belasting wordt aangesloten
![enter image description here](https://i.imgur.com/zE7qOba.png)


### Typische opamp schakeling
![enter image description here](https://upload.wikimedia.org/wikipedia/commons/thumb/6/66/Operational_amplifier_noninverting.svg/220px-Operational_amplifier_noninverting.svg.png)
* Versterkingsfactor: positieve versterker: $V_{\text{out}} = (1 + \frac{R_f}{R_g}) * V_{\text{in}}$
* Positieve versterker: wordt gebruikt voor het aanpassen van niveau's om ene optimale digitalisatie te kunnen doen (maximaal aantal bits gebruiken)

### Pin nummering IC's

![enter image description here](https://www.amiga-stuff.com/hardware/images/DIP-numbering.gif)
* DIP IC (zoals in labo): Pin nummer 1 begint aan het bolletje / links van de inkeping.
* Telling gaat verder en draait rond

# Hoofdstuk 11: PCB's
= Printed Circuit Board
= Printplaat
= plaatje waarop door middel van koperbanen verbindingen worden gemaakt tussen elektrische componenten die je er zelf op soldeert

## Stappen om een PCB te maken
1. Ontwerpen van de printplaat / layout
2. PCB online bestellen of zelf maken:
3. Belichting van de PCB met de geprinte (op kalkpapier/transparant) layout met UV licht
4. Fixeren van de belichte print
5. Etsen van de print
6. Gefixeerde beschermlaag verwijderne met bv acetone, want op de beschermlaag kan je niet solderen
7. Gaatjes boren

## Enkelzijdige vs dubbelzijdige PCB's
* Enkelzijdig is gemakkelijk
* Dubbelzijdig: opletten voor doormetalisaties. Als je de print zelf maakt, moet je deze doormetalisaties zelf organiseren
* Anders online prototype van PCB bestellen, valt nog mee in prijs

## Driehoek - Ster formatie
![enter image description here](https://upload.wikimedia.org/wikipedia/commons/c/cd/Ster_driehoektransformatie.png)
= Manier om bepaalde schakelingen op te lossen
### Formules

* Van driehoek naar ster:
![enter image description here](https://wikimedia.org/api/rest_v1/media/math/render/svg/8327805c60e208fcd2ad2876e4b64d0a64d24678)

* Van ster naar driehoek:
![enter image description here](https://wikimedia.org/api/rest_v1/media/math/render/svg/e15438ca5d202169cb60af04e745b99ffd49ee96)


<!--stackedit_data:
eyJoaXN0b3J5IjpbLTU0MjAwOTQwNiwxNzYwODgyMTk2LC01Nj
UzMzEzMjMsLTk1ODczMjAwNiwtMTMwNjYyNTkxNCwxMDQ4ODMw
Mjc1LC0zNzQzMTAyNTEsLTExMDI0NDIxMzgsMTgzNzIxNjE4Ny
wtMTQ0OTMwMDA1OSwxODQxODYxMTUwLC03OTIxNTk1MjIsMTcz
NzgwMDM4MSwxNzkyOTc3MTA1LDE5ODU4ODcyMCw3MzExMTY2MD
ksNjc0ODMxMjYwLC00MTM3MTk1MjIsMTI5NDc2NjM1MywtNjc5
NDM3NTA4XX0=
-->