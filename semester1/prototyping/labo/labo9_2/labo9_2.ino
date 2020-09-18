int motor = 5;
int knop = 2;
bool knopOudeStatus = 1;
bool knopNieuweStatus = 1;

void setup() {
  // put your setup code here, to run once:
  pinMode(motor, OUTPUT);
  pinMode(knop, INPUT_PULLUP);
  //digitalWrite(motor, HIGH);
  Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
  knopNieuweStatus = digitalRead(knop);

  if(knopNieuweStatus != knopOudeStatus){
    if(!knopNieuweStatus){
      if(!digitalRead(motor)){
        digitalWrite(motor, HIGH);
        Serial.println("HIGH");
      }else{
        digitalWrite(motor, LOW);
        Serial.println("LOW");
      }
    }
  }

  knopOudeStatus = knopNieuweStatus;
  delay(50);
}
