#include<stdio.h>
#include<stdlib.h>

typedef struct Node {
    int data;
    struct Node* next;
} Node;

Node* head;

void InsertAtNth(int position, int number) {
    Node* temp1 = (Node*)malloc(sizeof(Node));
    temp1 -> data = number;
    temp1 -> next = NULL;
    if(head == NULL || position == 1) {
        temp1 -> next = head;
        head = temp1;
        return;
    }
    Node* temp2 = head;
    for(int i=0;i<position-2;i++) {
        temp2 = temp2 -> next;
    }
    temp1 -> next = temp2 -> next;
    temp2 -> next = temp1;
}
void InsertArray(int* ref, int number) {
    printf("Added array to the list: \n");
    for(int i=1;i<=number;i++) {
        InsertAtNth(i, ref[i-1]);
    }
}
void InsertArrayM(int* ref, int number) {
    printf("Added array to the list: \n");
    for(int i=0;i<number;i++) {
        Node* temp = (Node*)malloc(sizeof(Node));
        temp -> data = ref[i];
        temp -> next = NULL;
        
        Node* temp2 = head;
        while(temp2 -> next != NULL) {
            temp2 = temp2 -> next;
        }
        temp2 -> next = temp;
    }
}
void DeleteAtN(int position) {
    Node* temp1 = head;
    Node* temp2 = head;

    if(position == 1) {
        head = temp1 -> next;
        printf("Deleted node %d having data %d\n", position, temp1 -> data);
        free(temp1);
        return;
    }

    for(int i=0;i<position-2;i++) {
        temp2 = temp2 -> next;
        if(temp2 -> next == NULL) { 
            printf("Position more than number of nodes present, total nodes: %d\n", i+2);
            return;
        }
    }
    temp1 = temp2 -> next;
    temp2 -> next = temp1 -> next; 
    printf("Deleted node %d having data %d\n", position, temp1 -> data);
    free(temp1);
}
void Print() {
    Node* temp = head;
    printf("List is: ");
    while(temp != NULL) {
        printf("%d -> ", temp -> data);
        temp = temp -> next;
    }
    printf(" NULL\n\n");
}
int main() {
    printf("\n");
    int Array[10] = {100, 101, 102, 103, 104, 105, 106, 107, 108, 109};
    int n = sizeof(Array)/sizeof(int);
    InsertArray(Array, n);
    Print();
    DeleteAtN(5);
    Print();
    DeleteAtN(2);
    Print();
    DeleteAtN(10);
    Print();
    
    int Arr[] = {201, 202, 203, 204, 205};
    int number = sizeof(Arr)/sizeof(int);
    InsertArrayM(Arr, number);
    Print();
    DeleteAtN(1);
    Print();
    DeleteAtN(12);
    Print();
    DeleteAtN(12);
    Print();
}