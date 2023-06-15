# Cho N  số nguyên dương tạo thành dãy A = {A1, A2, ..., AN}. Tìm ra một dãy con
# của dãy A(không nhất thiết là các phần tử liên tiếp trong dãy) có tổng bằng S
# cho trước.
# Input: Dòng đầu ghi số bộ test T(T < 10).  Mỗi bộ test có hai dòng, dòng đầu
# tiên ghi hai số nguyên dương N và S(0 < N ≤ 200) và S(0 < S ≤ 40000). Dòng
# tiếp theo lần lượt ghi N số hạng của dãy A là các số A1, A2, ..., AN(0 < Ai ≤ 200).
# Output:  Với mỗi bộ test, nếu bài toán vô nghiệm thì in ra “NO”, ngược lại in
# ra “YES”
# Ví dụ:
# Input
# Output
# 2
# 5 6
# 1 2 4 3 5
# 10 15
# 2 2 2 2 2 2 2 2 2 2
# YES
# NO

# https://www.geeksforgeeks.org/subset-sum-problem-dp-25/
def main():
    for _ in range(int(input())):
        ln, target = [int(x) for x in input().split()]
        arr = [int(x) for x in input().split(maxsplit=ln)]
        tab = [[False for _ in range(0, target+1)] for _ in range(ln)]
        # if target = 0, we always have an empty subset to make sum 0, so 0 is always True
        for i in range(ln):
            tab[i][0] = True
        # we go bottom up to see if arr has a subset whose sum = s for s in range [1, target]
        for n in range(ln):
            cur = arr[n]
            for i in range(1, target+1):
                # we can always have a subset [A] to make sum A
                if i == cur:
                    tab[n][i] = True
                elif n > 0:
                    if i < cur:
                        # has any prev subarray had a subset of sum i?
                        tab[n][i] = tab[n-1][i]
                    else:
                        # target sum i is bigger than cur, did prev subarray have a
                        # subset of sum i - cur (so we can plus with cur to make i)
                        tab[n][i] = tab[n-1][i-cur]
        print("YES" if tab[-1][-1] else "NO")


main()
