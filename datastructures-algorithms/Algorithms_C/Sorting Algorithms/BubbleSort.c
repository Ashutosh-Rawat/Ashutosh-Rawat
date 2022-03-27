#include<stdio.h>  
void main ()  
{  
    int i, j,temp, number;
    printf("Enter number of elements: ");
    scanf("%d", &number);

    int array[number];
    for(int i=0;i<number;i++) {
        printf("Enter element %d : ", i+1);
        scanf("%d", &array[i]);
    }   

    // Applying bubble sort:
    for(i = 0; i<number; i++)  
    {  
        for(j = i+1; j<number; j++)  
        {  
            if(array[j] < array[i])  
            {  
                temp = array[i];  
                array[i] = array[j];  
                array[j] = temp;   
            }   
        }   
    } 

    printf("\n\nSorted array using Bubble Sort ...\n");  

    for(i = 0; i<number; i++)  
    {  
        printf("%d  ", array[i]);  
    }  
}  