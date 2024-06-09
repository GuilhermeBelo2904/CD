#include "Utils.hpp" 

int N = 0;

void setup() {
  Serial.begin(ARDUINO_UNO_BAUD_RATE);
}

void loop() {
  if (Serial.available() > 0) {
    N = Serial.parseInt();
    printPrimes(N);
  }
}
