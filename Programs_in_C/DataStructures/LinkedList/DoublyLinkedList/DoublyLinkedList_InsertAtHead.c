#include<stdio.h>
#include<stdlib.h>

typedef struct Node {
    int data;
    struct Node* prev;
    struct Node* next;
} Node;

Node* head;

void InsertAtHead(int number) {
    Node* temp = (Node*)malloc(sizeof(Node));
    temp -> data = number;
    temp -> next = NULL;
    temp -> prev = NULL;
    
    if(head == NULL) {
        head = temp;
        return;
    }
    temp -> next = head;
    head = temp;
    temp = temp -> next;
    temp -> prev = head;
}

void Print() {
    Node* temp = head;
    printf("List is: \n");

    while(temp != NULL) {
        printf("%d -> ", temp -> data);
        temp = temp -> next;
    }
    printf("NULL\n");
}

void PrintReverse() {
    Node* temp = head;

    printf("Reversed list is: \n");
    while(temp -> next != NULL) {
        temp = temp -> next;
    }
    while(temp != NULL) {
        printf("%d -> ", temp -> data);
        temp = temp -> prev;
    }
    printf("NULL\n");
}
int main() {
    head = NULL;
    InsertAtHead(3);
    InsertAtHead(10);
    InsertAtHead(102);
    InsertAtHead(40);
    Print();
    PrintReverse();
    return 0;
}