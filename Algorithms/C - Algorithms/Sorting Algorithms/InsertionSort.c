#include <stdio.h>

void insertionSort(int arr[], int n) {
	int i, key, j;
	for (i = 1; i < n; i++) {
		key = arr[i];
		j = i - 1;

		while (j >= 0 && arr[j] > key) {
			arr[j + 1] = arr[j];
			j = j - 1;
		}
		arr[j + 1] = key;
	}
}

void printArray(int arr[], int n) {
	int i;
	for (i = 0; i < n; i++)
		printf("%d ", arr[i]);
    printf("\n");
}

int main() {
	int arr[] = { 9, 23, 10, 21, 95, 191, 67, 34, 12, 11, 13, 5, 6, 25, 16, 22, 29,87, 6, 54, 22, 43, 54, 2 };
	int n = sizeof(arr) / sizeof(arr[0]);
    printf("\nInput Array ...\n");
    printArray(arr, n);
    printf("\n\n"); 

	insertionSort(arr, n);
    printf("Sorted Array using Insertion Sort ...\n");
	printArray(arr, n);

	return 0;
}

