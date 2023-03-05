#include <stdio.h>

void main() {
	int height;
	scanf("%d", &height);
	int curMax = 1;
	for (int i= 0; i<height; i++) {
		for (int j=1; j <= curMax; j++) {
			printf("%d", j);
		}
		printf("\n");
		curMax+=2;
	}
}
/*
input 5
output
1
123
12345
1234567
123456789
*/