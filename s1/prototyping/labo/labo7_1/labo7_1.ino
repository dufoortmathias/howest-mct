int condensatorOut = 2;
int condensatorIn = A0;
bool opOntladen = true;
int huidigeTijd = 0;
int startTijd = 0;
int teller = 0;

void setup() {
  // put your setup code here, to run once:
  pinMode(condensatorOut, OUTPUT);
  Serial.begin(9600);
  Serial.println("Opgestart");
  digitalWrite(condensatorOut, LOW); // zorgen dat de condensator volledig is ontladen

  int analogValue = 0;
  do {
    analogValue = analogRead(condensatorIn);
  } while (analogValue > 5);

  delay(5000); // 5*tau wachten
  startTijd = millis();
}

void loop() {
  // put your main code here, to run repeatedly:
  int analogValue = analogRead(condensatorIn);

  if(teller < 3){
    opladen(analogValue);
    serialPlotter(analogValue);
    ontladen(analogValue);
  }

}

void opladen(int analogValue) {
  if(analogValue < 5){
    digitalWrite(condensatorOut, HIGH);
    startTijd = millis();
    opOntladen = true;
    teller++;
  }
}

void ontladen(int analogValue) {
  if(analogValue > 1020){
    digitalWrite(condensatorOut, LOW);
    startTijd = millis();
    opOntladen = false;
    teller++;
  }
}

void serialPlotter(int value) {
  if(opOntladen == true){
    Serial.print("opladen");
  }else{
    Serial.print("ontladen");
  }
  Serial.print(";");

  //afdrukken tijd
  huidigeTijd = millis();
  Serial.print(huidigeTijd - startTijd);
  Serial.print(";");
  Serial.println(berekenSpanning(value));
}

String berekenSpanning(int value){
  float spanning = value / 1023.0 * 5;
  String spStr = String(spanning);
  return spStr.replace(".", ",");
}
