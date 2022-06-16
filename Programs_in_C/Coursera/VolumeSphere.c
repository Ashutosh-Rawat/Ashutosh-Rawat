#include<stdio.h>
#include<math.h>
#define PI 3.14159
int main(void)
{ 
 int radius;
 printf("Enter radius: ");
 scanf("%d", &radius);
printf("volume is : %f \n\n", 4*(pow((double)radius,3))/3 );
return 0;
}