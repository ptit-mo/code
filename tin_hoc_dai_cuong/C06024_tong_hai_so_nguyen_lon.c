#include <stdio.h>
#include <string.h>
void print(char* bigNum, int n)
{
	for (int i = 0; i <= n; i++)
	{
		if (bigNum[i] != ' ')
			printf("%c", bigNum[i]);
	}
	printf("\n");
}
void sum(char* biggerNum, char* smallerNum) {
	int biggerLen = strlen(biggerNum) - 1;
	char res[biggerLen + 1];
	res[0] = ' ';
	int smallerLen = strlen(smallerNum) - 1;
	int remainder = 0;
	// printf("biggerLen %d smallerLen %d\n", biggerLen, smallerLen);
	for (int index = biggerLen - 1; index >= 0; index--) {
		int bDigit = biggerNum[index] - '0';
		int sDigit = 0;
		if (smallerLen -1 >= 0) {
			sDigit = smallerNum[smallerLen - 1] - '0';
			smallerLen--;
		}
		int sumDigits = sDigit + bDigit + remainder;
		res[index+1] = sumDigits % 10 + '0';
		remainder = sumDigits / 10;
		// printf("s %d b %d rc %c\n", sDigit, bDigit, res[index+1]);
	}
	if (remainder > 0) {
		res[0] = remainder + '0';
	}
	print(res, biggerLen);
}
void sumNum(char* a, char* b)
{
	int lenA = strlen(a);
	int lenB = strlen(b);
	if (lenA > lenB) {
		 sum(a, b);
		 return;
	}
	 sum (b, a);
}
int main()
{
	int numTests;
	scanf("%d\n", &numTests);
	while (numTests--)
	{
		char a[1000], b[1000];
		fgets(a, sizeof(a), stdin);
		fgets(b, sizeof(b), stdin);
		sumNum(a, b);
	}
}