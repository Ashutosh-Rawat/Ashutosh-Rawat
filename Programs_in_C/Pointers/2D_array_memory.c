#include<stdio.h>

void Input(int A[3][4]) {
    int a = 100;
    for(int i=0;i<=3;i++) {
        for(int j=0;j<=4;j++) {
            A[i][j] = a;
            a = a+4;
        }
    }
}

void Print(int A[3][4]) {
    for(int i=0;i<=3;i++) {
        for(int j=0;j<=4;j++) {
            printf("%d ", A[i][j]);
        }
        printf("\n");
    }
}
int main() {

    int Array[3][4];
    Input(Array);
    Print(Array);

    /* Array[i][j]  =   *(Array[i]+j)
                    =   *(*(Array+i)+j)
    */
    printf(" This is address of A[0][0] : %d\n", (*Array)); // is same as &Array[0][0] or &(Array[0][0]) returns the address of the Array(i+1)
    printf(" This is the value of A[0][0] : %d\n", *(*Array)); // is value at Array[0][0]
    printf(" This is address of A[0][1] : %d\n", (*Array+1)); // is same as &Array[0][1] or &(Array[0][0]+1) returns the address of the Array(i+1)
    printf(" This is the value of A[0][1] : %d\n", *(*Array+1));  /* This is derefrencing the derefrenced value of pointer to the first address of array*/
    printf(" This is address of A[1][0] : %d\n", *(Array+1)); // is same as &Array[1][0] or &(Array[0]+1) returns the address
    printf(" This is the value of A[1][0] : %d\n", *(*(Array+1))); 

    /* This is now the final part where we would assign a new pointer to the matrix and we would be able to find the concept of pointers with multi dimensional matrix */

    int (*P)[4] = Array;
    printf("\n");
    printf("\n This returns the first element of the first matrix : %d\n", *P);
    printf(" This is address of A[0][1] : %d\n", *P+1);
    printf(" This prints the address of first element too: %d\n", P);
    /* Here P points to the first 1D matrix of the 2D matrix or we say points to the Array[0][] 
    So printing it will still give the first element of the matrix P and *P gives the same yet the difference
    is what they points *P points to the first element of the first matrix */

    printf(" This is the value of Array[0][0] : %d\n", **P);
    printf(" This is the value of A[1][0] : %d\n", **(P+1));
    printf(" This is address of A[1][0] : %d\n", (P+1));
    printf(" This is address of A[1][0] : %d\n", *(P+1));
    printf(" This is address of A[2][2] : %d\n", *(P+2)+2);
    printf(" This is the value of A[2][2] : %d\n", *(*(P+2)+2));

    return 0;
}