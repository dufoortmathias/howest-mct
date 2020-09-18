int knop = 5;
int ledBlauw = 4;
int ledRood = 3;
int knopOudeStatus = 1;
int knopNieuweStatus = 1;

int delaySpeed = 50;


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
  knopNieuweStatus = digitalRead(knop);
  if (knopNieuweStatus != knopOudeStatus) { //Flank gedetecteerd
    if (!knopNieuweStatus) { //stijgende flank
      delaySpeed += 50;
      Serial.println(delaySpeed);
    }
  }

  knopOudeStatus = knopNieuweStatus;

  digitalWrite(ledBlauw, LOW);
  digitalWrite(ledRood, HIGH);
  delay(delaySpeed);
  digitalWrite(ledRood, LOW);
  digitalWrite(ledBlauw, HIGH);
  delay(delaySpeed);


}
