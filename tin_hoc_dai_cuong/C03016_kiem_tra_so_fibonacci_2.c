#include <stdio.h>
int isFib(long long num)
{
	if (num <= 1)
	{
		return 1;
	}
	long long dp[3];
	dp[0] = 0;
	dp[1] = 1;
	dp[2] = -1;
	while (dp[2] <= num)
	{
		dp[2] = dp[0] + dp[1];
		if (dp[2] > num)
		{
			return 0;
		}
		else if (dp[2] == num)
		{
			return 1;
		}
		else
		{
			dp[0] = dp[1];
			dp[1] = dp[2];
			dp[2] = -1;
		}
	}
	return 0;
}
int main()
{
	int numTests;
	scanf("%d", &numTests);
	while (numTests--)
	{
		long long num;
		scanf("%lld", &num);
		if (isFib(num))
		{
			printf("YES\n");
		}
		else
		{
			printf("NO\n");
		}
	}
}