#include <stdio.h>

int main() {
	int rows, cols;
	scanf("%d %d", &rows, &cols);
	int matt[rows][cols];
	for (int r = 0; r < rows; r++) {
		for (int c = 0; c < cols; c++) {
			scanf("%d", &matt[r][c]);
		}
	}
	int target1, target2;
	scanf("%d %d", &target1, &target2);
	for (int r = 0; r < rows; r++) {
		int row = r + 1;
		if (row == target1) row = target2;
		else if (row == target2) row = target1;
		for (int c = 0; c < cols; c++) {
			printf("%d ", matt[row - 1][c]);
		}
		printf("\n");
	}
}