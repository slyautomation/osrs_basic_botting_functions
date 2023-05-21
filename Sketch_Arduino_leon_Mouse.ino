/* HID KeyBoard Example
   by: Jim Lindblom
   date: 1/12/2012
   license: MIT License - Feel free to use this code for any purpose.
   No restrictions. Just keep this license if you go on to use this
   code in your future endeavors! Reuse and share.

   This is very simplistic code that allows you to send a 'z' with
   a momentary pushbutton.
*/

#include <Mouse.h>

int buttonPin = 9;  // Set a button to any pin
int y;
int i;
int l;
int x;
String list;
void setup()
{
  Serial.begin(115200);
  Serial.setTimeout(1);
  // pinMode(buttonPin, INPUT);  // Set the button as an input
  digitalWrite(buttonPin, HIGH);  // Pull the button high
  delay(1000);  // short delay to let outputs settle
  Mouse.begin(); //Init mouse emulation
}
void loop()
{
     if ( Serial.available()) {
      list = Serial.readStringUntil('\n'); //  Use readStringUntil to avoid the 1 second delay.
      if (list == "l") {
        Mouse.click(MOUSE_LEFT);
      }
      if (list == "r") {
        Mouse.click(MOUSE_RIGHT);
      }
      else {
      i = list.indexOf(";");
      l = list.length();
      x = list.substring(0,i).toInt(); 
      y = list.substring(i+1,l).toInt(); 
      Serial.println(x + " | " + y);
      }
  }
   //delay(1000);  // delay so there aren't a kajillion z's
   Mouse.move(x, y, 0); // move mouse on y axis
   //delay(1000);  // delay so there aren't a kajillion z's
   //Mouse.move(x, 0, 0); // move mouse on x axis
   x = 0;
   y = 0;
}
