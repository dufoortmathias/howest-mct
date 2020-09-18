int led = 8;

void setup() {
  //Voor analoge inputs is het niet nodig om pinMode te gebruiken.
  Serial.begin(9600);
  Serial.println("Opgestart");
  pinMode(led, OUTPUT);
}

void loop() {
  int inputPotMeter = analogRead(A0);
  int inputLDR = analogRead(A1);
  //Serial.println("De waarde van de potentiometer is: " + String(inputPotMeter));
  //Serial.println("De spanning bedraagt " + String(aantalVolt(inputPotMeter)) + "V.");

  Serial.println("De waarde van de LDR is: " + String(inputLDR));
  Serial.println("De spanning bedraagt " + String(aantalVolt(inputLDR)) + "V.");

  if(inputLDR > 300){
    digitalWrite(led, HIGH);
  }else{
    digitalWrite(led, LOW);
  }
  
  delay(400);
}

float aantalVolt(float analogeWaarde){
  return (analogeWaarde/1023.0) * 5.0;
}
