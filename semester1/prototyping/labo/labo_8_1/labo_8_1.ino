int passieveBuzzer = 10;
int actieveBuzzer = 9;
int knop = 2;
int led = 3;
String inKomend;

void setup() {
  pinMode(knop, INPUT_PULLUP);
  pinMode(led, OUTPUT);
  pinMode(passieveBuzzer, OUTPUT);
  pinMode(actieveBuzzer, OUTPUT);
  Serial.begin(9600);

  Serial.println("Geef in aan of uit: ");
}

void loop() {
  // put your main code here, to run repeatedly:
  
  if(Serial.available()) {
    inKomend = Serial.readString();
    Serial.print("U gaf in: ");
    Serial.println(inKomend);
  }

//  if(inKomend.equals("aan") or !digitalRead(knop)){
//    digitalWrite(led, HIGH);
//    digitalWrite(actieveBuzzer, HIGH);
//  }else if(inKomend.equals("uit") or digitalRead(knop)){
//    digitalWrite(led, LOW);
//    digitalWrite(actieveBuzzer, LOW);
//  }  

  digitalWrite(passieveBuzzer, HIGH);

  for(int i = 0; i < 500; i++){
    digitalWrite(actieveBuzzer, HIGH);
    delayMicroseconds(100);
    digitalWrite(actieveBuzzer, LOW);
  }
  
}
