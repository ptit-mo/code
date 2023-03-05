#include <stdio.h>
void longestIncrementParts(int *array, int size, int testOrder) {
	printf("Test %d:\n", testOrder);
	//iterate twice, once is to find max, once is to print out
	int max = 1;
	if (size < 2) { printf("1\n%d\n", array[0]); return; }
	int left = 0, right = 1;
	while (right < size) {
		if (array[right] > array[right - 1]) {
			max = max > right - left + 1 ? max : right - left + 1;
			right++;
		} else {
			left = right;
			right ++;
		}
	}
	printf("%d\n", max);
	left = 0, right = 1;
	while (right < size)
	{
		while (array[right] > array[right - 1])
		{
			if (right - left + 1 == max) {
				for (int i = left; i <= right; i++) {
					printf("%d ", array[i]);
				}
				printf("\n");
				break;
			}
			right++;
		}
		left = right;
		right++;
	}
	
}
int main()
{
	int numTests;
	scanf("%d", &numTests);
	for (int test = 1; test <= numTests; test++) {
		int size;
		scanf("%d", &size);
		int array[size];
		for (int i = 0; i < size; i++) {
			scanf("%d",&array[i]);
		}
		longestIncrementParts(array, size, test);
	}
	
}