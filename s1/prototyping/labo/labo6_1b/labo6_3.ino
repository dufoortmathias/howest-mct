int led = 2;

void setup() {
  Serial.begin(9600);
  pinMode(led, OUTPUT);
  digitalWrite(led, HIGH);

}

void loop() {
  float temp = analogRead(A0)/1023.0*5*100;
  float potentio = analogRead(A1)/1023.0*30;
  Serial.println("Temperatuur: " + String(temp) + "C\tSetpoint: " + String(potentio) + "C");

  if (potentio > temp - 0.5){
    digitalWrite(led, HIGH);
  }else if (potentio < temp + 0.5){
    digitalWrite(led, LOW);
  }else{
    digitalWrite(led, HIGH);
  }
  delay(1000);
}
