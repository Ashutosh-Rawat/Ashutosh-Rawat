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

void Print(Node* point) {
    if(point == head) {
        printf("\nList is: \n");
        
    }
    if(point == NULL) {
        printf("NULL\n");
        return;
    }

    printf("%d -> ", point -> data);
    point = point -> next;
    Print(point);
}

void Println() {
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
    InsertNode(14);
    Print(head);
    InsertNode(20);
    InsertNode(110);
    Print(head);
    return 0;
}