#include "Utils.hpp"

char lastNumber = '\0';
int lastInt = 0;

char calculateChecksum(char number1, char number2) {
  return ((~(number1 + number2)) & 0xFF);
}

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
  while(true){
  Serial.print("\n");  
  for (int i = 2; i <= N; i++) {
    if (isPrime(i)) {
      lastInt = i;
      String primeNumber = String(i);
      for (size_t j = 0; j < primeNumber.length(); j++) {
        if (lastNumber != '\0') {
          Serial.print(lastNumber);
          Serial.print(primeNumber[j]);
          Serial.print(calculateChecksum(lastNumber, primeNumber[j]));
          lastNumber = '\0';
        } else {
          lastNumber = primeNumber[j];
        }
      }
    }
  } 
  if (lastNumber != '\0') {
    Serial.print(lastNumber);
    Serial.print('\0'); 
    Serial.print(calculateChecksum(lastNumber, '\0'));
    lastNumber = '\0';
  }
  delay(4000);
  }
}






