#include <stdio.h>
#include <string.h>

void countMostfrequent(int *array, int size) {
	int max = 0;
	int freq[30001] = {0};
	int order[size];
	memset(order, 0, sizeof(order));
	int curPosition = 0;
	for (int i = 0; i < size; i++) {
		int num =array[i];
		freq[num]++; 
		if (freq[num] == 1) { //first time appear
			order[curPosition++] = num;
		}
		if (max < freq[num]) {
			max = freq[num];
		}
	}
	for (int i = 0; i < size; i++) {
		if (freq[order[i]] == max) {
			printf("%d ",order[i]);
		}
	}
	printf("\n");
}
int main()
{
	int numTests;
	scanf("%d", &numTests);
	while (numTests--)
	{
		int size;
		scanf("%d", &size);
		int array[size];
		for (int i = 0; i < size; i++) {
			scanf("%d",&array[i]);
		}
		countMostfrequent(array, size);
	}
	
}