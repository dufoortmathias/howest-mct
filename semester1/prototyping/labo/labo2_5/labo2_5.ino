int rood = 13;
int geel = 12;
int groen = 11;
int knop1 = 4;
int knop2 = 5;

int teller = 0;

void setup() {
  // put your setup code here, to run once:
  pinMode(rood, OUTPUT);
  pinMode(geel, OUTPUT);
  pinMode(groen, OUTPUT);
  pinMode(knop1, INPUT_PULLUP);// !!!! PULLUP: zie labo2 arduino
  pinMode(knop2, INPUT_PULLUP); // !!!! PULLUP: zie labo2 arduino

}

void loop() {
  digitalWrite(groen, HIGH);
  digitalWrite(rood, LOW);
  if(!digitalRead(knop1)){
    digitalWrite(groen, LOW);
    digitalWrite(rood, HIGH);
    delay(2000);
  }
}
