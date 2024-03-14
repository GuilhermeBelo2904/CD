#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <string.h>

#define INT_BIT sizeof(int) * 8
#define MAX_LINE_SIZE 1024

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


typedef struct symbol {
    char s;
    int occ;
} Symbol;

typedef struct node {
    Symbol * data;
    struct node * next;
} Node;

bool search_symbol(Node * head, char c) {
    while (head != NULL) {
        if ((head->data)->s == c) {
            return true;
        }
        head = head->next;
    }
    return false;
}

Node * createNode(Symbol * data) {
    Node * new_node = (Node*)malloc(sizeof(Node));
    new_node->data = data;
    new_node->next = NULL;
    return new_node;
}

void insertSymbol(Node ** head, Symbol * data) {
    Node * new_node = createNode(data);
    new_node->next = *head;
    *head = new_node;
}

void free_list(Node * head) {
    Node * temp;
    while (head != NULL) {
        temp = head;
        head = head->next;
        free(temp->data);
        free(temp);
    }
}

void file_histogram(char * file_name) {
    Node * head = NULL;

    char line[MAX_LINE_SIZE];
    FILE * f = fopen(file_name, "r");
    while (fgets(line, MAX_LINE_SIZE, f) != NULL) {
        for (int i = 0; i < strlen(line); i++) {
            if (!search_symbol(head, line[i])) {
                Symbol * currSymbol = (Symbol*)malloc(sizeof(Symbol));
                currSymbol->s = line[i];
                currSymbol->occ = 1;

                insertSymbol(&head, currSymbol);
            } else {
                Node * temp = head;
                while (temp != NULL) {
                    if ((temp->data)->s == line[i]) {
                        (temp->data)->occ++;
                        break;
                    }

                    temp = temp->next;
                }
            }
        }
    }

    fclose(f);

    Node * temp = head;
    while (temp != NULL) {
        printf("Symbol: %c, Frequency: %d\n", (temp->data)->s, (temp->data)->occ);
        temp = temp->next;
    }

    free_list(head);
}


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
    countBits(15);

    printf("Symbol freq: %d\n", file_symbol_freq("test.txt", 'c'));

    file_histogram("test.txt");

    char input_file_name[] = "input.txt";
    char output_file_name[] = "output.txt";
    reverse_file(input_file_name, output_file_name);

    return 0;
}
