# Cho mảng đã được sắp xếp A[] gồm N phần tử không có hai phần tử giống nhau và số X. Nhiệm vụ của bạn là tìm floor(X). Trong đó, K=floor(X) là phần tử lớn nhất trong mảng A[] nhỏ hơn hoặc bằng X.
# Input:
# Dòng đầu tiên đưa vào số lượng bộ test T.
# Những dòng kế tiếp đưa vào các bộ test. Mỗi bộ test gồm 2 dòng: dòng thứ nhất đưa vào số N là số phần tử của mảng A[] và số X; dòng tiếp theo đưa vào N số của mảng A[]; các số được viết cách nhau một vài khoảng trống.
# T, N, A[i] thỏa mãn ràng buộc: 1≤T≤100;  1≤ N≤107; 1≤ A[i]≤1018.
# Output:
# Đưa ra vị trí của  floor(X) trong mảng A[] hoặc -1 nếu không tồn tại floor(X) của mỗi test theo từng dòng.
#   Ví dụ:
# Input
# 3
# 7 0
# 1 2 8 10 11 12 19
# 7 5
# 1 2 8 10 11 12 19
# 7 10
# 1 2 8 10 11 12 19
# Output
# -1
# 2
# 4
tests = int(input())

def floorX(arr: list, ln: int, target: int, start: int) -> int:
    if ln == 1:
        if arr[0] <= target:
            return start
        return -1
    mid = arr[ln//2]
    if mid <= target:
        arr = arr[ln//2:]
        newLn = len(arr)
        return floorX(arr, newLn, target, start+(ln - newLn))
    else:
        arr = arr[:ln//2]
        return floorX(arr, len(arr), target, start)

for i in range(tests):
    ln, target = [int(x) for x in input().split(maxsplit=2)]
    arr = [int(x) for x in input().split(maxsplit=ln)]
    print(floorX(arr, ln, target, 1))
    