#include <stdio.h>

void solve1(int height)
{
	int max = 1;
	for (int line = 1; line <= height; line++)
	{
		// left
		int j = 1;
		for (int i = 0; i < max / 2; i++)
		{
			printf("%d", j);
			j += 2;
		}
		printf("%d", max);
		// right
		j = max - 2;
		for (int i = 0; i < max / 2; i++)
		{
			printf("%d", j);
			j -= 2;
		}
		max += 2;
		printf("\n");
	}
}
void solve2(int height)
{
	int len = 1;
	for (int line = 0; line < height; line++)
	{
		int res[len];
		int left = 0, right = len - 1;
		int filler = 1;
		while (left <= right)
		{
			res[left] = res[right] = filler;
			filler += 2;
			left++;
			right--;
		}
		for (int i = 0; i < len; i++)
		{
			printf("%d", res[i]);
		}
		printf("\n");
		len += 2;
	}
}

void main()
{
	int height;
	scanf("%d", &height);
	solve2(height);
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