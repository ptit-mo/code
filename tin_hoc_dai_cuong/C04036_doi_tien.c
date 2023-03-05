#include <stdio.h>
void exchange(int amount)
{
	int opts[10] = {1, 2, 5, 10, 20, 50, 100, 200, 500, 1000};
	int min = amount;
	int newAmount = amount;
	for (int startMax = 9; startMax >= 0; startMax--)
	{
		int count = 0;
		if (newAmount >= opts[startMax])
		{
			for (int i = startMax; i >= 0; i--)
			{
				while (newAmount >= opts[i])
				{
					newAmount -= opts[i];
					count++;
				}
			}
			if (count != 0 && count < min) {
				min = count;
			}
		}
	}
	printf("%d\n", min);
}
int main()
{
	int numTests;
	scanf("%d", &numTests);
	while (numTests--)
	{
		int amount;
		scanf("%d", &amount);
		exchange(amount);
	}
}