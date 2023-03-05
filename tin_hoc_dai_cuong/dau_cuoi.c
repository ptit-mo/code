#include <stdio.h>
#include <string.h>

void main() {
	int numTests;
	scanf("%d", &numTests);
	while (numTests--) {
		char num[20];
		scanf("%s", num);
		int len = strlen(num);
		if (num[0] == num[len-2] && num[1] == num[len-1]) {
			printf("YES\n");
		} else {
			printf("NO\n");
		}
	}
}