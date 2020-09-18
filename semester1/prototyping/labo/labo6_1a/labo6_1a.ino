void setup() {
  Serial.begin(9600);
  

}

void loop() {
  // put your main code here, to run repeatedly:
  float value = analogRead(A0);
  float temp = value/1023.0*5*100;
  Serial.println(String(value, 1) + "mV\t" + String(temp, 1) + "C\t" + String(temp*9/5 + 32,1) + "F");
  delay(400);
}
