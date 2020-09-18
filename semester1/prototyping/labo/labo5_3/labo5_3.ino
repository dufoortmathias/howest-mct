int led1 = 3;
int led2 = 5;
int led3 = 6;

int waardenR[] = {255, 0, 0, 128, 0, 128, 128, 255, 0};
int waardenB[] = {0, 255, 0, 128, 128, 0, 128, 255, 0};
int waardenG[] = {0, 0, 255, 0, 128, 128, 128, 255, 0};
int leds[] = {led1, led2, led3};

void setup() {
  // put your setup code here, to run once:
  pinMode(led1, OUTPUT);
  pinMode(led2, OUTPUT);
  pinMode(led3, OUTPUT);
  pinMode(A0, INPUT_PULLUP);
}

void loop() {
  // put your main code here, to run repeatedly:
  for(int i = 0; i < 3; i++){
    analogWrite(leds[i], analogRead((A0 / 1023.0) * 255.0));
  }
  
  //    analogWrite(led2, waardenB[i]);
  //    analogWrite(led3, waardenG[i]);
  delay(1000);



}
