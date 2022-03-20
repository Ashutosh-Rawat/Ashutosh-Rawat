// This method is same as insert at tail method for doubly linked list

#include<stdio.h>
#include<stdlib.h>

typedef struct Node {
    int data;
    struct Node* prev;
    struct Node* next;
} Node;

Node* head;

void InsertNode(int number) {
    Node* temp = (Node*)malloc(sizeof(Node));
    temp -> data = number;
    temp -> prev = NULL;      // NULL is address 0
    temp -> next = NULL;

    if(head == NULL) {
        head = temp;
        return;
    }

    Node* temp2 = head;
    while(temp2 -> next != NULL) {
        temp2 = temp2 -> next;
    }
    temp2 -> next = temp;
    temp -> prev = temp2;
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
    InsertNode(3);
    InsertNode(10);
    InsertNode(102);
    InsertNode(11);
    InsertNode(1);
    Print();
    PrintReverse();
    return 0;
}