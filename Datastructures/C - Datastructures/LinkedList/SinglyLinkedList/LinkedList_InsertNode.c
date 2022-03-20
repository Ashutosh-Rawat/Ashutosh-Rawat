// this program inserts nodes in a serial in linked list

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
    }
    

    else {
        Node* temp2 = head;
        int count = 1;
        while(temp2 -> next != NULL) {
            temp2 = temp2 -> next;
            count++;
        }
        temp2 -> next = temp;
    }


}
void Print() {
    Node* temp = head;
    printf("List is: ");
    while(temp != NULL) {
        printf("%d -> ", temp -> data);
        temp = temp -> next;
    }
    printf("NULL\n");
}

int main() {
    head = NULL;
    InsertNode(3); // 3
    Print();
    InsertNode(4); // 3 4
    Print();
    InsertNode(5); // 3 4 5
    Print();
    InsertNode(2); // 3 4 5 2 
    Print();
    InsertNode(8); // 3 4 5 2 8
    Print();
}