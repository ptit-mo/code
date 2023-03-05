#include <stdio.h>

void main()
{
	int height;
	scanf("%d", &height);
	for (int line = 1; line <= height; line++)
	{
		int lead = line;
		printf("%d", lead);
		int adder = height - 1;
		for (int i = 1; i < line; i++)
		{
			printf(" %d", lead += adder);
			adder--;
		}
		printf("\n");
	}
}
/*
in 5
out
1
2 6
3 7 10
4 8 11 13
5 9 12 14 15
*/