# Cho một dãy số nguyên gồm N phần tử A[1], A[2], ... A[N].
# Biết rằng dãy con tăng là 1 dãy A[i1],... A[ik]
# thỏa mãn i1 < i2 < ... < ik và A[i1] < A[i2] < .. < A[ik].
# Hãy cho biết dãy con tăng dài nhất của dãy này có bao nhiêu phần tử?
# Input: Dòng 1 gồm 1 số nguyên là số N (1 ≤ N ≤ 1000). Dòng thứ 2 ghi N số nguyên A[1], A[2], .. A[N] (1 ≤ A[i] ≤ 1000).
# Output: Ghi ra độ dài của dãy con tăng dài nhất.
# Ví dụ:
# Input
# 6
# 1 2 5 4 6 2
# Output
# 4

def main():
    cnt = int(input())
    arr = [int(x) for x in input().split(maxsplit=cnt)]
    maxFromHeadToIndex = [1 for _ in range(cnt)]
    res = 1
    for i in range(cnt):
        if i == 0:
            continue
        for j in range(0, i):
            if arr[j] < arr[i]:
                maxFromHeadToIndex[i] = max(
                    maxFromHeadToIndex[i], maxFromHeadToIndex[j] + 1)
                res = max(res, maxFromHeadToIndex[i])
    print(res)


main()
