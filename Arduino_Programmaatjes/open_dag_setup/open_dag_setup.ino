#include <Servo.h>

// Servo myservo; 

int potPin = A2;  
int servoPin = 2;
const int SIZE = 6;
int LEDS[SIZE] = {6, 7, 8, 9, 10, 11};
int potValue; 
typedef enum {state_LEDS, state_DELAY} state; // Switch between setting the amount of LEDS or the amount of delay.
state currentState = state_DELAY;

void setup() {
  // Setup LEDS
  for(int i = 0; i < SIZE; i++){
    pinMode(LEDS[i], OUTPUT);
  }
  // myservo.attach(servoPin);
  Serial.begin(9600);
}

void loop() {
  int LEDSValue; 
  // int ServoValue; 
  // ServoValue = map(potValue, 0, 1023, 0, 180); 
  // myservo.write(ServoValue);    
  if(currentState == state_LEDS){
  potValue = analogRead(potPin);
  LEDSValue = map(potValue, 0, 1023, 0, SIZE);
  for(int i = 0; i <= SIZE; i++){
    if(LEDSValue >= i){
    digitalWrite(LEDS[SIZE - i], HIGH);
    } else {
    digitalWrite(LEDS[SIZE - i], LOW);
    }
  }
  } else if(currentState == state_DELAY){
      potValue = analogRead(potPin);
      LEDSValue = map(potValue, 0, 1023, 0, 500); // Max delay van 500 ms
      for(int i = 0; i < SIZE; i++){
       digitalWrite(LEDS[i], HIGH);
      }
      delay(LEDSValue);
      for(int i = 0; i < SIZE; i++){
       digitalWrite(LEDS[i], LOW);
      }
    delay(LEDSValue);
  }
}
