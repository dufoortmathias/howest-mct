int led = 2;

void setup() {
  //Voor analoge inputs is het niet nodig om pinMode te gebruiken.
  Serial.begin(9600);
  Serial.println("Opgestart");
  pinMode(led, OUTPUT);
  digitalWrite(led, HIGH);
}

void loop() {
  int inputPotMeter = analogRead(A0);
  int inputLDR = analogRead(A1);
  int inputWeerstand = analogRead(A2);
/*
  //Serial.println("De waarde van de potentiometer is: " + String(inputPotMeter));
  //Serial.println("De spanning bedraagt " + String(aantalVolt(inputPotMeter)) + "V.");

  //Serial.println("De waarde van de LDR is: " + String(inputLDR));
  //Serial.println("De spanning bedraagt " + String(aantalVolt(inputLDR)) + "V.");

  if(inputLDR > 300){
    digitalWrite(led, HIGH);
  }else{
    digitalWrite(led, LOW);
  }
 */

  //spanning over de weerstand
  Serial.println("De spanning over de weerstand: " + String(aantalVolt(inputWeerstand)) + "V.");
  float stroom = aantalVolt(inputWeerstand)/220.0*1000.0; //in mA
  Serial.println(String(stroom) + "mA");
  delay(800);
}

float aantalVolt(float analogeWaarde){
  return (analogeWaarde/1023.0) * 5.0;
}
