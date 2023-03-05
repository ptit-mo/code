#include <stdio.h>
#include <string.h>
int main()
{
	int t;
	scanf("%d", &t);
	while (t--)
	{
		int count = 0;
		int even = 0, odd = 0;
		char separator = ' ';
		while (separator == ' ')
		{
			int x;
			scanf("%d", &x);
			count++;
			if (x % 2 == 0)
				even++;
			else
				odd++;
			separator = getchar();
		}
		if ((count % 2 == 0 && even > odd) || (count % 2 != 0) && odd > even)
		{
			printf("YES\n");
		}
		else
			printf("NO\n");
	}
}