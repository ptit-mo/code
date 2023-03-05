#include <stdio.h>
#include <string.h>
#include <stdlib.h>
 void uocChungNhoNhat(char *num, int size) {
	int len = size/2;
	char num1[len], num2[len];
	for (int i =0; i< len; i++) {
		num1[i] = num[i];
	}
	for (int i =len; i< size; i++) {
		num2[i] = num[i];
		printf("%c", num2[i]);
	}
	printf("\n");
	char *temp1;
	long n1 = strtol(num1, &temp1, 10);
	char *temp2;
	long n2 = strtol(num2, &temp2, 10);
	printf("%ld %ld\n", n1, n2);

 }

void main() {
	int numTests;
	scanf("%d", &numTests);
	while (numTests--)
	{
		char num[18];
		scanf("%s", num);
		int size = strlen(num);
		if (size % 2 == 1) {
			printf("INVALID\n");
		} else {
			uocChungNhoNhat(num, size);
		}
	}
	
}