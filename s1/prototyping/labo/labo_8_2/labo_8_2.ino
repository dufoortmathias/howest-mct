int passieveBuzzer = 10;
int actieveBuzzer = 9;
int knop = 2;
int led = 3;
String inKomend;

void setup() {
  pinMode(knop, INPUT_PULLUP);
  pinMode(led, OUTPUT);
  pinMode(passieveBuzzer, OUTPUT);
  pinMode(actieveBuzzer, OUTPUT);
  Serial.begin(9600);

  Serial.println("Gelieve een getal groter dan 0 te geven: ");
}

void loop() {
  // put your main code here, to run repeatedly:

  if (Serial.available()) {
    inKomend = Serial.readString();
    Serial.print("U gaf in: ");
    Serial.println(inKomend);
  }

  if (inKomend.toInt() > 0) {
    toon(inKomend.toInt());
  } else if(inKomend.length() > 0){
    Serial.println("Foute waarde. Gelieve een getal groter dan 0 te geven.");
  }

  toon(inKomend.toInt());

}

void toon(int aantalMicroseconden) {
  digitalWrite(passieveBuzzer, HIGH);
  delayMicroseconds(aantalMicroseconden);
  digitalWrite(passieveBuzzer, LOW);
  delayMicroseconds(aantalMicroseconden);

}
