const bool stap[8][4] = {
  {0, 0, 0, 1},
  {0, 0, 1, 1},
  {0, 0, 1, 0},
  {0, 1, 1, 0},
  {1, 1, 0, 0},
  {1, 0, 0, 0},
  {1, 0, 0, 1}
};

int step = 1;

const int pin[] = {2, 3, 4, 5};

int theStep = 0;

String ontvangen;

void setup() {
  // put your setup code here, to run once:
  for (int i = 0; i < 4; i++) {
    pinMode(pin[i], OUTPUT);
  }
  Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:

  if (Serial.available()) {
    ontvangen = Serial.readString();
  }



  doStep(theStep++);
  if (theStep > 7) {
    theStep = 0;
  }
  //de Arduino controller is sneller dan de steppermotor, 
  //tussen elke puls zullen we één milliseconde delay moeten inbouwen. 
  delay(1);
}

void doStep(int n) {
  for (int i = 0; i < 4; i++) {
    digitalWrite(pin[i], stap[n][i]);
  }
}
