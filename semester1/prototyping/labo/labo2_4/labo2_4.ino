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
  digitalWrite(rood, HIGH);
  digitalWrite(geel, LOW);
  digitalWrite(groen, LOW);
  delay(3000);
  digitalWrite(rood, LOW);
  digitalWrite(geel, HIGH);
  digitalWrite(groen, LOW);
  delay(3000);
  digitalWrite(rood, LOW);
  digitalWrite(geel, LOW);
  digitalWrite(groen, HIGH);
  delay(3000);
}
