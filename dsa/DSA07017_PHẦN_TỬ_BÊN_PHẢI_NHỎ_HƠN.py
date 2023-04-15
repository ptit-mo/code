# Cho mảng A[] gồm n phần tử. Hãy đưa ra các phần tử nhỏ hơn tiếp theo của phần tử lớn hơn đầu tiên phần tử hiện tại. Nếu phần tử hiện tại không có phần tử lớn hơn tiếp theo ta xem là - 1. Nếu phần tử không có phần tử nhỏ hơn tiếp theo ta cũng xem là - 1. Ví dụ với mảng A[] = {5, 1, 9, 2, 5, 1, 7} ta có kết quả là ans = {2, 2, -1, 1, -1, -1, -1} vì:
# Next Greater                         Right Smaller
# 5 -> 9                                        9 -> 2
# 1 -> 9                                        9 -> 2
# 9 -> -1 - 1 -> -1
# 2 -> 5                                         5 -> 1
# 5 -> 7                                         7 -> -1
# 1 -> 7                                        7 -> -1
# 7 -> -1                                       7 -> -1
# Input:
# Dòng đầu tiên đưa vào số lượng bộ test T
# Những dòng tiếp theo mỗi dòng đưa vào một bộ test. Mỗi bộ test gồm hai dòng: dòng thứ nhất đưa vào n là số phần tử của mảng A[], dòng tiếp theo đưa vào n số A[i].
# Output:
# Đưa ra kết quả mỗi test theo từng dòng.
# Ràng buộc:
# T, n, A[i] thỏa mãn ràng buộc: 1≤T≤100
# 1≤n, A[i] ≤106.
# Ví dụ:
# Input
# 2
# 7
# 5 1 9 2 5 1 7
# 8
# 4 8 2 1 9 5 6 3
# Output
# 2 2 1 1 - 1 - 1 - 1
# 2 5 5 5 - 1 3 - 1 - 1

# =>find index of first bigger number, then find smaller number on the right of the array
# then map them together

def find(arr: list):
    ln = len(arr)
    biggerNumIndx = [-1] * ln
    stackOfBiggerNumIndx = []
    for i in reversed(range(0, ln)):
        while len(stackOfBiggerNumIndx) > 0 and arr[i] >= arr[stackOfBiggerNumIndx[-1]]:
            stackOfBiggerNumIndx.pop()
        if len(stackOfBiggerNumIndx) > 0:
            biggerNumIndx[i] = stackOfBiggerNumIndx[-1]
        stackOfBiggerNumIndx.append(i)

    smallerNum = [-1] * ln
    stackOfSmallerNum = []
    for i in reversed(range(0, ln)):
        while len(stackOfSmallerNum) > 0 and arr[i] <= stackOfSmallerNum[-1]:
            stackOfSmallerNum.pop()
        if len(stackOfSmallerNum) > 0:
            smallerNum[i] = stackOfSmallerNum[-1]
        stackOfSmallerNum.append(arr[i])

    # print(arr)
    # print(biggerNumIndx)
    # print(smallerNum)
    res = [-1]*ln
    for i in range(0, ln):
        if biggerNumIndx[i] != -1:
            res[i] = smallerNum[biggerNumIndx[i]]
    print(" ".join(str(x) for x in res))


for _ in range(int(input())):
    input()
    find([int(x) for x in input().split()])
