#include <stdio.h>

void solve(int num)
{
	int res = 1;
	for (int i = 2; i <= num; i++)
	{
		if (num % i == 0) {
			res *= i;
		}
		while (num % i == 0)
		{
			num /= i;
		}
	}
	printf("%d\n", res);
}
void main()
{
	int numTests;
	scanf("%d", &numTests);
	while (numTests--)
	{
		int num;
		scanf("%d", &num);
		solve(num);
	}
}