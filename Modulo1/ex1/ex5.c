#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <string.h>

void reverse_file(char *input_file_name, char *output_file_name) {
    FILE *input_file = fopen(input_file_name, "r");
    FILE *output_file = fopen(output_file_name, "w");

    fseek(input_file, 0, SEEK_END);

    long input_file_size = ftell(input_file);

    for (long i = input_file_size - 1; i >= 0; i--) {
        fseek(input_file, i, SEEK_SET);

        char ch = fgetc(input_file);

        fputc(ch, output_file);
    }

    fclose(input_file);
    fclose(output_file);

    printf("File reversed successfully.\n");
}

int main() {
    char input_file_name[] = "input.txt";
    char output_file_name[] = "output.txt";
    reverse_file(input_file_name, output_file_name);

    return 0;
}

