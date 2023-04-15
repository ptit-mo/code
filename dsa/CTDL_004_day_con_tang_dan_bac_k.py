# Cho dãy gồm N số phân biệt AN = {a1, a2, .., aN} và số tự nhiên K(K <= N <= 100). Ta gọi một dãy con tăng dần bậc K của dãy số AN là một dãy các số gồm K phần tử trong dãy đó thỏa mãn tính chất tăng dần. Bài toán được đặt ra là in ra màn hình  số các dãy con tăng dần bậc K của dãy số AN. Ví dụ:
# Input:
# 5    3
# 2    5    15   10    20
# Dòng đầu tiên ghi lại hai số N và K tương ứng với số phần tử của dãy số và bậc của dãy con.
# Dòng kế tiếp: N số của dãy số AN, các số trong dãy không lớn hơn 100.
# thì Output: 7 (số các dãy con tăng dần bậc 3 của dãy số AN)

def isIncrementing(arr: list) -> bool:
    ln = len(arr)
    for idx in range(0, ln):
        if idx == 0:
            continue
        if arr[idx-1] > arr[idx]:
            return False
    return True


def countCombination(arr: list, ln: int) -> int:
    count = 0

    def backtrack(cur: list, head: int):
        nonlocal count
        if len(cur) == ln:
            if isIncrementing(cur):
                count += 1
            return
        for idx in range(head, len(arr)):
            backtrack(cur+[arr[idx]], idx+1)
    backtrack([], 0)
    print(count)


def main():
    _, ln = [int(x) for x in input().split()]
    arr = [int(x) for x in input().split()]
    countCombination(arr, ln)


main()
