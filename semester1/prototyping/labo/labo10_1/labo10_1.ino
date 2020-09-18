int servo = 7;
int huidigeHoek = 90;
int hoekOntvangen = 90;
//180 deg: 2200 us
//0   deg: 600  us
int laagsteWaarde = 500;
int hoogsteWaarde = 2400;

void setup() {
  // put your setup code here, to run once:
  pinMode(servo, OUTPUT);
  Serial.begin(9600);
  Serial.println("Geef een hoek in tussen 0 en 180 graden");
}

void loop() {
  // put your main code here, to run repeatedly:
  if (Serial.available()) {
    String ontvangen = Serial.readString();
    Serial.println(ontvangen);
    if(ontvangen.toInt() != huidigeHoek){
      hoekOntvangen = ontvangen.toInt();
      stelServoIn(gradenNaarPositie(hoekOntvangen));
      huidigeHoek = hoekOntvangen;
    }
  }

//  for (int i = 0; i < 10; i++) {
//    for (int i = 0; i < 180; i++) {
//      stelServoIn(gradenNaarPositie(i));
//    }
//
//    for (int i = 180; i >= 0; i--) {
//      stelServoIn(gradenNaarPositie(i));
//    }
//  }

  
}

void stelServoIn(int positie) {
  digitalWrite(servo, HIGH);
  delayMicroseconds(positie);
  digitalWrite(servo, LOW);
  delayMicroseconds(16000 - positie);
}

int gradenNaarPositie(int hoek) {
  float positie = (hoek / 180.0) * (hoogsteWaarde - laagsteWaarde);
  positie += laagsteWaarde;
  return positie;
}
