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

void ReverseList(Node* p) {
    if(head == p) {
        printf("\nReversing List...\n");
    }
    if(p -> next == NULL) {
        head = p;
        return;
    }
    ReverseList(p -> next);

    Node* temp = p -> next;
    temp -> next = p;
    p -> next = NULL;
}

void RecursePrint(Node* p) {
    if(p == NULL) {
        printf("NULL\n");
        return;
    }
    if(head == p) {
        printf("List is: \n");
    }
    printf("%d -> ", p -> data);
    RecursePrint(p -> next);
}

int main() {
    head = NULL;
    InsertNode(14);
    InsertNode(22);
    InsertNode(32);
    InsertNode(65);
    RecursePrint(head);

    ReverseList(head);
    RecursePrint(head);
    printf("\n");

    InsertNode(100);
    InsertNode(12);
    InsertNode(35);
    InsertNode(1);
    InsertNode(42);
    RecursePrint(head);

    ReverseList(head);
    RecursePrint(head);
    
    return 0;
}