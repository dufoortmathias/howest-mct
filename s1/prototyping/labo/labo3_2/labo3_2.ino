int knop = 5;
int ledBlauw = 4;
int ledRood = 3;
int knopOudeStatus = 1;
int knopNieuweStatus = 1;


void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600); //snelheid = 9600 baud
  pinMode(knop, INPUT_PULLUP);
  pinMode(ledRood, OUTPUT);
  pinMode(ledBlauw, OUTPUT);
  digitalWrite(ledRood, HIGH);
  Serial.println("Opgestart");
}

void loop() {
  //Serial.println("De waarde van de knop is " + String(knopStatus));
  knopNieuweStatus = digitalRead(knop);
  if (knopNieuweStatus != knopOudeStatus) { //Flank gedetecteerd
    if (knopNieuweStatus) { //stijgende flank
      if (digitalRead(ledRood) == HIGH) { //led inlezen en toggle
        digitalWrite(ledRood, LOW);
        digitalWrite(ledBlauw, HIGH);
        Serial.println("Blauw brandt");
      } else { //dalende flank
        digitalWrite(ledBlauw, LOW);
        digitalWrite(ledRood, HIGH);
        Serial.println("Rood brandt");

      }
    }
  }

  knopOudeStatus = knopNieuweStatus;
  delay(50);
}
