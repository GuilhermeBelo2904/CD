#include <stdio.h>

void fibonacci(int N) {
    printf("First %d numbers of the fibonacci sequence:\n", N);
    int n = N;
    int last1;
    int last2;
    int actual;
    if(N >= 1) {
        printf("1\n");
    }
    last2 = 0;
    last1 = 1;
    for(int i = 2; i <= n; i++) {
        actual = last1 + last2;
        printf("%d\n", actual);
        last2 = last1;
        last1 = actual;
        
    }
}

int main() {
    fibonacci(15);
}
