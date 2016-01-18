#include <Servo.h>

Servo myservo; 
                
int pos = 110;  // angle tracker
int angle = 10; // how much to rotate by
 
void setup()
{
  Serial.begin(9600);  //Begin serial communcation
  myservo.attach(9);  // attaches the servo on pin 9 to the servo object
  myservo.write(pos);
}
 
void loop()
{

  char var = Serial.read();
  switch (var) {
    case 't': 
      Serial.write("Tap!");
      pos = pos - angle;
      myservo.write(pos);
      delay(75);
      pos = pos + angle;
      myservo.write(pos);
    break;
    case 'p': //rotate +
        pos = pos + angle;
        myservo.write(pos);
        Serial.write(pos);
      break;
 
      case 'm': //rotate -
        pos = pos - angle;
        myservo.write(pos);
        Serial.write(pos);
      break;
  }

}
