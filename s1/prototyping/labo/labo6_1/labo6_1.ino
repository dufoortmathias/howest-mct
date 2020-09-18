void setup() {
  Serial.begin(9600);
  

}

void loop() {
  // put your main code here, to run repeatedly:
  float value = analogRead(A0);
  Serial.println(String(value/1023.0 * 5.0) + "\t" + String(temperatuur(value/1023.0 * 5.0)));
  delay(400);
}


float temperatuur(float spanning){
  return -12.82*spanning + 77.82;
}
