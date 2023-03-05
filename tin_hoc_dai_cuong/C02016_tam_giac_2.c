#include <stdio.h>

void main() {
	int height;
	scanf("%d", &height);
	for (int line= 1; line<=height; line++) {
		int start = 1;
		if (line % 2 == 0) start = 2;
		for (int i = 0; i < line; i++) {
			printf("%d", start);
			start +=2;
		}
		printf("\n");
	}
}

/*
input 5
output
1
24
135
2468
13579
*/