#include<stdio.h>
#include<stdlib.h>

typedef struct queue {
    int data;
    struct queue* next;
} queue;

queue *front, *rear;

void enque(int number) {
    queue* temp = (queue*)malloc(sizeof(queue));
    temp->data = number;
    temp->next = NULL;

    if(front==NULL) {
        front = temp;
        rear = front;
        rear->next = NULL;
        return;
    }
    else {
        rear->next = temp;
        rear = rear->next;
    }
}
void deque() {
    if(front==rear) {
        front = front->next;
        rear = front;
        return;
    }
    front = front->next;
}

void printQueue() {
    printf("\n");
    queue* head = front;
    while(head!=NULL) {
        printf("%d  ", head->data);
        head = head->next;
    }
}

int main() {
    enque(30);
    enque(45);
    enque(10);
    enque(50);
    printQueue();
    deque();
    printQueue();
    deque();
    printQueue();
    deque();
    printQueue();
    deque();
    printQueue();
    enque(33);
    printQueue();
    
    return 0;
}