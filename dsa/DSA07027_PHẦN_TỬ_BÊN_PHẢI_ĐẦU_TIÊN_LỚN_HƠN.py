# Cho dãy số A[] gồm N phần tử. Với mỗi A[i], bạn cần tìm phần tử bên phải đầu tiên lớn hơn nó. Nếu không tồn tại, in ra - 1.
# Input:
# Dòng đầu tiên là số lượng bộ test T(T ≤ 20).
# Mỗi test bắt đầu bởi số nguyên N(1 ≤ N ≤ 100000).
# Dòng tiếp theo gồm N số nguyên A[i](0 ≤ A[i] ≤ 109).
# Output:
# Với mỗi test, in ra trên một dòng N số R[i], với R[i] là giá trị phần tử đầu tiên lớn hơn A[i].
# Ví dụ
# Input
# 3
# 4
# 4 5 2 25
# 3
# 2 2 2
# 4
# 4 4 5 5
# Output
# 5 25 25 - 1
# -1 - 1 - 1
# 5 5 - 1 - 1

def findFirstBiggerNumOnTheRight(arr: list):
    stack = []
    ln = len(arr)
    res = [-1]*ln
    for i in reversed(range(0, ln)):
        while len(stack) > 0 and arr[i] >= stack[-1]:
            stack.pop()
        if len(stack) > 0:
            res[i] = stack[-1]
        stack.append(arr[i])
    print(" ".join(str(x) for x in res))


for _ in range(int(input())):
    input()
    arr = [int(x) for x in input().split()]
    findFirstBiggerNumOnTheRight(arr)
