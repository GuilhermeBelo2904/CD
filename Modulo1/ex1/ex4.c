#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <string.h>

#define MAX_LINE_SIZE 1024

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
        printf("Symbol: %c, Frequency of occurrence: %d\n", (temp->data)->s, (temp->data)->occ);
        temp = temp->next;
    }

    free_list(head);
}

int main() {
    file_histogram("test.txt");

    return 0;
}
