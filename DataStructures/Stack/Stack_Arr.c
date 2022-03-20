#include<stdio.h>
#include<stdlib.h>

int Array[10];
int head = -1;

void Push(int x) {
    head++;
    Array[head] = x;
    printf("Added %d to stack...\n", x);
}

void Pop() {
    int x = Array[head];
    //Array[head] = '\0';     // Can be done to clear it.
    head--;
    printf("Removed %d from stack...\n", x);
}

void Top() {
    printf("Top: %d\n", Array[head]);
}
void IsEmpty() {
    if(head == -1) 
        printf("Stack is empty...\n");
    else
        printf("Stack is not empty...\n");
}

int main() {
    IsEmpty();
    Push(10);
    Push(11);
    Push(20);
    Push(2);
    Pop();
    IsEmpty();
    Top();
    return 0;
}
