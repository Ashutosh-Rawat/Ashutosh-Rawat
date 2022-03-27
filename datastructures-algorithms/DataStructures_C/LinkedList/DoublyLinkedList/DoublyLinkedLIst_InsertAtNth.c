#include<stdio.h>
#include<stdlib.h>

typedef struct Node {
    int data;
    struct Node* prev;
    struct Node* next;
} Node;
Node* head;

void InsertAtNth(int number, int position) {
    Node* temp = (Node*)malloc(sizeof(Node));
    temp -> data = number;
    temp -> prev = NULL;
    temp -> next = NULL;
    if(head == NULL) {
        printf("No node present, adding node %d at beginning...\n", temp -> data);
        head = temp;
        return;
    }
    Node* temp2 = head;
    if(position == 1) {
        temp2 -> prev = temp;
        temp -> next = temp2;
        head = temp;
        /*
        This can also be coded as (saves a variable):
            head -> prev = temp;
            temp -> next = head;
            head = temp;
        */
        printf("Inserting node %d at position %d...\n", temp -> data, position);
        return;
    }
    for(int i=0;i<position-2;i++) {
        if(temp2 -> next == NULL) {
            temp2 -> next = temp;
            temp -> prev = temp2;
            return;
        }
        temp2 = temp2 -> next;
    }
    temp -> next = temp2 -> next;
    temp -> next -> prev = temp;
    temp2 -> next = temp;
    temp -> prev = temp2;
    printf("Inserting node %d at position %d...\n", temp2 -> next -> data, position);
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

    while(temp -> next != NULL) {
        temp = temp -> next;
    }
    printf("Reversed List is: \n");
    while(temp != NULL) {
        printf("%d -> ", temp -> data);
        temp = temp -> prev;
    }
    printf("NULL\n");
}

int main() {
    head = NULL;
    printf("\n");
    InsertAtNth(53, 2); // 53
    Print();
    InsertAtNth(34, 1); // 34 53
    Print();
    InsertAtNth(42, 2); // 34 42 53
    Print();
    InsertAtNth(110, 3); // 34 42 110 53
    Print();
    InsertAtNth(102, 100); // 34 42 110 53 102
    Print();
    PrintReverse();

    InsertAtNth(12, 4); // 34 42 110 12 53 102
    InsertAtNth(55, 10); // 34 42 110 12 53 102 55
    InsertAtNth(60, 5); // 34 42 110 60 13 53 103 55
    Print();
    PrintReverse();
    return 0;
}