#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <string.h>

#define INT_BIT sizeof(int) * 8

int countBits(int val) {
    int mask = 1;

    int countZero = 0;
    int countOne = 0;

    int n;
    for(int i = 0, n = val; i < INT_BIT; i++, n >>= 1) {
        int bit = n && mask;
        if(bit) {
            countOne++;
        } else {
            countZero++;
        }
    }

    printf("Number of zeros: %d\n", countZero);
    printf("Number of ones: %d\n", countOne);
}

int main() {
    countBits(53);

    return 0;
}