#include <stdio.h>

void main() {
	int numTests;
	scanf("%d", &numTests);
	int num = 0;
	while (numTests--) {
		char op[3];
		scanf("%s", op);
		if (op[0] == '-' || op[2] == '-') {
			num --;
		} else {
			num++;
		}
	}
	printf("%d", num);
}