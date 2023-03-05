#include <stdio.h>
void calMaxSubArraySum(int *arr, int size) {
	//use sliding window
	long long max, sum;
	max = sum = arr[0];
	int left = 0, right = 1;
	while (right < size) {
		while (sum < 0) {
			sum -= arr[left];
			left++;
		}
		sum += arr[right];
		if (max < sum) {
			max = sum;
		} 
		right++;
	}
	printf("%lld\n", max);

}
int main()
{
	int numTests;
	scanf("%d", &numTests);
	while (numTests--)
	{
		int size;
		scanf("%d", &size);
		int arr[size];
		for (int i = 0; i < size; i++) {
			scanf("%d", &arr[i]);
		}
		calMaxSubArraySum(arr, size);
	}
}