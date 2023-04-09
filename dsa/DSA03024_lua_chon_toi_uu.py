# Bạn được giao cho N công việc, công việc thứ i có thời gian bắt đầu là A[i] và kết thúc tại B[i]. Tại một thời điểm, bạn chỉ có thể làm một công việc.
# Bạn hãy lựa chọn các công việc một cách tối ưu sao cho số công việc làm được là nhiều nhất.
# Input: Dòng đầu tiên là số lượng bộ test T (T ≤ 10).
# Mỗi test gồm 1 số nguyên N ( 1 ≤ N ≤ 100 000).
# N dòng tiếp theo, mỗi dòng gồm 2 số A[i] và B[i] (0 ≤ A[i] < B[i] ≤ 106).
# Output:  Với mỗi test, in ra đáp án trên một dòng.
# Ví dụ:
# Input
# 1
# 6
# 5 9
# 1 2
# 3 4
# 0 6
# 5 7
# 8 9
# Output
# 4

tests = int(input())
for _ in range(tests):
	count = int(input())
	times = []
	for i in range(count):
		times.append([int(x) for x in input().split(maxsplit=2)])
	times.sort(key=lambda x:x[1])
	res = []
	for i, f in enumerate(times):
		if len(res) == 0:
			res.append(f)
		else:
			if f[0] >= res[-1][1]:
				res.append(f)
	print(len(res))