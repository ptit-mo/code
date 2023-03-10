# Cho mảng A[] gồm N phần tử chỉ bao gồm các số 0 và 1. Các số 0 được đặt trước các số 1. Hãy đếm các số 0 với thời gian log(N).
# Input:
# Dòng đầu tiên đưa vào số lượng bộ test T.
# Những dòng kế tiếp đưa vào các bộ test. Mỗi bộ test gồm 2 dòng: dòng thứ nhất đưa vào số N; dòng tiếp theo đưa vào N số của mảng A[]; các số được viết cách nhau một vài khoảng trống.
# T, N, A[i] thỏa mãn ràng buộc: 1≤T≤100;  1≤ N≤1000; 0≤ A[i]≤1.
# Output:
# Đưa ra kết quả mỗi test theo từng dòng.
#  Ví dụ:
# Input
# 3
# 12
# 0 0 0 0 0 0 0 0 0 1 1 1 
# 5
# 0 0 0 0 0
# 6
# 1 1 1 1 1 1
# Output
# 9
# 5
# 0

tests = int(input())

def count0s(arr: list) -> int:
    ln = len(arr)
    if ln == 1:
        if arr[0] == 0:
            return 1
        return 0
    mid = arr[ln//2]
    if mid == 0:
        return ln//2 + count0s(arr[ln//2:])
    return count0s(arr[:ln//2])

for i in range(tests):
    ln = int(input())
    arr = [int(x) for x in input().split(maxsplit=ln)]
    print(count0s(arr))
    