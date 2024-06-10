#include "Utils.hpp"

bool flag = true;

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
  delay(3000);
  while(flag) {
    int checksum = 0;
    for (int i = 2; i <= N; i++) {
      if (isPrime(i)) {
          String prime = String(i);
          for (size_t j = 0; j < prime.length(); j++) {
            Serial.print(prime[j]);
            checksum += prime[j];
          }
          Serial.print(" ");
          checksum += 32;
      }
    }
    String checksumStr = String(~(checksum) & 0xFF);
    switch (checksumStr.length()) {
      case 1:
        Serial.print("00");
        break;
      case 2: 
        Serial.print("0");
        break;  
    }
    Serial.print(checksumStr);
    delay(4000);
   // flag = false;
  }
}
