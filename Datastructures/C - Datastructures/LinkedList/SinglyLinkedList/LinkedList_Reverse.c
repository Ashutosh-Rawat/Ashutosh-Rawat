#include<stdio.h>
#include<stdlib.h>

typedef struct Node {
    int data;
    struct Node* next;
} Node;

Node* head;

void InsertNode(int number) {
    Node* temp = (Node*)malloc(sizeof(Node));
    temp -> data = number;
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
}

void ReverseList() {
    Node *current, *prev, *next;
    current = head;
    prev = NULL;
    while(current != NULL) {
        next = current -> next;
        current -> next = prev;
        prev = current;
        current = next;
    }
    head = prev;
}

void Print() {
    Node* temp = head;
    printf("List is: ");
    while(temp != NULL) {
        printf("%d -> ", temp -> data);
        temp = temp -> next;
    }
    printf("NULL\n\n");
}

int main() {
    head = NULL;
    printf("\n");
    InsertNode(3);
    InsertNode(5);
    InsertNode(20);
    InsertNode(100);
    Print();
    ReverseList();
    Print();

    InsertNode(102);
    InsertNode(33);
    InsertNode(14);
    InsertNode(43);
    InsertNode(26);
    Print();
    ReverseList();
    Print();
    return 0;
}