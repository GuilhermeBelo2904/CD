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

short calculateChecksum(short sum) {
    short carry = sum >> 12;
    sum = sum + carry;
    return ~sum;
}

void printPrimes(int N) {
    delay(3000);
    while(flag) {
      byte msg[2];
      short checksum = 0;
      for (short i = 2; i <= N; i++) {
          if (isPrime(i)) {
              msg[0] = i >> 8;
              msg[1] = i & 0xFF;
              Serial.write(msg, 2);
              checksum += i;
              delay(15);
          }
      }
      checksum = calculateChecksum(checksum);
      msg[0] = checksum >> 8;
      msg[1] = checksum & 0xFF;
      Serial.write(msg, 2);
      flag = false;
    }
}
