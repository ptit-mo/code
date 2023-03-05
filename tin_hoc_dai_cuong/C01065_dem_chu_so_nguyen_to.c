#include <stdio.h>
int isPrime(int num)
{
	if (num < 2) return 0;
	for (int i = 2; i * i <= num; i++)
	{
		if (num % i == 0)  return 0; 
	}
	return 1;
}
int main()
{
	long long num;
	scanf("%lld", &num);
	int freq[10] = {0};
	int order[10] = {0};
	int curOrder = 9;
	while (num > 0)
	{
		int digit = num % 10;
		num /= 10;
		if (isPrime(digit))
		{
			freq[digit]++;
			if (freq[digit] == 1) //first time 
				order[curOrder--] = digit;
		}
	}
	for (int n = 0; n < 10; n++) {
		int digit = order[n];
		if (digit > 0 && freq[digit] > 0) {
			printf("%d %d\n", digit, freq[digit]);
		}
	}
	return 0;
}