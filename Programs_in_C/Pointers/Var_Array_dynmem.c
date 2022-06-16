#include<stdio.h>
#include<stdlib.h>

int main() {
    int n;
    printf("Enter size of array : ");
    scanf("%d", &n);
    // wrong statement 
    /* 
    int A[n];  this will show a compilation error as compiler doesn't know the amount of memory it needs
    */
    // right statement

    int* A = (int*)malloc(n*sizeof(int));   

    /* this statement can also be written as : 
        int* A = (int*)calloc(n, sizeof(int));
        since calloc takes two inputs first is number of elements and second is size of element
    */
    printf("\nArray: \n");
    for(int i=0;i<n;i++) {
        *A = i+101;                 // or A[i] = i+101;
        printf("%d ", *A);          // or A[i]
        A++;                        
    }
    free(A);
    
    /* The use of realloc : this can be done if we use another pointer and point it to the first pointer
    int *B = (int*)realloc(A, 2*sizeof(int));
    
    since void* realloc(void* ptr, size_t size);
    it also copies value to the new addresses
    if we pass void to the first parameter it is same as malloc i.e. it creates the new pointer and addresses but does not copies the values to the new address
    */

    return 0;
}