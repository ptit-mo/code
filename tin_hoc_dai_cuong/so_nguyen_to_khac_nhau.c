#include <stdio.h>

void checkPrime(int num) {
	if (num <=1) return;
	for (int i = 2; i*i <= num; i++) {
		if (num%i == 0) {
			return;
		}
	}
	printf("%d ", num);
}
void sort(int arr[], int size) {
	for (int i = 0; i<size-1; i++) {
	for (int j = 1; j<size; j++) {
		if (arr[i] < arr[j]) {
			int temp = arr[i];
			arr[i] = arr[j];
			arr[j] = temp;
		}
	}	
	}
	for (int i = 1; i<size; i++) {
		if (arr[i] == arr[i-1]) {
			arr[i] = 0;
		}
		}
}
void main() {
	int numTests;
	scanf("%d", &numTests);
	while (numTests--)
	{
		int size;
		scanf("%d", &size);
		int arr[size];
		for (int i = 0; i < size; i++) {
			scanf("%d", &arr[i]);
		}
		sort(arr, size);
		for (int i = 0; i < size; i++) {
			checkPrime(arr[i]);
		}
		printf("\n");
	}
	
}