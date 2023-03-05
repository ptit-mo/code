#include <stdio.h>
#include <math.h>
void swap(int *a, int *b)
{
	int tmp;
	tmp = *a;
	*a = *b;
	*b = tmp;
}
int main()
{
	int n;
	scanf("%d", &n);
	int T[n], D[n];
	for (int i = 0; i < n; i++)
		scanf("%d %d", &T[i], &D[i]);
	int time = 0;
	for (int i = 0; i < n - 1; i++)
		for (int j = i + 1; j < n; j++)
			if (T[j] < T[i])
			{
				swap(&D[i], &D[j]);
				swap(&T[i], &T[j]);
			}
	for (int i = 0; i < n; i++)
		time = fmax(time, T[i]) + D[i];
	printf("%d", time);
}
// don't know why it doesn't work
// #include <stdio.h>

// struct Info {
// 	long start;
// 	long time;
// };
// void sortBystart(struct Info arr[], int size) {
// 	for (int i =0; i< size - 1; i++) {
// 		for (int j=1; j < size; j++) {
// 			if (arr[i].start > arr[j].start) {
// 				long temp = arr[i].start;
// 				arr[i].start = arr[j].start;
// 				arr[j].start = temp;
// 			}
// 		}
// 	}
// 	// for (int i = 0; i < size; i++) {
// 	// 	printf("%d %d\n", arr[i].start, arr[i].time);
// 	// }
// }
// void main() {
// 	int count;
// 	scanf("%d", &count);
// 	struct Info arr[count];
// 	for (int i = 0; i < count; i++) {
// 		scanf("%ld %ld", &arr[i].start, &arr[i].time);
// 	}
// 	sortBystart(arr, count);
// 	long res = 0;
// 	for (int i = 0; i < count; i++) {
// 		if (arr[i].start > res) {
// 			res = arr[i].start;
// 		}
// 		res += arr[i].time;
// 	}
// 	printf("%ld\n", res);
// }