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
    if(head == NULL) {
        head = temp;
        printf("Inserting node %d...\n", temp -> data);
        return;
    }
    Node* temp2 = head;
    while(temp2 -> next != NULL) {
        temp2 = temp2 -> next;
    }
    temp2 -> next = temp;
    temp -> prev = temp2;
    printf("Inserting node %d...\n", temp2 -> next -> data);
}

void DeleteNode(int position) {
    Node* temp;
    Node* temp2 = head;

    if(position == 1) {
        printf("Deleting node %d...\n", temp2 -> data);
        head = temp2 -> next;
        temp2 -> prev = NULL;
        return;
    }
    for(int i=0;i<position-2;i++) {
        if(temp2 == NULL) {
            printf("Position more that number of nodes, nodes present: %d\n", i);
            return;
        }
        temp2 = temp2 -> next;
    } 
    if(temp2 -> next -> next == NULL) {
        temp = temp2 -> next;
        temp2 -> next = NULL;
        temp -> prev = NULL;
        return;        
    }
    printf("\nDeleting node %d...\n", temp2 -> next -> data);
    temp = temp2 -> next -> next;
    temp -> prev = temp2;
    temp2 -> next = temp;
}
void Print() {
    Node* temp = head;
    printf("List is:\n");
    while(temp != NULL) {
        printf("%d -> ", temp -> data);
        temp = temp -> next;
    }
    printf("NULL\n");
}

int main() {
    head = NULL;
    InsertNode(15);
    InsertNode(10);
    InsertNode(5);
    InsertNode(20);
    InsertNode(33);
    InsertNode(60);
    Print();
    DeleteNode(5);
    Print();
    DeleteNode(100);
    DeleteNode(5);
    Print();
    DeleteNode(1);
    Print();
    return 0;
}