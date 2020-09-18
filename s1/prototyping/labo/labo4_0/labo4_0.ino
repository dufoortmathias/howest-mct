
void setup() {
  //Voor analoge inputs is het niet nodig om pinMode te gebruiken.
  Serial.begin(9600);
  Serial.println("Opgestart");
}

void loop() {
  int inputPotMeter = analogRead(A0);
  Serial.println("De waarde van de potentiometer is: " + String(inputPotMeter));
  Serial.println("De spanning bedraagt " + String(aantalVolt(inputPotMeter)) + "V.");
  delay(10);
}

float aantalVolt(float analogeWaarde){
  return (analogeWaarde/1023.0) * 5.0;
}
