#include<stdio.h>

int rear = -1;

int front(int* arr) {
    return arr[0];
}

int end(int* arr) {
    return arr[rear];
}
int isEmpty(int* arr) {
    if(rear == -1) return 1;
    else return 0;
}

int isFull(int* arr, int size) {
    if((rear+1) == size) return 1;
    else return 0;
}
void enque(int* array, int number, int size) {
    if(isFull(array, size) == 1) {
        printf("queue is full\n");
        return;
    }
    rear++;
    array[rear] = number;
    printf("Inserted %d to queue \n", array[rear]);
}

void dequeue(int* array) {
    if(isEmpty(array)) {
        printf("queue is empty\n");
        return;
    }
    int i = 0;
    printf("Removed %d from queue \n", front(array));
    while(i<rear) {    // complexity O(n) but the need is O(1) so it's not used insted use circular array
        array[i] = array[i+1];
        i++;
    }
    rear--;
}

int main() {
    int arr[20];
    int size = sizeof(arr)/sizeof(int);
    dequeue(arr);
    enque(arr, 1, size);
    enque(arr, 21, size);
    enque(arr, 201, size);
    dequeue(arr);
    enque(arr, 100, size);
    printf("Front: %d\n", front(arr));
    printf("End: %d\n", end(arr));

    return 0;
}