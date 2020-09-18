# H1
* Digitale pinnen: kunnen gebruikt worden als digitale in- en uitgangen of als analoge uitgang als de pin voorzien is van het PWM-symbool ~.
* Knop met INPUT_PULLUP en weerstand

# H2
* $AF = x%$ van de afgelezen waarde + $y$ digit
* Spanningen:
	* Rode led: $2V$
	* Blauwe led: $3V$
	* Diode: $0.7V$
* Knop inlezen met:

		if(!digitalRead(knop)){
		...
		}


* Flank, met als voorbeeld een LED togglen:

		void loop(){
			  knopNieuweStatus = digitalRead(knop);
			  if (knopNieuweStatus != knopOudeStatus) { //Flank gedetecteerd
			      if (knopNieuweStatus) {
			          Serial.println("Stijgende flank");
			          if (digitalRead(led) == HIGH) { //led inlezen en toggle
			              digitalWrite(led, LOW);
			          } else {
			              digitalWrite(led, HIGH);
			          }
			      } else {
			          Serial.println("Dalende flank");
			      }
			  }

			  knopOudeStatus = knopNieuweStatus;
		  }

### Meten van spanning
* Over het component (parallel)

# H3

### Meten van stroom
* In serie
* Stroom is overal hetzelfde behalve bij een splitsing (Stroomwet van Kirchhof)

### Serial monitor
* Serial.begin(9600);

# H4
* Weerstandsmetingen met de ohmmeter gebeuren **spanningsloos**
* Floats casten: String(getal, 3): zal de float naar een string casten met 3 cijfers na de komma 

### Potentiometer
* via analoge pin met analogRead(A0);
* Spanning: (analogeWaarde / 1023.0 ) * 5.0 
* Als je een trimmer wil aansluiten aan een **digitale** in- of uitgang moet er altijd een weerstand in serie staan met de trimmer
* Heeft 3 pins:
![enter image description here](https://i.ytimg.com/vi/wUAiBnPg3TU/maxresdefault.jpg)

# H5:
### Diode
![enter image description here](https://wikitronics.nl/wp-content/uploads/2019/04/Diode.jpg)
* Laat stroom door in 1 richting (van + naar -)
* Kan gebruikt worden als OR-gate
* Wordt gebruikt bij voorrangsschakelingen
* 0.7V

### RGB LED
* 3 leds in 1 behuizing met 4 poten
	* Gemeenschappelijke kathode (-) = GND
	* Andere 3: rood, groen, blauw = aansluiten aan 3 PWM-ingangen $\Rightarrow$ waardes tss 0 en 255

# H6
### Hysterese
* Bv regeling van de centrale verwarming: als de verwarming ingesteld staat op 20°C, zal de verwarming aanslaan bij 19.5°C, en weer uitschakelen bij 20.5°C.
![enter image description here](https://i.imgur.com/9b50ydy.png)

### NTC (Thermistor)
= Negative Temperature Coefficient
* Weerstand verschilt op basis van welk model NTC
![enter image description here](https://i.imgur.com/vWm8ydW.png)

### LM35 (TMP35)
![enter image description here](https://cdn.instructables.com/FE0/DHQ4/HV2AIB01/FE0DHQ4HV2AIB01.MEDIUM.jpg)
* $V_{\text{out}}$ naar A0, met daartussen een weerstand (1kΩ) die naar de grond gaat

### Interne weerstand van een bron
Een spanningsbron heeft zelf een interne weerstand $R_i$, want het kost moeite om de elektronen zich door de bron te verplaatsen
$R_i = \frac{U_{bron} - U_{out}}{I_{kring}}$, met $U_{out}$ de spanning over de externe weerstand

# H7
### Condensator
* Spanning meten:
	* $\tau = R\cdot C$
	* Bij opladen:
		* $U_C = U_{bron} \cdot (1 - e^{\frac{-t}{\tau}})$
	* Bij ontladen:
		* $U_C = U_{bron} \cdot (e^{\frac{-t}{\tau}})$
* Capaciteit: in Farad ($F$)
	* $C[F] = \frac{q[C]}{U[V]}$ (tussen vierkante haakjes = eenheden)
	* = Coulomb per Volt
	* meestal in micro- of nano-Farad


# H8
### Geluid
1. Frequentie (=toonhoogte)
2. Amplitude/niveau (luider)

### Piëzo effect
Onder invloed van spanning vervormen kristallen van bepaalde materialen, die vervorming kan geluidstrillingen veroorzaken. 

### Actieve buzzer
* Beschikt over een ingebouwde oscillator. 
* Van zodra je een actieve zoemer onder spanning plaatst genereert hij een toon (altijd dezelfde toon)
* Met digitale uitgang
* Heeft een polariteit

### Passieve buzzer
* Beschikt niet over een oscillator
* We moeten een blokgolf creëren
* Heeft een polariteit
* Kan met PWM: een PWM-uitgang is een blokgolf met telkens een delay ertussen:

![enter image description here](https://circuitdigest.com/sites/default/files/projectimage_tut/Pulse-Width-Modulation.jpg)

### Serieel data ontvangen
* Byte per byte inlezen:


		if(Serial.available() > 0){
			incomingByte = Serial.read();
			Serial.println(incomingByte)
		}

* De hele buffer in 1 String inlezen:

		if(Serial.available() > 0){
			incomingString = Serial.readString();
			Serial.println(incomingString)
		}


# H9
## Transistor
* Bipolar Junction Transistor (BJT), waarvan 2 versies bestaan:
	* NPN (bv: PN2222, BC337)
	* PNP
* 3 pootjes: collector, base en emitter
	* Base: Bij spanning > 0.7V: transistor gaat in geleiding van collector naar emitter (zoals een diode)
	* Te gebruiken als schakelaar
* Verschillende versterkingsfactoren $\beta$: x10 ... x1000
	* $I_C = I_B \cdot \beta$

![enter image description here](https://www.componentsinfo.com/wp-content/uploads/2018/06/bc337-transistor-pinout-equivalent.gif)

### Schakeling met een motor
Parralel met de motor een diode: want bij het onderbreken van de stroom ontstaat er een inductiespanning in de spoel van de motor. Via de diode brengen we de stroom ontstaan door de inductiespanning bij afschakelen terug naar de motor en worden de transistor en Arduino niet beschadigd.
![enter image description here](https://i.imgur.com/ST2JsWc.png)

# H10
## Servomotor
### Opbouw
* een motor
* een reductiekast (set van tandwielen)
* een controller
* 3 draadjes:
	* PWM (oranje)
	* Vcc (rood)
	* GND (bruin)

### Werking
Om een bepaalde hoek mee te geven moeten we de signaaldrraad verbinden met een digitale uitgang van de Arduino. De servomotor verwacht een PWM-signaal. De standaard PWM uitgangen van onze Arduino kunnen we hiervoor echter niet gebruiken omdat die werken op een frequentie van 490Hz of 980Hz. De servomotor verwacht een PWM van 50Hz (periode T=20ms)
![enter image description here](https://i.imgur.com/HsbSdBO.png)
Onze servomotor kan een hoek van 180° maken. Daarvoor moeten we een hoge puls meegeven die varieert tussen de 600$\mu$s en de 2400$\mu$s (DC = 3 - 12%). Deze puls zullen we moeten herhalen tot de motor zijn gewenste positie heeft bereikt.

## Stappenmotor
### Opbouw
* een aantal spoelen in de stator (vast gedeelte van de motor)
* een aantal permanente polen in de rotor (draaiend gedeelte)
 
### Werking
Als we een stroom sturen naar de spoel, wordt er een magnetisch veld opgewekt. Door telkens een volgende spoel in de stator aan te sturen kunnen we de motor telkens een stap laten opschuiven. De stappenmotor kan, in tegenstelling tot de servo, blijven ronddraaien.

* Heeft een stepper driver nodig, want de gevraagde stroom is veel te hoog.
* Veel code nodig om het te besturen (zie 10-A-motoren.pdf)
<!--stackedit_data:
eyJoaXN0b3J5IjpbNjczNjM5NzQ4XX0=
-->