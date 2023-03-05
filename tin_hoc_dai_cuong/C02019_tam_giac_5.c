#include <stdio.h>

void solve1(int height)
{
	int max = 2;
	int len = 1;
	for (int line = 1; line <= height; line++)
	{
		// left
		int j = 2;
		for (int i = 0; i < len / 2; i++)
		{
			printf("%d", j);
			j += 2;
		}
		printf("%d", max);
		// right
		j = max - 2;
		for (int i = 0; i < len / 2; i++)
		{
			printf("%d", j);
			j -= 2;
		}
		max += 2;
		len +=2;
		printf("\n");
	}
}
void main()
{
	int height;
	scanf("%d", &height);
	solve1(height);
}
/*
in 5
out
1
131
13531
1357531
135797531
*/