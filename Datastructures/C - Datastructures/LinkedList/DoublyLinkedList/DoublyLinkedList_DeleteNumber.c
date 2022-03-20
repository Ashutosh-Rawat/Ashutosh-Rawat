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
    temp -> prev = NULL;
    temp -> next = NULL;

    printf("Inserting Node %d...\n", number);

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

void DeleteNumber(int number) {
    Node* temp = head;
    Node* temp2 = head;

    if(temp -> data == number) {
        printf("Deleting Number %d...\n", temp -> data);
        head = temp -> next;
        temp -> next -> prev = NULL;
        return;
    }
    while(temp != NULL) {
        if(temp -> next == NULL) {
            printf("Number %d not in list...\n",number);
            return;
        }
        if((temp -> next) -> data == number) {
         break;
        }
        temp = temp -> next;
        temp2 = temp2 -> next;
    }
    printf("Deleting Number %d...\n", (temp -> next) -> data);
    if((temp -> next) -> next == NULL) {
        temp -> next = NULL;
        return;
    }
    temp = (temp -> next) -> next;
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
    InsertNode(15);
    InsertNode(30);
    InsertNode(45);
    InsertNode(60);
    InsertNode(75);
    Print();
    PrintReverse();
    DeleteNumber(75);
    Print();
    DeleteNumber(4005);
    DeleteNumber(30);
    Print();
    InsertNode(34);
    InsertNode(103);
    InsertNode(40);
    Print();
    DeleteNumber(34);
    Print();
    DeleteNumber(15);
    Print();
    PrintReverse();
    return 0;
}