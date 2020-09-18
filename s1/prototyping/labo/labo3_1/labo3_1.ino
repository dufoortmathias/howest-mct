int knop = 5;
int led = 4;
int knopOudeStatus = 1;
int knopNieuweStatus = 1;


void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600); //snelheid = 9600 baud
  pinMode(knop, INPUT_PULLUP);
  pinMode(led, OUTPUT);
}

void loop() {
  //Serial.println("De waarde van de knop is " + String(knopStatus));

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
  delay(50);
}
