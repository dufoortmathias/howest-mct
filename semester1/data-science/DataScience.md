*Auteur: Tuur Vanhoutte*
# Hoofdstuk 1: Getalformaten

## Begrippen

|Woord|Definitie|
|--|--|
|Getal|Een vaste waarde|
|Geheel getal|Een waardie die voortkomt uit een telling|
|Fractie|Een waarde tussen 0 en 1 die voortkomt uit een meting/berekening|
|Vlottende komma|Het scheidingsteken tussen het geheel en fractioneel deel van een getal|
|Toestandsteken|Het minteken (-) voor getallen kleiner dan 0 en het plusteken (+) voor getallen groter of gelijk aan 0|
|Reëel getal|Getal dat bestaat uit een toestandsteken, een geheel deel, een vlottende komma en een fractioneel deel|
|Additief talstelsel|Een additief genoteerd getal is gedefinieerd als een waarde die wordt uitgedrukt door het bijeentellen van absolute symbolen. Bv: Romeinse getallen|
|Positiestelsels|Talstelsel waarin een getal voorgesteld wordt door een rij symbolen, meestal cijfers, waarvan de positie op basis van een gekozen grondtal de bijdrage aan het getal bepaalt. Notatie: (cijferpatroon)$_B$, met $B$ het aantal mogelijke cijfersymbolen gelijk aan de getalbasis $B$|
|Wetenschappelijke notatie|getal = toestandsteken x mantisse x (getalbasis)$^{exponent}$|
|mantisse|Een waarde tussen 1 en de vaste getalbasis $B$|

## Tweedelige getallen

|||
|--|--|
|Binair getal|Een waarde die uitgedrukt wordt in het positiesysteem met vaste getalbasis 2|
|bit|'binary digit'. Altijd afgekort met kleine letter 'b'|
|Most significant bit|De bit helemaal vooraan (msb)|
|Least significant bit|De meest rechtse bit (lsb)|
|Bitrijen|Informatie in computers (geluidsamples, pixels, letters, ...) worden door bitrijen voorgesteld. Weergegeven met suffix 'b': (10110010)$_b$
|byte|Bitrij bestaande uit 8bit|
|nibble|Bitrij bestaande uit 4bit|

### Binair optellen
Zoals de decimale optelling met een overdrachtcijfer/overdrachtbit naar de volgende positie waar nodig.

### Binair vermenigvuldigen
Zoals de decimale vermenigvuldiging van twee getallen via het optellen van deelproducten.

### Binair verdubbelen
* Door de komma 1 positie naar rechts op te schuiven
* Door de bitsequentie met 1 positie naar links te verschuiven

*Voorbeelden:*
$01 \Rightarrow 10$
$0101 \Rightarrow 1010$
$1,1100110 \Rightarrow 11,100110$
Viervoud (2 posities opschuiven):
$1,1100110 \Rightarrow 111,00110$
Achtvoud (3 posities opschuiven):
$1,1100110 \Rightarrow 1110,011000010110110$

## Achtdelige getallen
Octaal getal = Waarde uitgedrukt in het positiesysteem met vaste getalbasis 8.

*Voorbeeld:*
$(123.05)_8 = 1\cdot8^2 +2\cdot8^1 + 3\cdot8^0+0\cdot8^{-1}+5\cdot8^{-2}$
$=1\cdot64+2\cdot8+3\cdot1+0\cdot\frac{1}{8}+5\cdot\frac{1}{64}$
$=83,078125$

## Zestiendelige getallen
Hexadecimaal getal = Waarde uitgedrukt in het positiesysteem met vaste getalbasis 16.
$\Rightarrow \{0,1,2,3,4,5,6,7,8,9,A,B,C,D,E,F\}$

*Voorbeeld:*
$(5AE,4D)_{16} = 5\cdot16^2+A\cdot16^1+E\cdot16^0+4\cdot16^{-1}+D\cdot16^{-2}$
$= 5\cdot 256+10\cdot16+14\cdot1+4\cdot\frac{1}{16}+13\cdot\frac{1}{256}$


## Converteren naar decimaal
#### Binair naar decimaal
Elke bit is een macht van 2 $\Rightarrow$ alle machten optellen
#### Octaal naar decimaal
Elk octet is een macht van 8 $\Rightarrow$ alle machten optellen
#### Hexadecimaal naar decimaal
Elk hextet is een macht van 16 $\Rightarrow$ alle machten optellen


## Converteren naar binair
#### Decimaal naar binair
1) De grootste macht van 2 zoeken die kleiner is dan het te converteren decimaal getal
2) Verschil nemen van deze macht van 2 en het decimaal getal
3) Zoek opnieuw de grootste macht van 2 kleiner dan het verschilgetal. Herhaal tot verschil == 0
####  Octaal naar binair
Elke octale bit converteren naar een equivalente 3bit-representatie
*Voorbeeld:*
$7 \Rightarrow 111$
$0 \Rightarrow 000$
$5 \Rightarrow 101$
$1 \Rightarrow 001$

$(7051)_8 = (111000101001)_2$
#### Hexadecimaal naar binair
Idem als octaal, maar dan met 4bit-representatie.

## Converteren naar octaal
#### Decimaal naar octaal
* Het geheel deel:
	* Delen door 8
	* Hou telkens de rest na deling bij.
* Het fractioneel deel:
	* Vermenigvuldig met 8
	* Strip telkens het gehele deel van het product
	* Herhaal tot de fractie 0 wordt of een (niet) repeterend karakter vertoond

*Voorbeeld:* $(175,62)_{10} = (?)_8$
* Het gehele deel: $(175)_{10}$

|Deeltal/deler|quotiënt|rest|
|--|--|--|
|$\frac{175}{8}$|$21$|$7$|
|$\frac{21}{8}$|$2$|$5$|
|$\frac{2}{8}$|$0$|$2$|

* Het fractioneel deel (FD): $(0,62)_{10}$

|FD $\cdot$ 8|product|geheel cijfer|Nieuw DF|
|--|--|--|--|
|$0,62\cdot8$|$4,69$|$\bold4$|$0,96$|
|$0,96\cdot8$|$7,68$|$\bold7$|$0,68$|
|$0,62\cdot8$|$5,44$|$\bold5$|$0,44$|
|$0,44\cdot8$|$3,52$|$\bold3$|$0,52$|
|$0,52\cdot8$|$4,16$|$\bold4$|$0,16$|
|$...$|$...$|$...$|$...$|

$(175,62)_{10}=(257,47534...)_8$

#### Binair naar octaal
* Groepeer bits per 3 startende van rechts
* Converteer naar octale getallen

*Voorbeeld:* $(1011010111)_2 = (?)_8$

$1 \Rightarrow 1$
$011 \Rightarrow 3$
$010 \Rightarrow 2$
$111 \Rightarrow 7$

$(1011010111)_2=(1327)_8$

#### Hexadecimaal naar octaal
* Gebruik de binaire voorstelling als tussenstap
* Hexadecimaal $\Rightarrow$ binair $\Rightarrow$ octaal

*Voorbeeld:* $(1F0C)_{16}=(?)_8$
* Hexadecimaal $\Rightarrow$ binair:

$1 \Rightarrow 0001$
$F \Rightarrow 1111$
$0 \Rightarrow 0000$
$C \Rightarrow 1100$

* Binair $\Rightarrow$ octaal:

$0 \Rightarrow 0$
$001 \Rightarrow 1$
$111 \Rightarrow 7$
$100 \Rightarrow 4$
$001 \Rightarrow 1$
$100 \Rightarrow 4$

$(1F0C)_{16} = (17414)_8$


## Converteren naar hexadecimaal

#### Decimaal naar hexadecimaal
Idem als 'decimaal naar octaal', maar dan met 16 ipv 8.

#### Binair naar hexadecimaal
* Groepeer bits per 4 (want $2^4=16$) startende van rechts
* Converteer naar hexadecimale getallen

*Voorbeeld:* $(10101101000101)_2=(?)_{16}$

$10 \Rightarrow 2$
$1011 \Rightarrow B$
$0100 \Rightarrow 4$
$0101 \Rightarrow 5$

$(10101101000101)_2=(2B45)_{16}$

#### Octaal naar hexadecimaal
* Octaal $\Rightarrow$ binair $\Rightarrow$ hexadecimaal
* Zelfde manier als Hexadecimaal naar octaal, maar dan omgekeerd

## Getallen in computers

|Woord|Definitie|
|--|--|
|Unsigned integer|Datatype die natuurlijke getallen vasthoudt|
|Getalbreedte|De door de computer benutte aantal bits voor een getal.|
|Unsigned byte |1 byte: $2^8 = 256$ natuurlijke getallen|
|Unsigned int|2 bytes: $2^{16} = 65536$ natuurlijke getallen|
|Unsigned long|4 bytes: $2^{32} = 4.294.967.296$ natuurlijke getallen|
|Overflowbit|Bij rekenen met binaire getallen kan het zijn dat de breedte van de uitkomst breder is dan de oorspronkelijke getalbreedte: computer kan deze overflowbits niet stockeren $\Rightarrow$ verkeerde uitkomst|


## Getalopslag van gehele getallen
Hoe negatieve getallen opslaan? 3 mogelijkheden:
* Magnitude-voorstelling (sign and magnitude)
* 1-komplement
* 2-komplement

### Magnitudevoorstelling
= getalopslag waarbij we teken voor de getalgrootte zetten. 
Uiterst linkse bit = tekenbit (1 == negatieve waarde). 
Rest van de bits = magnitude (absolute getalwaarde)

*Voorbeeld:*
$-20_{dec}=(10010100)_{m/8bit}$

|decimale waarde|'signed nibble'|decimale waarde|'signed nibble'|
|--|--|--|--|
|+0|0000|-0|1000|
|+1|0001|-1|1001|
|+2|0010|-2|1010|
|+3|0011|-3|1011|
|+4|0100|-4|1100|
|+5|0101|-5|1101|
|+6|0110|-6|1110|
|+7|0111|-7|1111|

**Probleem: 0 komt twee keer voor**
* Moeilijk in hardware te implementeren
* Problemen bij elementaire binaire operaties


### 1-komplement
= Inverteer elke bitwaarde in het bitpatroon

*Voorbeeld:*
$(+20_{dec})=(00010100)_{8bit} \Rightarrow (-20_{dec})=(11101011)_{1k/8bit}$

|decimale waarde|'nibble'|decimale waarde|'1-komplement'|
|--|--|--|--|
|+0|0000|-0|1111|
|+1|0001|-1|1110|
|+2|0010|-2|1101|
|+3|0011|-3|1100|
|+4|0100|-4|1011|
|+5|0101|-5|1010|
|+6|0110|-6|1001|
|+7|0111|-7|1000|

**Probleem: 0 komt twee keer voor**
* Som en verschil werken zolang geen overflow

### 2-komplement
* Neem het 1-komplement
* Verhoog het 1-komplement met 1

*Voorbeeld:*
$(+20_{dec})=(00010100)_{8bit} \Rightarrow (-20_{dec})=(11101011)_{1k/8bit}$
$(+20_{dec})=(00010100)_{8bit} \Rightarrow (-20_{dec})=(11101\bold{100})_{2k/8bit}$

|decimale waarde|'nibble'|decimale waarde|'2-komplement'|
|--|--|--|--|
|+0|0000|-0|0000|
|+1|0001|-1|1111|
|+2|0010|-2|1110|
|+3|0011|-3|1101|
|+4|0100|-4|1100|
|+5|0101|-5|1011|
|+6|0110|-6|1010|
|+7|0111|-7|1001|
|+8|1000|-8|1000|

* 0 komt nu maar 1x voor
* 'signed nibble' $= \{\bold{-8}, -7,-6,-5,-4,-3-2,-1,0,+1,+2,+3,+4,+5,+6,+7\}_{dec}$
* Som en verschil werken zolang geen overflow

## Getalopslag van Reele getallen
* Je kan geen komma zelf opslaan in de computer
* Geen enkele methode kan getallen opslaan met een oneindige nauwkeurigheid
* Nodig om getalbenadering op te slaan
	* **Fixed point** getalpresentatie = vaste komma
	* **Floating piont** getalrepresentatie = vlottende komma
	* Rationele getalsystemen = gebruik verhoudingen van gehele getallen
	* Logaritmische getalsystemen

### Fixed point getalrepresentatie
* Vast aantal bits voor het geheel getaldeel (links van de komma)
* Vast aantal bits voor het fractioneel getaldeel (rechts van de komma)

### Floating point getalrepresentatie
Hoe het geheel en fractioneel deel representeren met een zo hoog mogelijke nauwkeurigheid?

*Voorbeeld:*
$13,9$ in een 8bit floating representatie

Algemene 8bit floating point representatie:
|7|6|5\|4\|3|2\|1\|0|
|--|--|--|--|--|--|--|--|
|Teken van getal|Teken van exponent|3 bits voor exponent|3 bits voor mantisse


$(13)_{10} = (1101)_2$ en $(0,9)_{10}\approx(0,11100)_2$
$(-13,9)_{10}=-(1101,11100)_2$
Komma verschuiven tot er exact 1 bit met waarde 1 links van de komma staat
$(-13,9)_{10}=-(1,10111100)_2\cdot2^3$
We hebben maar 3 plaatsen voor de mantisse:  $(-13,9)_{10}=-(1,101)_2\cdot2^3$
3 bits voor de exponent: $(3)_{10} = (11)_2=(011)_2$
$(-13,9)_{10}\approx-(1,101)_2\cdot2^{(011)_2}$

* 32 bit single precision floating point:
	* aantal bytes: 4
	* Normalisatie van de exponent:
		* exponent bias = $(127)_{10}$
		* gestockeerde exponent = werkelijke exponent + $(127)_{10}$
	* Absolute grenzen: $[5,877472\cdot10^{-39}; 6,805647\cdot10^{+38}]$
	* Aantal mogelijke getalwaarden : 4 miljard
* 64bit double precision floating point:
	* aantal bytes: 8
	* Normalistatie van de exponent:
		* exponent bias = $1023^{10}$
		* gestockeerde exponent = werkelijke exponent + $1023^{10}$
	* Absolute grenzen: $[2,23\cdot10^{-308}; 1,79\cdot10^{+308}]$
	* Aantal mogelijke getalwaarden: 16 triljoen

## Endianness
Heeft te maken met de volgorde waarmee bytes in het geheugen van de computer worden opgeslagen.
2 verschillende methodes:
* Little endian: de minst significante byte wordt eerst in het geheugen geplaatst
* Big endian: de meest significante byte wordt eerst in het geheugen geplaatst

*Voorbeeld:*
| Adres in computergeheugen | Big Endian | Little Endian |
|---------------------------|------------|---------------|
| 0 | 2D | 07 |
| 1 | EF | FF |
| 2 | 5A | 71 |
| 3 | 71 | 5A |
| 4 | FF | EF |
| 5 | 07 | 2D |

# Hoofdstuk 2: Centrummaten
## Soorten statistiek
* Beschrijvende statistiek

Gebruikt **numerieke en grafische** methoden om **patronen in een gegevensverzameling** te ontdekken, om de informatie in een gegevensverzameling **samen te vatten** en om deze informatie op een overzichtelijke manier te **presenteren**.

* Verklarende statistiek

De verklarende statistiek gebruikt **steekproefgegevens** voor het **schatten**, het **nemen van beslissingen** en het **voorspellen**. Wordt ook wel **inductieve statistiek** of **inferentiële statistiek** genoemd.

|Woord|Definitie|
|--|--|
|Experimentele eenheid|Een object (persoon/ding/transactie/gebeurtenis/...) waarvan we gegevens vastleggen|
|Populatie|Een verzameling eenhden (personen/dingen/transacties/gebeurtenissen/...) die we willen bestuderen. **Vbdn:** inwoners van Europa, personen besmet met Zika, vliegtuigen van Airbus|
|||
|Variabele|Kenmerk of eigenschap van een eenheid uit een populatie. **Vbdn:** Leeftijd, geslacht, inkomen, levensduur, beoordelingsscore, temperatuur, luchtvochtigheid, druk,...|
|Meten|Proces waarbij getallen toegekend worden aan variabelen|
|Census|Als we een variabele meten voor iedere eenheid van de populatie, is het resultaat een census van de populatie|
|Steekproef|Een deelverzameling van de eenheden van een populatie (sample). De steekproef moet representatief zijn voor de volledige populatie|
|Statistische conclusie|Een schatting, een voorspelling of een andere generalisatie die gebaseerd is op informatie uit een steekproef|
|Betrouwbaarheidsmaat|Kwantitatieve uitspraak over de mate van onzekerheid die gepaard gaat met een statistische conclusie. **Vbdn:** Hoe goed voorspelt een verkiezingspeiling de uiteindelijke uitslag? Met welke zekerheid valt te zeggen dat een dierenpopulatie met 10% is gestegen?...|

### Vier elementen van de beschrijvende statistiek
1. De populatie (of steekproef)
2. Een of meerdere variabelen
3. Tabellen, grafieken, numerieke hulpmiddelen om een samenvatting te geven
4. Vermeldingen van patronen die in de samenvattingen naar voren komen

### Vijf elementen van de verklarende statistiek
1. De populatie
2. Een of meerdere variabelen
3. De steekproef
4. De conclusie over de populatie, gebaseerd op informatie in de steekproef
5. Een betrouwbaarheidsmaat voor de conclusie



## Kwantitatieve gegevens
= meetwaarden die worden geregistreerd op een van nature voorkomen numerieke schaal
= numerieke gegevens

**2 soorten:**
1. Discrete gegevens
2. Continue gegevens

*Voorbeelden:*
* Het inkomen van 100 willekeurige geselecteerde Vlamingen
* Een 2000-tal metingen van de bloeddruk bij hartpatiënten
* De dagelijkse hoeveelheid elektriciteit geproduceerd door een PV installatie op het dak van een nieuwbouwwoning in Kortrijk tijdens het jaar 2018

#### Discrete gegevens
= gegevens waarbij de variabele een eindig aantal verschillende waarden aan kan nemen. Komen meestal tot stand door een *telling*.

*Voorbeelden:*
* Leeftijd van een persoon
* Examenscores op 20
* Het aantal passagiers op een vliegtuig
* Het aantal klachten bij een telecomoperator

#### Continue gegevens
= gegevens waarbij de variabele een oneindig aantal verschillende waarden kan aannemen. Komen meestal tot stand door een *meting*.

*Voorbeelden:*
* lengte
* breedte
* grootte
* tijd
* temperatuur
* kosten

## Kwalitatieve gegevens
= metingen die niet op een natuurlijk voorkomende numerieke schaal kunnen worden gemeten; ze kunnen alleen worden ingedeeld in categorieën. Ze worden ook **categorische gegevens** genoemd.

*Voorbeelden:*
* Maanden van het jaar
* Beoordeling van een film met slecht -- matig -- goed -- uitstekend
* Het geslacht M/V/X
* Een lijst van kleuren

### Nominale gegevens
= gegevens waarbinnen er verschillende categorieën aan te duiden vallen, maar er zijn geen rangordelijke verschillen tussen deze categorieën.

*Voorbeelden:*
* Geslacht M/V/X
* Provincies
* Automerken
* Lijst van ingrediënten

### Ordinale gegevens
= gegevens die categorieën bevatten die te rangschikken zijn. 

*Voorbeelden:*
* eens -- neutraal -- oneens
* goud -- zilver -- brons
* koud -- loauw -- warm -- heet
* slecht -- matig -- goed -- uitstekend

![enter image description here](https://i.imgur.com/vbcOSMF.png)
![enter image description here](https://i.imgur.com/41mm9ds.png)

## Kwalitatieve gegevens voorstellen en ordenen
|Woord|Definitie|
|--|--|
|Klasse|Eén van de categorieën waarin kwalitatieve gegevens kunnen worden ingedeeld
|Absolute frequentie per klasse|Aantal waarnemingen in de gegevensverzameling die tot een bepaalde klasse behoren|
|Relatieve frequentie per klasse|De frequentie per klasse gedeeld door het aantal waarnemingen in de gegevensverzamelingen|

## Continue gegevens voorstellen en ordenen

### Stengel-blad diagram
* In de stengel staat het eerste (meest beduidende) deel van het getal
* In het blad staat het laatste deel van het getal
* Per blad staan de getallen van klein naar groot gerangschikt

*Voorbeeld:*
* Stengel: tientallen
* Bladeren: eenheden

![enter image description here](https://i.imgur.com/idFVKT0.png)

### Groeperen van gegevens in klassen
|Woord|Definitie|
|--|--|
|Klasse|Verzameling van alle waarden die een variabele grootheid kan aannemen, liggend tussen de twee opeenvolgende klassegrenzen|
|Klasse-interval|De grootte van een klasse|

Notatie klasseinterval: [ondergrens; bovengrens[
Klassebreedte = bovengrens - ondergrens
Bepalen klassebreedte: $C=\mid\frac{max - min}{\sqrt{N}}\mid$ met zelfde nauwkeurigheid als meetwaarden

### Cumulatieve absolute frequentie $N_i$
= Het aantal waarnemingen die kleiner of gelijk aan zijn aan het eindpunt van de $i^{de}$ klasse
$N_i =\sum n_j$
$N_k = N$

### Cumulatieve relatieve frequentie $F_i$
= Verhouding van de cumulatieve absolute frequentie tov het aantal waarnemingen
$F_i =\sum_{j\leq i} f_j = \frac{N_i}{N}$
$F_k = 1 = 100\%$

### Cumulatief frequentiepolygoon
= Grafische voorstelling van de cumulatieve absolute (of relatieve) frequentie
* Punten in de grafiek zetten bij de klassebovengrens
* Eerste punt is de ondergrens van de eerste klasse
* Het cumulatief frequentiepolygoon kan nooit dalen

![enter image description here](https://i.imgur.com/nDAHMbq.png)


## Centrummaten
Centrum = de neiging van de gegevens om zich rond een bepaalde waarde te concentreren
De verschillende centrummaten:
* Gemiddelde
* Modus
* Mediaan

|Maat|Steekproef|Populatie|
|--|--|--|
|Gemiddelde|$\overline{x}$|$\mu$|
|Grootte|n|N|


### Gemiddelde $\ \overline{x}$
= de som van de meetwaarden gedeeld door het aantal meetwaarden in de gegevensverzameling

$\overline{x}=\frac{\sum_{i=1}^nx_i}{n}$

* Meest gebruikte grootheid om het centrum uit te drukken
* Wordt beinvloed door extreme waarden (uitschieters)
* Kan als een evenwichtspunt worden gezien
* Engels: mean/average

#### Gemiddelde als evenwichtspunt
Zoek $m$ zodat de fout $e=\sum_{i=1}^n(x_i-m)^2$ geminimaliseerd wordt
* We gaan op zoek naar de waarde voor $m$ waarbij het totale verschil tussen $m$ en elke meetwaarde zo klein mogelijk is.
* $e$ is minimaal wanneer $m = \overline{x}$
* $e$ wordt de **squared error** genoemd

#### Gemiddelde van continue gegevens
* Data is gegroepeerd in klassen
	* Exacte waarde is verloren
	* Veronderstelling dat alle waarden in de klasse deze van het klassengemiddelde aannemen

Bepalen van het klassenmidden $m_i$
$m_i = \frac{ondergrens + bovengrens}{2}$

### Modus
= de meest voorkomende waarde
Eigenschappen:
* Is een maat voor de centrale tendens
* Modus wordt niet beinvloed door extreme waarden
* Het kan dat er geen modus bestaat (elke waarde uniek) of dat er verschillende modi (sommige waarden komen evenveel voor) zijn.
* Kan voor zowel kwalitatieve als kwantitatieve data gebruikt worden
* Engels: mode

#### Modus van gegroepeerde gegevens
$x_{mo} = L + \frac{n_i - n_1}{(n_i - n_1) + (n_i - n_2)}\cdot C$
met
$n_i =$ abs. freq. van de modale klasse
$n_1 =$ abs. freq. van de vorige klasse
$n_2=$ abs.freq. van de volgende klasse
$C=$ klassenbreedte
$L =$ benedengrens v.d. modale klasse

### Mediaan
= middelste waarde van een geordende rij waarden
Eigenschappen:
* Is een maat voor de *centrale tendens*
* Als n oneven is, de middelste waarde van de rij
* Als n even is, het gemiddelde van de 2 middelste waarden
* De positie van de mediaan in een rij = $\frac{n+1}{2}$
* Engels: median

$x_{me}=L + (pN - N_L)\cdot\frac{C}{n_j}$
met
$L =$ benedengrens v.d. mediale klasse
$p=0.5$
$N_L=$ cumulatieve frequentie tot benedengrens
$n_j=$ abs.frequentie mediale klasse
$C=$ klassenbreedte
$N=$ totaal aantal waarnemingen

||gemiddelde|mediaan|modus|
|--|--|--|--|
|nominaal|||x|
|ordinaal||x|x|
|discreet|x|x|x|
|continu|x|x|x|

# Hoofdstuk 3: Spreidingsmaten
= om duidelijker een reeks gegevens te kunnen beschrijven, centrummaten volstaan niet altijd.

Gebruikte spreidingsmaten
* Range = variatiebreedte = bereik
* Interkwartielafstand (IQR = interquartile range)
* Variantie (variance)
* Standaardafwijking (standard deviation)

## Range
= variatiebreedte 
= bereik
= de grootste meetwaarde -- de kleinste meetwaarde

* Gevoelig voor uitschieters
* Zegt niets over de verdeling van de gegevens tussen het minimum en het maximum
* Variantie, standaardafwijking en de interkwartielafstand zijn doorgaans betrouwbaarder

## Kwartielen
* Splitst geordende data in 4 delen:
	* Q1 = $25^{ste}$ percentiel
	* Q2 = $50^{ste}$ percentiel = **mediaan**
	* Q3 = $75^{ste}$ percentiel
* Interkwartielafstand $= Q3 - Q1$

### Boxplot
= Grafische voorstelling van de spreiding van de data op basis van 5 kerngetallen:
minimum, maximum, mediaan, Q1 en Q3

![enter image description here](https://i.imgur.com/gIVfnYF.png)

### Uitschieters
= waarden die kleiner zijn dan $Q1 - (1.5\cdot IQR)$ of groter dan $Q3 + (1.5\cdot IQR)$
Staarten van de boxplot aanpassen zodat elke staart maximaal $1.5\cdot IQR$ bedraagt.

## Variantie en afwijking
### Steekproefvariantie $s^2$
= de som van de gekwadrateerde afwijkingen van het gemiddelde, gedeeld door $(n-1)$, met $n=$ aantal meetwaarden.

$s^2=\frac{\sum_{i=1}^n(x_i-\overline{x})^2}{n-1}$



### Populatievariantie $\sigma^2$
= de som van de gekwadrateerde afwijkingen van het gemiddelde, gedeeld door $N$, met $N=$ het aantal meetwaarden.

$\sigma^2=\frac{\sum_{i=1}^N(x_i-\overline{x})^2}{N}$


### Algemene eigenschappen van de variantie
* Variantie is een maat voor de onzekerheid. Hoe groter de variantie, des te moeilijker een waarde te voorspellen valt.
* Variantie wordt gebruikt om de hoeveelheid ruis (fouten) op een signaal uit te drukken.

### Standaardafwijking $s$ van een steekproef
$s=\sqrt{s^2}$

### Standaardafwijking $\sigma$ van een populatie
$\sigma=\sqrt{\sigma^2}$

### Symbolen voor variantie en standaardafwijking
* $s^2=$ variantie van de steekproef
* $s=$ standaardafwijking van de steekproef
* $\sigma^2=$ variantie van de populatie
* $\sigma=$ standaardafwijking van de populatie

## Spreidingsmaten vergelijken

|Spreidingsmaat|Eigenschappen|
|--|--|
|Range|<ul><li>Zeer weinig rekenwerk</li><li>Vertegenwoordigt slechts 2 gegevens: de uitersten</li><li>Zeer gevoelig voor uitschieters</li></ul>|
|Interkwartielafstand (IQR)|<ul><li>Relatief weinig rekenwerk</li><li>Geeft enkel de spreiding van de middelste groep gegevens</li><li>Niet gevoelig voor uitschieters</li></ul>|
|Variantie/standaardafwijking|<ul><li>Veel rekenwerk</li><li>Vertegenwoordigt alle gegevens</li><li>Enkel gevoelig voor uitschieters bij kleine $n$ of $N$ (aantal samples/grootte van de populatie)</li></ul>|


### Variatiecoefficiënt $V$
= dimentieloos getal dat uitdrukt hoe een standaardafwijking zich verhoudt tot het gemiddelde. Is een maat voor de relatieve spreiding.

$V=\frac{s}{\overline{x}}$

Wordt $V$ uitgedrukt in procenten, dan:
* $V < 5\% \rightarrow$ zeer kleine spreiding
* $5\%<V<10\% \rightarrow$ kleine spreiding
* $V>50\% \rightarrow$ zeer grote spreiding

Nut: verschillende populaties of steekproeven met elkaar vergelijken die (sterk) uiteenlopende gemiddelden hebben.

## Theorema van Chebyshev
Toepasbaar op elke kansverdeling of histogram en zegt dat niet meer dan $\frac{1}{k^2}$ van de waarden van een kansverdeling niet verder dan $k$ standaardafwijkingen verwijderd liggen van het gemiddelde.

$P(|x-\mu|\geq ks) \leq \frac{1}{k^2}$
* Geen bruikbare informatie over de fractie data gelegen binnen het interval $\overline{x} - s$ tot $\overline{x} + s$
* Minstens $50\%$ van de data ligt binnen het interval $\overline{x} - \sqrt2\cdot s$ tot $\overline{x} + \sqrt2\cdot s$
* Minstens $75\%$ van de data ligt binnen het interval $\overline{x} - 2\cdot s$ tot $\overline{x} + 2\cdot s$
* Minstens $88.89\%$ van de data ligt binnen het interval $\overline{x} - 3\cdot s$ tot $\overline{x} + 3\cdot s$


## Symmetrische heuvelvormige verdelingen
* $\approx68\%$ van de waarden liggen in het interval $\overline{x} - s$ tot $\overline{x} + s$ bij steekproeven en $\overline\mu - \sigma$ tot $\overline\mu + \sigma$ bij populaties
* $\approx95\%$ van de waarden liggen in het interval $\overline{x} - 2\cdot s$ tot $\overline{x} + 2\cdot s$ bij steekproeven en $\overline\mu - 2\cdot \sigma$ tot $\overline\mu + 2\cdot \sigma$ bij populaties
* $\approx99.7\%$ van de waarden liggen in het interval $\overline{x} - 3\cdot s$ tot $\overline{x} + 3\cdot s$ bij steekproeven en $\overline\mu - 3\cdot \sigma$ tot $\overline\mu + 3\cdot \sigma$ bij populaties


![enter image description here](https://i.imgur.com/Nj5WIcT.png)


## Relatieve maten
### Hoe sterk wijkt een waarneming af van de overige waarnemingen?
* Beschrijven de relatieve positie van een meting ten opzichte van de rest van de data
* Twee veelgebruikte maten zijn:
	* Percentiel
	* z-score
* Laten toe om uitschieters op te sporen

### Percentiel
Voor een verzameling van $n$ meetwaarden (gesorteerd in toenemende volgorde), is het $p^e$ percentiel een getal zodat $p\%$ van de meetwaarden onder het $p^e$ percentiel valt, en $(100 - p)\%$ erboven valt. Is een cumulatieve proportie.

* Q1 is het $25^{ste}$ percentiel
* Mediaan is het $50^{ste}$ percentiel
* Q3 is het $75^{ste}$ percentiel

### z-score
Populaire maat om de relatieve positie van een waarde t.o.v. de rest van de data uit te drukken. De z-score vertegenwoordigt de afstand tussen een gegeven meetwaarde $x$ en het gemiddelde, uitgedrukt in standaardafwijkingen. 

* De z-score van een steekproef is

$z=\frac{x-\overline{x}}{s}$

* De z-score van een populatie is

$z=\frac{x-\mu}{\sigma}$

#### Eigenschappen van de z-score
* z-score is relatieve maat voor de meetwaarde
	* Grote positieve z-score $\Rightarrow$ meetwaarde is **groter** dan vrijwel alle andere meetwaarden
	* Grote negatieve z-score $\Rightarrow$ meetwaarde is **kleiner** dan vrijwel alle andere meetwaarden
	* z-score $\approx 0$, dan ligt de meetwaarde rond het gemiddelde van de steekproef of populatie.

#### z-scores voor heuvelvormige gegevensverdelingen
1. Ongeveer $68\%$ vd meetwaarden heeft een z-score tussen $-1$ en $+1$
2. Ongeveer $95\%$ vd meetwaarden heeft een z-score tussen $-2$ en $+2$
3. Ongeveer $99.7\%$ vd meetwaarden heeft een z-score tussen $-3$ en $+3$

#### Uitschieters detecteren via z-scores
* Observaties met een z-score groter dan $3$ in absolute waarde uitgedrukt.
* Bij erg scheve datasets, observaties met een z-score groter dan $2$ in absolute waarde uitgedrukt.

#### Uitschieters detecteren via boxplot
* Observaties die buiten de wimpels van de boxplot liggen. Dit is wanneer kleiner dan $Q1 - 1.5 \cdot IQR$ en groter dan $Q3 + 1.5\cdot IQR$

## Scheefheid

![enter image description here](https://i.imgur.com/9mdE4Vp.png)
### Invloed van Q1, Q3 en de mediaan op de scheefheid: Galton Skewness
$SK_B=\frac{Q3 + Q1 - 2\cdot Q2}{(Q3 - Q1)}$
* $SK_B = 0$: Symmetrisch
* $SK_B > 0$: Rechtsscheef
* $SK_B < 0$: Linksscheef

### Skew en SkewP

* Voor steekproeven:

Skew $=\frac{n}{(n-1)\cdot(n-2)}\cdot\sum_{i=1}^n(\frac{x_i-\overline{x}}s)^3$

* Voor populaties:

SkewP $=\frac{1}{n}\cdot\sum_{i=1}^n(\frac{x_i-\overline{x}}\sigma)^3$

* Skew $=0$: symmetrisch
* Skew $>0$: rechtscheef
* Skew $<0$: linksscheef
* $|$Skew$|$ $>1$: sterk scheef

## Kurtosis
= een maat voor de piekvormigheid van een verdeling

* Voor steekproeven:

$K=\frac{n(n+1)(n-1)}{(n-2)(n-3)}\cdot\frac{\sum_{i=1}^n(x_i-\overline{x})^4}{(\sum_{i=1}^n(x_i-\overline{x})^2)^2}$

* Voor populaties:

$K=n\cdot\frac{\sum_{i=1}^n(x_i-\overline{x})^4}{(\sum_{i=1}^n(x_i-\overline{x})^2)^2}$

---
* $K=3:$ Normale verdeling (mesokurtic)
* $K>3:$ Scherpere piek (leptokurtic)
* $K<3:$ Stompere, bredere piek (platykurtic)

### Excess Kurtosis
$=K_e=$ een maat voor de piekvormigheid met als referentie de normaalverdeling.
$K_e=K- 3$.
Wordt door excel toegepast in de functie $\text{KURT()}$

* $K_e=0:$ Normale verdeling (mesokurtic)
* $K_e\gt0:$ Scherpere piek (leptokurtic)
* $K_e\lt0:$ Stompere, bredere piek (platykurtic)

## Lineaire transformatie van gegevens
*Niet expliciet te kennen voor examen, maar wel inzichtsvragen erover*

Lineaire transformatie = Bewerking waarbij elke waarde x herrekend wordt naar y volgens
$y=ax+b$

Alle waarden worden dus met een bepaald getal $a$ vermenigvuldigd waarna een constante waarde $b$ wordt opgeteld. 
Bewerkingen met vierkantswortels, kwadraten of hogere machten, logaritmes, enz. zijn geen lineaire transformations.

Toepassingen:
* Veranderen van eenheid
* Standaardiseren (bijvoorbeeld de z-score)

### Effect op het rekenkundig gemiddelde
De lineaire transformatie $y=ax+b$ zal het gemiddelde $\overline{x}$ omvormen tot: $\overline y = a\overline x + b$

### Effect op de variantie $s^2$ en de standaardafwijking $s$
De lineaire transformatie $y=ax+b$ zal het gemiddelde $s^2_x$ en de $s$ omvormen tot: 
$s^2_y=a^2s^2_x$
$s_y=|a|s_x$

## Overzicht kerngetallen
* Verwachtingswaarden
	* Engels: mean / expected value
	* Symbool: $\mu$ of $E(X)$
* Variantie
	* Engels: variance
	* Symbool: $\sigma^2$
* Standaardafwijking
	* Engels: standard deviation
	* Symbool: $\sigma$

# Hoofdstuk 4: Discrete Kansverdelingen
## Stochastische variabelen
= kansvariabele
= een variabele die numerieke waarden aanneemt die horen bij de uitkomsten van een toevalsexperiment, waarbij precies één waarde aan elke uitkomst wordt toegekend.
* Stochastisch = van het toeval afhankelijk
* Engels: stochastic/random variable

*Voorbeeld:*
Een experiment bestaat uit het tellen van het aantal klanten dat op een bepaalde dag gebruik maakt van de geldautomaat van een bank.
* **Stochastische variabele**: aantal klanten die dag
* **Uitkomst** van de stochastische variabele: het numeriek aantal klanten op die dag
* **Mogelijke uitkomsten** (waarden) van de stochastische variabele: lopen van 0 tot het maximum aantal klanten dat op een dag van de geldautomaat gebruik zou maken.

### Discrete stochastische variabele
Wanneer een stochastisch variabele een telbaar (eindig of oneindig) aantal waarden aan kan nemen
*Voorbeelden:*
|Experiment|Stochastische variabele|Mogelijke uitkomsten|
|--|--|--|
|100 verkoopspogingen|aantal verkopen|$0,1,2,...,100$|
|Inspectie van 70 auto's|aantal afgekeurd|$0,1,2,...,70$|
|Telling aantal bezoekers museum|aantal bezoekers|$0,1,2,...,\infty$|

### Continue stochastisch variabele
Wanneer een stochastisch variabele eender welke waarde binnen een bepaald interval kan aannemen.
*Voorbeelden:*
|Experiment|Stochastische variabele|Mogelijke uitkomsten|
|--|--|--|
|Weeg 100 mensen|gewicht|$45.1,78.6,89.4,...$|
|Tijd tussen aankomst van klanten|aantal minuten|$0.4,2.5,...,\infty$|

## Discrete kansverdeling
= een grafiek, tabel of formule die de kansen vastlegt die horen bij de mogelijke waarden die de stochastische variabele kan aannemen.
*Voorbeeld:*
Beschouw het experiment waarbij 2 munten worden opgeworpen. We zijn geintresseerd in het aantal keren 'kop'.
|Uitkomst|Waarde (x)|
|--|--|
||MM|0|
|KM|1|
|MK|1|
|KK|2|

$p(x=0) = p(MM)=\frac14$
$p(x=1)=p(MK)+p(KM)=\frac14 + \frac14 = \frac12$
$p(x=2)=p(KK)=\frac14$

![enter image description here](https://i.imgur.com/QKktOci.png)

#### Voorwaarden voor de kansverdeling van een discrete stochastische variabele x
1. $p(x)\geq0; \forall x$
2. $\sum p(x) = 1$

### Verwachtingswaarde/verwachting van een variabele x
$\mu = E(X) = \sum p(x)\cdot x$
$\mu$ valt te zien als de gemiddelde aarde van x bij een zeer groot aantal herhalingen van het experiment.
*Voorbeeld:*
Een verzekeringsmaatschappij verkoopt een levensverzekering van $€10.000$ met een looptijd van 1 jaar, voor een jaarpremie van $€290$. Onderstaande tabel geeft de kans weer dat een persoon (aan wie de verzekering wordt verkocht) al dan niet sterft binnen het komende jaar. Wat is de verwachte winst?

|Winst, x|Uitkomst|Kans|
|--|--|--|
|$€290$|Klant blijft leven|$0.999$|
|$€-9710$|Klant sterft|$0.001$|

$\mu = E(X) = \sum p(x)\cdot x$
$\mu = 290 \cdot 0.999 + (-9710)\cdot 0.001 = €280$

De verwachtingswaarde hoeft niet gelijk te zijn aan een mogelijke waarde van x. De verwachtingswaarde is $€280$, maar x zal gelijk zijn aan $€290$ of $-€9710$ elke keer het experiment uitgevoerd wordt. 

### Variantie en standaardafwijking
#### Variantie en std. afwijking van een discrete stochastische variabele x
$\sigma^2 = \text{var}(x) = E[(x-\mu)^2]=\sum(x-\mu)^2\cdot p(x)$
#### Standaardafwijking van een discrete stochastische variabele
$\sigma=\sqrt{\sigma^2}$

*Voorbeeld: kansspel met dobbelsteen*
Een kansspel met een dobbelsteen heeft volgende kansverdeling:

|Uitkomst, x|Waarde|Kans|
|:--:|:--:|:--:|
|$1$|$+€2$|$\frac16$|
|$2$|$-€1$|$\frac16$|
|$3$|$+€2$|$\frac16$|
|$4$|$-€1$|$\frac16$|
|$5$|$+€2$|$\frac16$|
|$6$|$-€3$|$\frac16$|

$\mu = E(X) = \sum x\cdot p(x)$
$\mu = 2\cdot \frac36 + (-1)\cdot \frac26 + (-3)\cdot \frac16 = \frac16 = €0.17$

$\sigma^2 = var(x) = E[(x-\mu)^2]=\sum(x-\mu)^2\cdot p(x)$
$\sigma^2 = (2-\frac16)^2\cdot \frac36 + (-1-\frac16)^2 \cdot \frac26 + (-3-\frac16)^2 \cdot \frac16$
$\sigma^2 = 3.81$

$\sigma = \sqrt{3.81} = 1.95$


## Binomiale verdeling
Eigenschappen
* Het experiment bestaat uit $n$ **identieke** deelexperimenten
* Er zijn slechts **2 mogelijke uitkomsten** voor elk deelexperiment. $S =$ succes, $M=$ mislukking.
* De kans $p$ op de uitkomst $S$ is voor ieder deelexperiment even groot. De kans op $M$ wordt aangeduid met $q$. 
* $q=1-p$.
* De deelexperimenten zijn **onafhankelijk**.
* De binomiale stochastische variabele $x$ is het aantal keren $S$ in $n$ deelexperimenten.

*Voorbeelden:*
* De kans dat er in een gezin van 5 kinderen 4 meisjes zijn.
* De kans dat er tussen 40 producten 3 defecte zijn
* De kans dat 4 van de 10 klanten die een winkel binnenkomt effectief iets koopt.
* De kans dat een student 2 van de 5 vierkeuzevragen correct beantwoordt als hij gokt.
* Het aantal patienten die goed reageren op een behandeling
* De kans dat er in een groep van 30 mannen er meer dan twee kleurenblind zijn. 

*Experimenten die niet binomiaal zijn:*
* De kans dat meer dan 20.000 mensen een nieuwe app zullen uitproberen.
* Een lottotrekking
* Een grabbelback bevat 5 blauwe en 7 rode ballen. Je wil de kans bepalen dat je 3 rode ballen na elkaar trekt, zonder teruglegging.

### Rekenen met de binomiale kansverdeling
$p(x)= \binom{n}{x}\cdot p^x\cdot q^{n-x}$

$p=$ kans op succes in één enkel deelexperiment
$q= 1 - p$
$n=$ aantal deelexperimenten
$x=$ aantal sucessen in $n$ deelexperimenten
$\binom{n}{x}=\frac{n!}{x!\cdot (n-x)!}$

*Voorbeeld:*
**Gegeven:** 
Een machine die stansstukken maakt voor automotoren functioneert niet goed en levert 10% defecte producten op. De volgorde waarin de defecte en gave stansstukken door de machine worden geproduceerd is willekeurig. 

**Gevraagd:**
Bepaal de kans dat van de 5 volgende stansstukken er 3 defect zijn.

**Oplossing:**
$x=$ aantal defecte stanstukken in $n=5$ deelexperimenten
$p=0.1$ en $q= 1 - p = 1 - 0.1 = 0.9$
$p(x)= \binom nx \cdot p^x \cdot q^{n-x} = \binom 5x \cdot 0.1^x \cdot 0.9^{5-x}$
Met $x = 3:$
$p(3)= \binom 53 \cdot (0.1)^3 \cdot (0.9)^{5-3}$
$p(3)= \frac{5!}{3!\cdot (5-3)!} \cdot (0.1)^3 \cdot (0.9)^{2}$
$=10 \cdot (0.1)^3 \cdot (0.9)^{2}$
$=0.0081=0.81\%$


### Verwachting en spreidingsmaten van de binomiale stochastische variabele
* Verwachting: $\mu = n\cdot p$
* Variantie: $\sigma^2 = n \cdot p \cdot q$
* Standaardafwijking: $\sigma = \sqrt{n\cdot p \cdot q}$

## De poissonverdeling
Eigenschappen
* Beschrijven van het **aantal gebeurtenissen in een bepaalde tijdsperiode**, oppervlak of in een bepaald volume (of gewicht, afstand of andere meeteenheid).
* De kans dat een gebeurtenis voorkomt in een bepaald tijdsinterval, oppervlak of volume is even groot voor alle tijdsintervallen, oppervlaktes en volumeeenheden van gelijke grootte.
* Deze gebeurtenissen zijn onafhankelijk van het aantal dat in andere disjuncte eenheden voorkomt.
* Het aantal gebeurtenissen in elke eenheid wordt aangegeven met $\lambda$

### Rekenen met de Poissonverdeling
$p(x) = \frac{\lambda^x\cdot e^{-\lambda}}{x!}$ met $x=\{0,1,2,...\}$
$p(x) =$ de kans dat x gebeurtenissen voorkomen in het tijdsinterval
$\mu =\lambda$
$\sigma^2 = \lambda \Leftrightarrow \sigma = \sqrt\lambda$
$\lambda =$ verwachte aantal gebeurtenissen in een bepaalde eenheid van de tijd, oppervlak, volume
$e = 2.71828... =$ constante van Euler.

*Voorbeeld*
**Gegeven:** 
Per maand gebeuren er in de luchtvaart gemiddeld $4.4$ ongelukken. Veronderstel dat de kansverdeling van het aantal ongelukken $x$ in een bepaalde maand kan worden benaderd door een Poissonverdeling.

**Gevraagd:**
1. Bepaal de verwachtingswaarde en standaardafwijking van $x$.
2. Hoe groot is de kans dat er geen enkel ongeluk gebeurt in een bepaalde maand?
3. Hoe groot is de kans dat er precies 1 ongeval gebeurt in een bepaalde maand?
4. Wat is de kans dat er meer dan 6 ongevallen gebeuren in een bepaalde maand?

**Oplossing:**
1. $\mu = \lambda = 4.4$, 
$\sigma^2=\lambda = 4.4$,
$\sigma = 2.1$

2. $p(x) = \frac{\lambda^x \cdot e^{-\lambda}}{x!} \Rightarrow p(0) = \frac{4.4^0 \cdot }{0!} = \frac{1 \cdot 0.0123}{1} = 0.0123 = 1.23\%$ 

3. $p(1) = \frac{4.4^1 \cdot e^{-4.4}}{1!} = \frac{4.4 \cdot e^{-4.4}}{1} = 0.054  = 5.4\%$ 

4. $p(x > 6) = 1 - p(x \leq 6) = 1 - 0.844 = 0.156 = 15.6\%$

# Hoofdstuk 5: Continue kansverdelingen
## De normale verdeling of Gaussiaanse verdeling
* **Symmetrisch** rond de verwachte waarde $\mu$
* Kansdichtheid is **klokvormig**
* De spreiding wordt bepaald door de standaardafwijking $\sigma$
## Kansverdeling voor een normaal verdeelde variabele
$f(x) = \frac{1}{\sigma\sqrt{2\pi}}\cdot e^{-\frac12\cdot(\frac{x-\mu}{\sigma})^2}$

* $\mu =$ verwachting van de normaal verdeelde variabele $x$
* $\sigma =$ standaardafwijking
* $e = 2.718$

## Herkennen van de normale verdeling
1. Histogram: klokvormig en symmetrisch?
2. Centrumwaarden: mediaan, modus en gemiddelde ongeveer gelijk?
3. Ongeveer 68% van de waarden binnen 1 standaardafwijking van het gemiddelde, en 95% binnen 2 standaardafwijkingen?

## De standaard normale verdeling
= een normale verdeling met $\mu = 0$ en $\sigma = 1$
Een stochastische variabele met het symbool $z$, wordt een standaardnormaal verdeelde variabele genoemd.

### Standaardiseren van een niet-standaardnormale verdeling.
Bij een normale verdeling waarbij $\mu \neq 0$ of $\sigma \neq 1$ moeten we standaardiseren via de z-score: $z=\frac{x-\mu}{\sigma}$
De z-score geeft het aantal standaardafwijking. Na standaardisatie gelden de rekenregels van standaard normale verdelingen. 

**Voorbeeld**:
Bepalen van $P(5 < x < 6.2)$ met $\mu = 5$ en $\sigma = 10$:
Standaardiseren van niet-standaard normale verdeling via z-score:
$z = \frac{x - \mu}{\sigma}$ 
$\Rightarrow z_1 = \frac{5-5}{10} = 0$
$\Rightarrow z_2 = \frac{6.2 - 5}{10} = 0.12$ 
$P(5 < x < 6.2) \Rightarrow P(0 < z < 0.12) = P(z < 0.12) - P (z < 0) = 4.77$% (via tabel)

# Hoofdstuk 6: Correlatie en lineaire regressie
## Doelstelling
* Puntenwolken
* Enkelvoudige lineaire regressie
* De covariantie
* De correlatiecoëffiënt

## Modellen
### Definitie
* Een (vereenvoudigde) beschrijving/voorstelling van een bepaald fenomeen
* Mathematische modellen beschrijven via een wiskundige uitdrukking dit fenomeen
* Heel dikwijls beschrijven ze het verband tussen variabelen

### Types
1. Deterministische modellen
2. Kansmodellen

## Deterministische modellen
* Veronderstelt een exacte relatie tussen de variabelen
	* Als er een deterministisch verband bestaat tussen x en y dan kan y altijd exact bepaald worden als de waarde van x bekend is.
	* We laten geen toevallige afwijkingen toe in het model

*Voorbeeld:* kracht is exact gelijk aan massa * versnelling ($F=m\cdot a$)

## Kansmodel
### Componenten
1. Deterministische componenten (deterministic component)
2. Toevallige afwijking (random error component)

De ene variabele kan niet exact uit de andere variabele voorspelt worden. 
*Voorbeeld:*
Het verkoopsvolume $y$ is 10 keer het bedrag dat aan marketing wordt besteed $x$ + een random error $ε$.
$y = 10\cdot x + ε$
De willekeurige afwijking $ε$ kan het gevolg zijn van andere factoren dan het bedrag dat aan marketing wordt besteed. 

### Algemene vorm van een kansmodel
$y =$ deterministische component $+$ toevallige afwijking
* $y=$ de variabele waarin we geintresseerd zijn
* We veronderstellen dat verwachtingswaarde van de toevallige afwijking gelijk is aan 0.
* $E(y)=$ determinstische component

## Verschil deterministisch model $\Leftrightarrow$ kansmodel
![Verschil modellen](https://i.imgur.com/GlP20CK.png)
## Bivariate gegevens
= gegevens die bestaan uit 2 variabelen.
*Voorbeelden:*
* Lengte van de vader en lengte van de zoon
* Het gewicht van een auto en zijn remafstand
* De lengte en de breedte van een bloemblaadje.
* De buitentemperatuur en het gasverbruik

### Onafhankelijke veranderlijke
= een variabele die men gebruikt om voorspellingen op te baseren. Op de $x$-as.

### Afhankelijke veranderlijke
= een variabele waarover men een voorspelling doet. Op de $y$-as.

### Bivariate gegevens voorstellen
* Via puntenwolk
= scatterplot
= scattergram
= spreidingsdiagram
= een grafische voorsteling van bivariate gegevens $(x_i, y_i)$

### Samenhang aflezen via puntenwolk
Aanwezigheid, sterkte en richting (zin) van de samenhang bij elllipsvormige puntenwolken.
* Rechte waarrond punten gelegen zijn
* Lineaire samenhang:
	* Sterke linaire samenhang: zeer smalle ellips
	* Zwakke linaire samenhang: wijdere ellips
	* Geen linaire samenhang: cirkelvormige puntenwolk

*Voorbeeld sterke linaire samenhang:*
![enter image description here](https://i.imgur.com/5lobOXI.png)

### Richting en zin van de puntenwolk
* Positieve linaire samenhang
	* Neemt de ene variabele toe, dan neemt de andere ook toe
* Negatieve linaire samenhang
	* Neemt de ene variabele toe, dan neemt de andere variabele af.

## Covariantie
* De covariantie $S_{xy}$ drukt een maat uit voor de (linaire) samenhang tussen twee stochastische variabelen
* De covariantie meet hoe de verandering van de ene variabele de verandering van de andere beinvloedt. 
* De covariantie $Cov(x,y)=S_{xy}$ tussen twee stochastische variableen $x$ en $y$ wordt gegeven door:

$Cov(x,y)=\frac{\sum_{i=1}^{N}(x_i-\mu_x)\cdot(y_i-\mu_y)}{N}$ = Populatie covariantie
$Cov(x,y)=\frac{\sum_{i=1}^{N}(x_i-\overline{x})\cdot(y_i-\overline{y})}{n-1}$ = Steekproef covariantie


### Intuitieve benadering van de covariantie
![enter image description here](https://i.imgur.com/l1M9E7s.png)

## Correlatie
De correlatie(coëfficënt)
* Genormaliseerde covariantie
* = een indexgetal dat altijd gelegen is tussen de $-1.0$ en $+1.0$

$r_{xy}=\frac{cov(x,y)}{\sqrt{s^2_x\cdot s^2_y}}=\frac{cov(x,y)}{s_x\cdot s_y}=\frac{s_{xy}}{s_x\cdot s_y}$

### Eigenschappen van de correlatie(coëfficënt) $r_{xy}$
* $r_{xy} > 0 \Rightarrow$ positieve linaire samenhang
* $r_{xy} < 0 \Rightarrow$ negatieve linaire samenhang
* $r_{xy} = +1 \Rightarrow$ perfect positieve linaire samenhang
* $r_{xy} = -1 \Rightarrow$ perfect negatieve samenhang
* $r_{xy} = 0 \Rightarrow$ ontbreken van linaire samenhang

## Linair kansmodel
### Kleinste-kwadratenmethode
= om te vinden welke lijn de best passende rechte is door een spreidingsdiagram
Kleinste-kwadraten lijn = Least Squares Line = de lijn $\hat{y}=\hat{\beta_0}+\hat{\beta_1}\cdot x$ die voldoet aan de volgende twee voorwaarden:
1. De som van alle errors $=0 \Rightarrow$ de gemiddelde fout = 0
2. De som van de gekwadrateerde fouten is minimaal

#### Formules voor de kleinstekwadratenschatting
De regressielijn wordt gegeven door $\hat{y}=\hat{\beta_1}\cdot x + \hat{\beta_0},$ waarbij:
* De helling $\hat{\beta_1}=\frac{Cov(x,y)}{var(x)}=r_{xy}\cdot \frac{s_y}{s_x}=\frac{SS_{xy}}{SS_{xx}}$
	* $SS_{xy} = \sum(x_i-\overline{x})\cdot(y_i-\overline{y})$
	* $SS_{xx} = \sum(x_i-\overline{x})^2$
	* $r_{xy}=$ de correlatiecoëfficiënt.
* Het snijpunt met de y-as: $\hat{\beta_0}=\overline{y}-\hat{\beta_1}\cdot\overline{x}$
	* $\overline{x}$ is het gemiddelde/verwachte waarde van x
	* $\overline{y}$ is het gemiddelde/verwachte waarde van y

### De determinatiecoëffiënt $r^2$
* De determinatiecoëffiënt meet in hoeverre $x$ bijdraagt aan het voorspellen van $y$
* De determinatiecoëffiënt geeft weer welk deel van de totale variatie verklaard wordt door de linaire relatie
* Bereken hiervoor hoeveel kleiner de afwijking in de voorspelling van $y$ kan worden door het gebruiken van de informatie die door $x$ wordt gegeven.

$r^2=\frac{SS_{yy}-SSE}{SS_{yy}}=1-\frac{SSE}{SS_{yy}}$,

met:
* $SS_{yy}=\sum(y_i-\overline{y})^2$
* $SSE = \sum(y_i-\hat{y})^2$
* $r^2=\frac{\text{Verklaarde steekproefvariantie}}{\text{Totale steekproefvariantie}}$

#### Eigenschappen van de determinatiecoëffiënt $r^2$
* $r^2$ is altijd gelegen tussen $-1$ en $+1$
* Bij enkelvoudige regressie is de determinatiecoëffiënt gelijk aan het kwadraat van de correlatiecoëfficiënt
* Ongeveer $100\cdot (r^2)%$ van de steekproefvariantie in $y$ kan verklaard worden door het gebruiken van $x$ voor het voorspellen van $y$ in het lineaire model.

## One-hot encoding
= omzetten van categorische variabelen naar meerdere aparte variabelen

![enter image description here](https://i.imgur.com/a6yWs0y.png)

# Hoofdstuk 7 & 8: Tijdreeksen
## Definitie
= gegevens(stromen) die door processen in de loop van de tijd worden geproduceerd.
*Voorbeelden:*
* Indexcijfers
* Weerbericht
* De vraag naar elektriciteit
* De omzetcijfers per kwartaal
* Beurskoers
* Temperatuursverloop
* Het maandelijks aantal passagiers bij Brussels Airlines

## 4 componenten van een tijdreeks $Y_t$
$Y_t = T_t + C_t + S_t + R_t$
1. Trend $T_t$
2. Conjunctuur $C_t$
3. Seizoen $S_t$
4. Toeval $R_t$

### Trend $T_t$
* Langetermijnbeweging
* Evolutie van de tijdreeks over lange tijd
* Engels: *secular trend*
![enter image description here](https://i.imgur.com/BrIpAzH.png)

### Conjunctuur $C_t$
* Fluctuaties rond de langetermijntrend
* Veroorzaakt door bijvoorbeeld economische omstandigheden
* Engels: *cyclical effect*
![enter image description here](https://i.imgur.com/n49nWxa.png)
### Seizoen $S_t$
* Regelmatig terugkerende beweging/fluctuatie
* Heeft een vaste geringe periodiciteit
* Engels: *seasonal effect*
![enter image description here](https://i.imgur.com/bwk8OVm.png)

### Toeval $R_t$
* Factoren die geen duidelijk patroon hebben
* Veroorzaakt door willekeurige externe invloeden
* Engels: *residual effect*
![enter image description here](https://i.imgur.com/dk77zEP.png)
## Voorspellingsfout
= *forecast error*
= werkelijke waarde - voorspelde waarde
### Maten om voorspellingsfouten uit te drukken:
* **MAE (Mean Absolute Error):** gemiddelde van de absolute waarde van de voorspellingsfouten
* **MSE (Mean Squared Error):** gemiddelde van de som van de gekwadrateerde voorspellingsfouten
* **MAPE (Mean Absolute Percentage Error):** gemiddelde absolute procentuele fout
### Eigenschappen
*  Voorspelling op basis van het gemiddelde van de historische waarden levert in alle gevallen een kleinere fout
* Als de data stationair is zal het gemiddelde in bijna alle gevallen een betere voorspelling geven
* Belangrijk dat een voorspellingsmethode zich snel kan aanpassen aan toekomstige veranderingen

## Stationaire reeksen
= De statistische paramaters van de tijdreeks, zoals het gemiddelde en de variantie zijn niet afhankelijk van de tijd en veranderen dus niet
* Er is geen trend aanwezig
* De plot heeft een horizontaal patroon
![enter image description here](https://i.imgur.com/obVG4cQ.png)
## Voorspellen van stationaire tijdreeksen
### Voortschrijdend gemiddelde (=moving average)
= Methodes gebaseerd op het voortschrijdend gemiddelde gebruiken de $k$ meest recente waarden in de tijdreeks als voorspelling voor de volgende periode.
Het voortschrijdend gemiddelde van orde $k$ wordt gegeven door:
$F_{t+1} = \frac{\sum(k\text{ meest recente waarden})}{k}=\frac{Y_t + Y_{t-1}+...+Y_{t-k+1}}{k}$
$F_{t+1}$ is de voorspelling voor de periode $t+1$
$Y_t$ is de waarde van de tijdreeks op tijdstip $t$

#### Voortschrijdend gemiddelde als filter
Het VG kan gebruikt worden om ruis in het signaal/tijdreeks weg te filteren.
* VG om de trend in de data bloot te leggen en fluctuaties weg te werken.
* Filter niet in voorspellingsmodus gebruiken
* Herreken elke waarde $Y(t)$ als een nieuwe gefilterde waarde $F(t)$ door het gemiddelde te nemen van $Y(t)$ met $k-1$ vorige waarden:
$F_t = \frac{\text{huidige waarde} + \sum(k-1) \text{meest recente waarden}}{k}$
$F_t=\frac{Y_t + Y_{t-1} + ... + Y_{t-k+1}}{k}$

*Voorbeeld:* fluctuaties wegwerken en trend overhouden:
![](https://i.imgur.com/o875NqI.png)

*Voorbeeld:* ruis uit de tijdreeks verwijderen:

![enter image description here](https://i.imgur.com/l4WFHEL.png)
### Exponentiële demping
Gebruikt een gewogen gemiddelde van vorige waarden als een voorspelling voor de volgende periode (waarde):
$F_{t+1} = \alpha \cdot Y_t + (1-\alpha)\cdot F_t$
* $F_{t+1}$ voorspelling van de tijdreeks voor periode $t+1$
* $Y_t$ huidige waarde van de tijdreeks in periode $t$
* $\alpha$ de dempingsconstante $(0 \leq \alpha \leq 1)$
	* De dempingsconstante $\alpha$ is het gewicht van de huidge waarde in periode $t$
	* $(1-\alpha)$ is het gewicht dat aan het verleden wordt toegekend.
#### Berekenen van de exponentiële demping
* Veronderstellen we een tijdreeks met maar $3$ perioden $Y_1, Y_2, Y_3$
* Om te starten: $F_1 = Y_1$
* De voorspelling voor periode 2 wordt:
$F_2=\alpha\cdot Y_1 + (1-\alpha)\cdot F_1$
$= \alpha\cdot Y_1 + (1-\alpha)\cdot Y_1$
$=Y_1$
* De voorspelling via E.D. voor periode 2 is gelijk aan de actuele waarde van de tijdreeks in periode 1
* De voorspelling voor periode 3 wordt:
$F_3 = \alpha \cdot Y_2 + (1- \alpha)\cdot F_2$
* De voorspelling voor periode 4 wordt:
$F_4=\alpha\cdot Y_3 + (1-\alpha)\cdot F_3$
$= \alpha\cdot Y_3 + (1-\alpha)\cdot [\alpha \cdot Y_2 + (1- \alpha)\cdot F_2]$
$= \alpha\cdot Y_3 + \alpha\cdot(1-\alpha)\cdot Y_2 + (1-\alpha)^2\cdot Y_1$
* Voorspelling $F_4$ is een gewogen gemiddelde van de eerste 3 perioden.
* Waarden van $\alpha$:

|||
|--|--|
|$\alpha$ groot| $\alpha$ klein|
|Groot gewicht aan actuale waarden <br>Voorspelling op korte termijn|Grotere stabiliteit.<br>Variaties wegwerken|


## Niet-stationaire reeks
= Er is een trend aanwezig waardoor het gemiddelde en/of de variantie van de tjidreeks in de tijd verandert.
* Bij veel voorspellingstechnieken is het aangewezen om niet-stationaire tijdreeksen stationair te maken door de trend te verwijderen.

### Voorspellen van niet-stationaire reeksen
Via het verwijderen van de trend:
1. Niet-stationaire gegevens stationair maken door de trend uit de tijdreeks te verwijderen. 
$Y_s = Y - \hat{Y} = Y - (\beta_1\cdot X + \beta_0)$
2. Voorspellen op basis van voortschrijdend gemiddelde of exponentiële demping.
$F_s =$ voorspelling van $Y_s$
3. Trend terug toevoegen.
$F=F_s + \hat{Y} = F_s + (\beta_1\cdot X + \beta_0)$

## Seizoensregressie
### Seizoensregressie zonder trend
*Voorbeeld: verkoop van paraplu's*

![enter image description here](https://i.imgur.com/SHlqqFU.png)
* Kwartaalcijfers in functie van kwartaal 4:
Verkopen = $95.0 + 29.0 \cdot Q1 + 57.0 \cdot Q2 + 26.0 \cdot Q3$
	* Kwartaal 1 cijfers=$95,0+29,0×\bold{1}+57,0×0+26,0×0=124$
	* Kwartaal 2 cijfers=$95,0+29,0×0+57,0×\bold{1}+26,0×0=152$
	* Kwartaal 3 cijfers=$95,0+29,0×0+57,0×0+26,0×\bold{1}=121$
	* Kwartaal 4 cijfers=$95,0+29,0×0+57,0×0+26,0×0=95$
### Seizoensregressie met trend
1. Bepaal de trendlijn en verwijder hem uit de tijdreeks
2. De de seizoensvoorspelling (seizoensregressie zonder trend)
3. Voeg de trend terug toe.

# Hoofdstuk 9:  Inconsistente data
## Ontbrekende data
= gaten / lege cellen, niet-geregistreerde data

### Mechanismes van ontbrekende data
1. MCAR (Missing Completely At Random)
	* De ontbrekende waarde $y$ hangt niet af van $x$ noch van $y$.
	* Willekeurig
2. MAR (Missing At Random)
	* De ontbrekende waarde $y$ hangt af van $x$, maar niet van $y$ zelf.
	* *Voorbeeld:* mannen gaan minder snel een enquete invullen onafhankelijk van de mate van depressie.
3. MNAR (Missing Not At Random)
	* De kans dat een waarde van een variabele ontbreekt hangt af van de variabele die ontbreekt
	* Het feit dat de data ontbreekt geeft informatie over de variabele die ontbreekt
	* *Voorbeeld:* Een temperatuursensor valt uit als de omgevingstemperatuur te hoog wordt.

### Analyse van ontbrekende data
1. Identificeer de ontbrekende data
	* Via een grafiek: plot de data en zoek naar gaten in de plot
	* Via Excel: tel het aantal gegevens (count / countif)
	* Via tijdsanalyse: 
		* Vergelijk met een correcte dataset
		* Controleer de timestamps bij de geregistreerde data of tijdsverschil tussen de registraties
		* Check voor errors bij het registratieproces
	* Onmogelijke waarden
	* Verkeerde types data
	* Corrupte gegevens
2. Zoek de oorzaak van de ontbrekende data
	* Natuurlijke aftakeling
		* Overlijden
		* Stoppen met invullen van enquete
		* Verminderen van belangstelling om waarde te registreren
	* Opzettelijke corrupte data
		* Sabotage
		* Manipulatie van data
	* Fouten tijdens het registreren van data (technische en niet-technische)
3. Bepaal de distributie van de ontbrekende data
	* Ga na wat de kans is dat data ontbreekt.
	* Hebben bepaalde datareeksen een grotere kans op ontbrekende gegevens dan andere?
	* Zit er willekeur in het ontbreken van de gegevens?
	* Wat is het interval tussen opeenvolgende onderbrekingen?
	* Hebben voorgaande waarden een effect op het al dan niet optreden van een onderbreking?
4. Gebruik de passende methode voor het omgaan met ontbrekende data.

## Methode 1: Listwise deletion
* De volledige rij verwijderen als een bepaalde cel in die rij ontbreekt/corrupt is
### Voordelen
* Simpel
### Nadelen
* Vermindert de betrouwbaarheid van statistische conclusies omdat de steekproefgrootte kleiner
* Gebruikt niet alle beschikbare informatie
* Werkt alleen met volledig (correct) geregistreerde data records
### Wanneer gebruiken
* De ontbrekende data is MCAR
* De resterende dataset blijft groot genoeg
* Bij tijdreeksen: als het verloop van de data geen rol speelt

## Methode 2: Pairwise deletion
* Negeer enkel de ontbrekende/corrupte waarden, zonder de volledige rij te schrappen
* Analyseer variabele aan de hand van de resterende gegevens
### Voordelen
* Er blijft meer data beschikbaar
* Gebruikt bij een analyse alle beschikbare informatie
### Nadelen
* Geen vergelijking tussen de variabele mogelijk omdat de gegevens niet meer gesynchrnoiseerd zijn.
* Verschillende samplegroottes
* Statistische parameters gebaseerd op verschillende sets gegevens
* Gebruikt niet alle beschikbare informatie
### Wanneer gebruiken
* Alleen bij een zeer beperkt aantal ontbrekende gegevens
* Bij voorkeur niet gebruiken.

## Methode 3: Gemiddelde/modus substitutie
Vervang ontbrekende/corrupte waarden door het gemiddelde of modus
### Voordelen
* Je kan werken met een volledige dataset
* Mogelijk om variabelen met elkaar te vergelijken. (gelijklopende data)
### Nadelen
* Voegt geen nieuwe bijkomende informatie toe
* Het gemiddelde blijft onveranderd
* De variabiliteit vermindert met een onderschatting ervan (en van de fout) tot gevolg.

## Methode 4: Substitutie via regressie
Gebruik de bestaande waarden om de ontbrekende waarden te voorspellen via een (lineaire) regressie
### Voordelen
* Meestal beter dan substitutie door het gemiddelde/modus
* De correlatie met andere gegevens blijft grotendeels, wat bij het gemiddelde niet het geval is.
### Nadelen
* Het probleem met de variantie blijft: de variantie wordt kleiner (substitutiewaarden liggen op de regressielijn)
* Er wordt geen extra informatie aan de datareeks toegevoegd.

## Linaire interpolatie berekenen
* Linaire interpolatie tussen twee opeenvolgende waarden = een geinterpoleerde waarde $L(x)$ gelegen tussen twee punten $(x_k, y_k)$ en $(x_{k+1}, y_{k+1})$ kan berkened worden via: 
	* $L(x) = y_k + (x-x_k) \cdot \frac{y_{k+1}-y_k}{x_{k+1}-x_k}$

## Niet-synchrone tijdreeksen
* Problematiek
	* Verschillende bemonsteringsgevallen tussen de tijdreeksen
![enter image description here](https://i.imgur.com/YEUpc2T.png)	
	* Niet equidistante onregelmatigede tijdsintervallen
![enter image description here](https://i.imgur.com/dOnmuEd.png)	
	* Tijdsverschuiving tussen de tijdreeksen
		* *Voorbeeld*: zelfde bemonsteringsfrequentie van de twee sensoren, maar bemonstering op verschillende tijdstippen

![enter image description here](https://i.imgur.com/grCWfaP.png)

### Listwise deletion
Beschouw enkel de metingen op tijdstippen waar volledige records beschikbaar zijn. 
* Subsampling van de tijdreeks
* Vermindert de betrouwbaarheid van statistische conclusies omdat de steekproefgrootte kleiner is.

![enter image description here](https://i.imgur.com/sCdowUw.png)

### Interpolatie
Gebruik interpolatie om de data van de ene tijdreeks te herrekenen naar de sampletijden van de andere tijdreeks

## dx/dt analyse
![enter image description here](https://i.imgur.com/AI49wFI.png)

$dx/dt$ analyse wordt gebruikt om na te gaan of veranderingen van de opeenvolgende waarden van de tijdreeks binnen bepaalde grenzen gebeuren.
*  *Voorbeelden*:
	* De temperatuur in ene lokaal kan in een minuut tijd met 10 graden stijgen of met 15 graden dalen
	* De snelheid van een vrachtwagen kan in 1 seconde niet met 50 km/h toenemen
	* Een nieuwe volledig geladen batterij van een smartphone kan in 40 minuten tijd onder normaal gebruik niet leeglopen.

* Bepalen:
	* aan de hand van grafiek: zoek zeer sterke stijgingen of dalingen
	* aan de hand van afgeleide: bepaal het verschil tussen de meest recente waarde en de vorige waarde. Zoek vervolgens naar extreme onrealistische waarden.



## One-hot encoding
* Doel
	* Omzetten van categorische variabelen naar aparte variabelen

![enter image description here](https://i.imgur.com/1lEN9IQ.png)
In python:
![enter image description here](https://i.imgur.com/8nfbsah.png)

Opgepast voor de *dummy variable trap*

# Hoofdstuk 10: AI
|Woord|Ontstaan|Definitie|
|--|--|--|
|Artificial Intelligence|1950's| Verzamelnaam voor software die problemen oplost door middel van algoritmes die sterk lijken op natuurlijke (menselijke) intelligentie|
|Machine Learning|1980's| Een methode om AI zelf dingen aan te leren door middel van grote hoeveelheden data|
|Deep Learning|2010's| Een deelverzameling van machine learning waarbij beslissingen worden gemaakt door een neuraal netwerk om zo tot een oplossing te komen.|

## Leerstrategieën
### Supervised
Leer uit data met antwoorden
* Classification vs Regression
### Unsupervised
Leer uit data zonder antwoorden
Toepassingen:
* Clustering
* Anomaly Detection
* Dimensionality reduction
### Reinforcement
Neem de beste actie door interactie met de omgeving
## Deep learning
Deel van machine learning waarbij kunstmatige neurale netwerken gebruikt worden. Kan beide supervised of niet supervised zijn.
![enter image description here](https://i.imgur.com/5sfjPES.png)


<!--stackedit_data:
eyJoaXN0b3J5IjpbLTMzMDI1NjczNCw2ODkwMDI5NiwtMTEwOD
E0NTYyMCwtMjA1NDg1OTMwLDE5MjUwNzU4MDEsLTE4ODc4NjAw
OTEsLTExNDQwODE0NDYsLTk5MDA5ODc3OCwtMTkwNTcwODgwNy
wtOTYwMTI0NDU4LDMwNDcxMjI2LDIwNTY4Nzc2NzIsMTIyNTM2
OTA2OCwtNzU1NTEyNjUxLC0xMTEyNDA2NjM1LC0xNjY2MjE5OD
c1LC0xNDk3OTgxMjUyLDEwNzI5NTkyNjMsLTkxNjg4MTU2MSwx
NTIzNzM0MjQ4XX0=
-->