#include <stdio.h>

void main()
{
	int height;
	scanf("%d", &height);
	int min = 1, max = 1;
	for (int line = 1; line <= height; line++)
	{
		// printf("line %d min %d max %d", line, min, max);
		if (line %2 ==1) {
			for (int i = min; i <= max; i++) {
				printf("%d ", i);
			}
		} else {
			for (int i = max; i >= min; i--) {
				printf("%d ", i);
			}
		}
		printf("\n");
		min = max+1;
		max= min+line;
	}
}
/*
in 5
out //lẻ thì tiến chẵn thì lùi 
1
3 2
4 5 6
10 9 8 7
*/