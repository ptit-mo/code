# Trường học X có N sinh viên, trong đó có M cặp là bạn bè của nhau.
# Bạn của bạn cũng là bạn, tức là nếu A là bạn của B, B là bạn của C
# thì A và C cũng là bạn bè của nhau.
# Các bạn hãy xác định xem số lượng sinh viên nhiều nhất trong một nhóm
# bạn là bao nhiêu?
# Input:
# Dòng đầu tiên là số lượng bộ test T(T ≤ 20).
# Mỗi test bắt đầu bởi 2 số nguyên N và M(N, M ≤ 100 000).
# M dòng tiếp theo, mỗi dòng gồm 2 số nguyên u, v(u  # v) cho
# biết sinh viên u là bạn của sinh viên v.
# Output:
# Với mỗi test, in ra đáp án tìm được trên một dòng.
# Ví dụ:
# Input:
# 2
# 3 2
# 1 2
# 2 3
# 10 12
# 1 2
# 3 1
# 3 4
# 5 4
# 3 5
# 4 6
# 5 2
# 2 1
# 7 1
# 1 2
# 9 10
# 8 9
# Output
# 3
# 7


def Find(u: int, parent: list) -> int:
    if u != parent[u]:
        u = Find(parent[u], parent)
    return parent[u]


def Union(u: int, v: int, ln: list, parent: list) -> int:
    shorter, longer = Find(u, parent), Find(v, parent)
    if shorter == longer:
        return 0
    if ln[longer] < ln[shorter]:
        shorter, longer = longer, shorter  # make sure shorter is always < longer
    parent[shorter] = longer
    ln[longer] += ln[shorter]
    return ln[longer]


def main():
    for _ in range(int(input())):
        sodinh, socanh = [int(x) for x in input().split()]
        parent = [0]*(sodinh+1)
        for i, _ in enumerate(parent):
            parent[i] = i
        ln = [1]*(sodinh+1)
        curMax = 0
        for _ in range(socanh):
            u, v = [int(x) for x in input().split()]
            curMax = max(curMax, Union(u, v, ln, parent))
        print(curMax)


main()
