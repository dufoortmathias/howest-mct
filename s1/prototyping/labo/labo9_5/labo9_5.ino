int led = 5;
bool knopOudeStatus = 1;
bool knopNieuweStatus = 1;

void setup() {
  // put your setup code here, to run once:
  pinMode(led, OUTPUT);
  digitalWrite(led, HIGH);
  Serial.begin(9600);
  Serial.println("Opgestart");
}

void loop() {
  // put your main code here, to run repeatedly:

  int a0 = analogRead(A0);
  int a1 = analogRead(A1);
  int a2 = analogRead(A2);
  int a3 = analogRead(A3);

  //Serial.println(String(a0) + " " + String(a1) + " " + String(a2) + " " + String(a3));

  float Vc = abs(a1 / 1023.0 * 5 - a0 / 1023.0 * 5);
  float Vb = abs(a2 / 1023.0 * 5 - a3 / 1023.0 * 5);

  float Ic = berekenStroom(330,  Vc);
  float Ib = berekenStroom(10000, Vb);

  Serial.println(String(Ic) + " " + String(Ib) + " " + String(berekenBeta(Ic, Ib)));

  delay(100);

}

float berekenStroom(float resistance, float voltage) {
  return voltage / resistance;
}

float berekenBeta(float Ic, float Ib) {
  return Ic / Ib;
}
