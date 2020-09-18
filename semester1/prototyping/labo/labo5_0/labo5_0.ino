int led = 3;

void setup() {
  Serial.begin(9600);
  pinMode(led, OUTPUT); //maakt niet uit of je het analoog of digitaal aanstuurt, gewoon altijd als output
}

void loop() {
  int statusRes = analogRead(A0);
  
  
  analogWrite(led, statusRes/4); //analoge uitgangen: altijd 8bits: tussen 0 en 255
  delay(1000);
  analogWrite(led, 0);
  delay(1000);
}
