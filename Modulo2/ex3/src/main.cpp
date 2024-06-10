#include "Utils.hpp" 

int N = 0;
bool didPrint = false;

void setup() {
  Serial.begin(ARDUINO_UNO_BAUD_RATE);
  didPrint = false;
}

void loop() {
  
  if (Serial.available() > 0 && !didPrint) {
    N = Serial.parseInt(); 
    printPrimes(N);
    didPrint = true;
  }
}
