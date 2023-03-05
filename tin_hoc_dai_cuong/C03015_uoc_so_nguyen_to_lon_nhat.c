#include <stdio.h>
int main()
{
	int numTests;
	scanf("%d", &numTests);
	while (numTests--)
	{
		long i = 2, n;
		scanf("%ld", &n);
		while (i <= n / i)
		{
			if (n % i == 0)
				n /= i;
			else
				i++;
		}
		printf("%ld\n", n);
	}
}