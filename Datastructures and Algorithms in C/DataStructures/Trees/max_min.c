#include<stdio.h>
#define max(x,y) ((x) >= (y)) ? (x) : (y)
#define min(x,y) ((x) >= (y)) ? (y) : (x)
int main() {
    int a=3, b=5;
    printf("max : %d\n", max(a,b));
    printf("min : %d\n", min(a,b));
    return 0;
}