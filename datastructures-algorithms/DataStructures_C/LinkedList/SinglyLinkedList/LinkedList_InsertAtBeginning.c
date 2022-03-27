#include<stdio.h>
#include<stdlib.h>

typedef struct Node {
    int data;
    struct Node* next;
} Node;

Node* head;

void InsertAtBeginning(int number) {
    Node* temp = (Node*)malloc(sizeof(Node));

        temp -> data = number;
        temp -> next = head;
        if(head != NULL) {
            temp -> next = head;
        }
        head = temp;
}
void Print() {
    Node* temp = head;
    while(temp!=NULL) {    
        printf("%d  ", temp->data);
        temp = temp->next;
    }
}


int main() {
    head = NULL;
    int flag = 1;
    int number, num;
    
    printf("How many to add: ");
    scanf("%d", &number);
    for(int i=0;i<number;i++) {
        printf("\nEnter number: ");
        scanf("%d", &num);
        InsertAtBeginning(num);
        Print();
    }

    
    return 0;
}