# Cho 2 xâu S1 và S2. Hãy tìm xâu con chung dài nhất của 2 xâu này (các phần tử không nhất thiết phải liên tiếp nhau).
# Input: Dòng đầu tiên là số lượng bộ test T (T ≤ 20). Mỗi test gồm hai dòng, mô tả xâu S1 và S2, mỗi xâu có độ dài không quá 1000 và chỉ gồm các chữ cái in hoa.
# Output:  Với mỗi test, in ra độ dài dãy con chung dài nhất trên một dòng.
# Ví dụ:
# Input
# 2
# AGGTAB
# GXTXAYB
# AA
# BB
# Output
# 4
# 0

tests = int(input())

for _ in range(tests):
	x, y = list(input()), list(input())
	rows, cols = len(x)+1, len(y)+1
	matt = [[0] * cols] * rows
	for row in range(1, rows):
		for col in range(1, cols):
			if x[row-1] == y[col-1]:
					matt[row][col] = 1+matt[row-1][col-1]
			else:
					matt[row][col] = max(matt[row][col-1], matt[row-1][col])
	print(matt[-1][-1])


