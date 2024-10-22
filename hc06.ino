#include<Servo.h>
#include <SoftwareSerial.h>
SoftwareSerial HC06(10,11);

Servo myServo;
String cmd;
int servoPin = 7;
int power = 3;

void setup(){
  HC06.begin(9600);
  myServo.attach(servoPin);
  pinMode(power, OUTPUT);

}

void loop(){
  digitalWrite(power, HIGH);

  if (HC06.available() > 0){
    cmd = HC06.readString();
    if (cmd == "ON"){
      myServo.write(0);
      delay(1000);
      myServo.write(30);
    }
  }
}