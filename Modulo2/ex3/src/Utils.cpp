#include "Utils.hpp"

bool isPrime(int number) {
    if (number <= 1) {
        return false;
    }
    for (int i = 2; i <= sqrt(number); i++) {
        if (number % i == 0) {
            return false;
        }
    }
    return true;
}

void printPrimes(int N) {
  while (true) {
    delay(3000);
    Serial.print("\n");  
    for (int i = 2; i <= N; i++) {
      if (isPrime(i)) {
        Serial.print(i); 
        Serial.print('\n'); 
        delay(15);
      }
    }
  }
}



