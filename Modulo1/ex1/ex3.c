#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <string.h>

#define MAX_LINE_SIZE 1024

int file_symbol_freq( char *file_name, char symbol ) {
    FILE * f = fopen(file_name, "r");

    char line[MAX_LINE_SIZE];
    double total_file_size = 0.0;
    double symbol_count = 0.0;
    while(fgets(line, MAX_LINE_SIZE, f) != NULL) {
        for(int i = 0; i < strlen(line); i++) {
            if(line[i] == symbol) {
                symbol_count++;
            }
            total_file_size++;
        }
    }

    fclose(f);

    if(symbol_count == 0.0) {
        return -1;
    }

    return (symbol_count/total_file_size) * 100;
}

int main() {
    printf("Symbol freq: %d\n", file_symbol_freq("test.txt", 'c'));

    return 0;
}
