#include<stdio.h>

void Print(char *C) {
    while(*C != '\0') {
        printf("%c", *C);
        C++;
    }
    printf("\n");
}
int main() {

    char A[20] = "Hello World"; // this is constant type and cannot change the value to the array...
    Print(A);

    return 0;
}