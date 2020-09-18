int led = 9;
int led2 = 2;

void setup() {
  Serial.begin(9600);
  pinMode(led, OUTPUT); //maakt niet uit of je het analoog of digitaal aanstuurt, gewoon altijd als output
  pinMode(led2, OUTPUT);
  digitalWrite(led2, HIGH);
  Serial.println("Opgestart");
}

void loop() {
  int statusRes = analogRead(A1);
  float spanning = toVoltage(statusRes);
  //Serial.println("De digitale waarde is: " + String(statusRes));
  //Serial.println("De spanningswaarde is: " + String(spanning) + "V.");
  //Serial.println("De stroomwaarde is:    " + String(toCurrent(spanning, 220) * 1000) + "mA.");

  analogWrite(led, 255 - statusRes/383.0 * 255);


  delay(100);
}


float toVoltage(float analogeWaarde) {
  return (analogeWaarde / 1023.0) * 5.0;
}

float toCurrent(float u, float r) {
  return u / r;
}
