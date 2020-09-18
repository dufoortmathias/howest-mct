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
  if (!digitalRead(knop2)) {
    digitalWrite(rood, HIGH);
    digitalWrite(geel, HIGH);
    digitalWrite(groen, HIGH);
    delay(200);
    digitalWrite(rood, LOW);
    digitalWrite(geel, LOW);
    digitalWrite(groen, LOW);
    delay(200);
  }

  if (!digitalRead(knop1)) { //als knop ingedrukt is
    if (teller == 0) {
      digitalWrite(rood, HIGH);
      digitalWrite(geel, LOW);
      digitalWrite(groen, LOW);
    } else if (teller == 1) {
      digitalWrite(rood, LOW);
      digitalWrite(geel, HIGH);
      digitalWrite(groen, LOW);
    } else if (teller == 2) {
      digitalWrite(rood, LOW);
      digitalWrite(geel, LOW);
      digitalWrite(groen, HIGH);
    } else if (teller > 2) {
      digitalWrite(rood, LOW);
      digitalWrite(geel, LOW);
      digitalWrite(groen, LOW);
      teller = 0;
      delay(200);
      return;
    }
    teller ++;
    delay(200);
  }
}
