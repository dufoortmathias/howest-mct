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

  Serial.println("Gelieve een getal groter dan 0 te geven: ");
}

void loop() {
  // put your main code here, to run repeatedly:
  if (Serial.available()) {
    inKomend = Serial.readString();
    Serial.print("U gaf in: ");
    Serial.println(inKomend);
    if(inKomend == "dingdong"){
      dingDong(500,1000);
    }else{
      digitalWrite(passieveBuzzer, LOW);
    }
  }
  
}

void dingDong(int frequency1, int frequency2){
  for(int i = 0; i < 600; i++){
    toon(frequency1);
  }
  for(int i = 0; i < 300; i++){
    toon(frequency2);
  }
}

void toon(int aantalMicroseconden) {  
  digitalWrite(passieveBuzzer, HIGH);
  delayMicroseconds(aantalMicroseconden);
  digitalWrite(passieveBuzzer, LOW);
  delayMicroseconds(aantalMicroseconden);
}
