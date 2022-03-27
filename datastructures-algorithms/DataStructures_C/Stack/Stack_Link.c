#include<stdio.h>
#include<stdlib.h>

typedef struct Node {
    int data;
    struct Node* next;
} Node;

Node* head;

void Push(int number) {
    Node* temp = (Node*)malloc(sizeof(Node));
    temp -> data = number;    
    temp -> next = head;
    head = temp;
    printf("Added %d to stack...\n", head -> data);
}

void Pop() {
    Node* temp = head;
    printf("Removed %d from stack...\n", temp -> data);
    head = temp -> next;
}

void Top() {
    Node* temp = head;
    printf("Top: %d \n", temp -> data);
}

void IsEmpty() {
    if(head == NULL) {
        printf("Stack is empty...\n");
    }
    else
        printf("Stack not empty...\n");
}

int main() {
    head = NULL;
    IsEmpty();
    Push(100);
    Push(21);
    Push(30);
    Pop();
    Push(1);
    Push(2);
    Top();
    IsEmpty();
    return 0;
}