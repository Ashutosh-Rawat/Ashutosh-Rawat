#include<stdio.h>
#include<stdlib.h>

int number, position;
typedef struct Node {
    int data;
    struct Node* next;
} Node;

Node* head;

void InsertAtNth(int position, int number) {
    Node* temp1 = (Node*)malloc(sizeof(Node));
    temp1 -> data = number;
    temp1 -> next = NULL;
    if(position == 1 || head == NULL) {
        temp1 -> next = head;
        head = temp1;
        return;
    }
    Node* temp2 = head;
    for(int i=0;i<position-2;i++){
        temp2 = temp2 -> next;
    }
    temp1 -> next = temp2 -> next;
    temp2 -> next = temp1;
}

void Print() {
    Node* temp = head;
    printf("List is : ");
    while(temp!=NULL) {    
        printf("%d  -> ", temp->data);
        temp = temp->next;
    }
    printf("NULL");
    printf("\n");
}

int main() {
    head = NULL;
    InsertAtNth(4, 5); // 5
    Print();
    InsertAtNth(2, 1); // 5 1
    Print();
    InsertAtNth(1, 3);  // 3 5 1
    Print();
    InsertAtNth(2, 9);  // 3 2 5 1
    Print();
    return 0;
}