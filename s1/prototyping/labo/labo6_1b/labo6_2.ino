void setup() {
  Serial.begin(9600);
  

}

void loop() {
  // put your main code here, to run repeatedly:
  float value = analogRead(A0);
  Serial.println(String(value) + "\t" + String(value/1023.0*5*100) + "C");
  delay(400);
}
