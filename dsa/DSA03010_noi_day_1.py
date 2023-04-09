# Cho N sợi dây với độ dài khác nhau được lưu trong mảng A[]. Nhiệm vụ của bạn là nối N sợi dây thành một sợi sao cho tổng chi phí nối dây là nhỏ nhất. Biết chi phí nối sợi dây thứ i và sợi dây thứ j là tổng độ dài hai sợi dây A[i] và A[j].
# Input:
# Dòng đầu tiên đưa vào số lượng bộ test T.
# Những dòng kế tiếp đưa vào các bộ test. Mỗi bộ test gồm hai dòng: dòng thứ nhất đưa vào số lượng sợi dây N; dòng tiếp theo đưa vào N số A[i] là độ dài của các sợi dây; các số được viết cách nhau một vài khoảng trống.
# T, N, A[i] thỏa mãn ràng buộc: 1≤T≤100;  1≤N≤106; 0≤A[i]≤106.
# Output:
# Đưa ra kết quả mỗi test theo từng dòng.
# Ví dụ:
# Input
# 2
# 4
# 4 3 2 6
# 5
# 4 2 7 6 9
# Output
# 29
# 62
from queue import PriorityQueue

tests = int(input())
for _ in range(tests):
	ln = int(input())
	queue = PriorityQueue()
	for x in input().split(maxsplit=ln):
		queue.put(int(x))
	res = 0
	while queue._qsize() > 1:
		min1, min2 = queue.get(), queue.get()
		val = min1 + min2
		res += val
		queue.put(val)
		# print(min1, min2, res)
	print(res)

  