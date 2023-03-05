#include <stdio.h>

void solve(long num) {
	long res = 0;
	int i = 1;
	while (i <= num/i) {
		if (num %i == 0) {
			if (i % 2 == 0) res++;
			if (i != num/i && num/i %2 == 0) res++;
		}
		i++;
	}
	printf("%ld\n", res);
}
void main() {
	int numTests;
	scanf("%d", &numTests);
	while(numTests--) {
		long num;
		scanf("%ld", &num);
		solve(num);
	}
}