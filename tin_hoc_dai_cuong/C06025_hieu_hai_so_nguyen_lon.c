#include <stdio.h>
#include <string.h>
void print(char *bigNum, int n)
{
	int i;
	/* find first non-0 byte, starting at the highest "digit" */
	for (i = 0; i <= n; ++i)
		if (bigNum[i] != 0 + '0')
			break;

	if (i > n) {
		i = n;
	}
	for (; i <= n; i++)
	{
		if (bigNum[i] != ' ')
			printf("%c", bigNum[i]);
	}
	printf("\n");
}
void sub(char *biggerNum, char *smallerNum)
{
	int biggerLen = strlen(biggerNum) - 1;
	char res[biggerLen];
	int smallerLen = strlen(smallerNum) - 1;
	int borrow = 0;
	// printf("biggerLen %d smallerLen %d\n", biggerLen, smallerLen);
	for (int index = biggerLen - 1; index >= 0; index--)
	{
		int bDigit = biggerNum[index] - '0';
		int sDigit = 0;
		if (smallerLen - 1 >= 0)
		{
			sDigit = smallerNum[smallerLen - 1] - '0';
			smallerLen--;
		}
		int diffDigit = bDigit - sDigit - borrow;
		// printf("b4 bDigit %d sDigit %d  diffDigit %d borrow %d smallerLen %d index %d ", bDigit, sDigit, diffDigit, borrow, smallerLen, index);
		if (diffDigit < 0)
		{
			diffDigit = bDigit + 10 - sDigit - borrow;
			borrow = 1;
		}
		else
		{
			borrow = 0;
		}
		// printf("af bDigit %d sDigit %d  diffDigit %d borrow %d smallerLen %d index %d\n", bDigit, sDigit, diffDigit, borrow, smallerLen, index);
		res[index] = diffDigit % 10 + '0';
	}
	print(res, biggerLen - 1);
}
void main()
{
	int numTests;
	scanf("%d\n", &numTests);
	while (numTests--)
	{
		char a[1000], b[1000];
		fgets(a, sizeof(a), stdin);
		fgets(b, sizeof(b), stdin);
		int lenA = strlen(a);
		int lenB = strlen(b);
		if ((lenA > lenB) || (lenA == lenB && strcmp(a, b) == 1))
		{
			sub(a, b);
			continue;
		}
		sub(b, a);
	}
}