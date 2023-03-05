#include <stdio.h>
#include <math.h>
int main()
{
	int height, num, width;
	scanf("%d", &num);
	height = width = num * 2 - 1;
	int bottom = 0;
	int a[height][height];
	while (height >= bottom)
	{
		for (int i = bottom; i < height; i++) {
			for (int j = bottom; j < height; j++) {
				a[i][j] = num - bottom;
			}
		}
		bottom++;
		height--;
	}
	for (int i = 0; i < width; i++)
	{
		for (int j = 0; j < width; j++)
			printf("%d", a[i][j]);
		printf("\n");
	}
}
// explanation
/*
          fill outer in. 
          <<<<<^^^^^>>>>>
          <<<<<^^^^^>>>>>
          <<<<<+++++>>>>>
          <<<<<vvvvv>>>>>
          <<<<<vvvvv>>>>>
*/
/*
num=4 => height = 7;
start filling outer in, keeping height and low outmost, then shrinking (collapsing) filling using num - low
1st round: filler=4 (num(4)-low(0)=4), height=7, low=0, all square is 4
4444444
4444444
4444444
4444444
4444444
4444444
4444444
2nd round: filler=3 (num(4)-low(1)=3), height=5, low=1, inner square is 3
4444444
4333334
4333334
4333334
4333334
4333334
4444444
3rd round: filler=2 (num(4)-low(2)=2) height=3, low=2, inner square is 2
4444444
4333334
4322234
4322234
4322234
4333334
4444444
4th round: filler=1 (num(4)-low(3)=1) height=1, low=3, inner square is 1
4444444
4333334
4322234
4322234
4322234
4333334
4444444
*/