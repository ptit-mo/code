#!/usr/bin/python3

# Cho một hoán vị của N số nguyên dương đầu tiên.
# Hãy xác định xem đó là hoán vị thứ bao nhiêu nếu liệt kê theo thứ tự tăng dần (tính từ 1).
# Input
# Dòng đầu ghi số T là số bộ test (T < 10)
# Mỗi bộ test gồm 2 dòng
# Dòng đầu ghi số nguyên dương N (3 < N < 10)
# Dòng tiếp theo ghi một hoán vị của các số nguyên dương từ 1 đến N.  
# Output
# Với mỗi bộ test, ghi ra trên một dòng số thứ tự của hoán vị (tính từ 1, theo thứ tự liệt kê tăng dần).
# Ví dụ
# Input
# 2
# 4
# 1 4 3 2
# 4
# 1 2 3 4
# Output
# 6
# 1
def checkPermutationOrder():
    ln  = int(input())
    line = [int(x) for x in input().split(maxsplit=ln)]
    visited = set()
    cnt = 0
    def backtrack(cur,found):
        if found:
            return
        nonlocal cnt
        # print(cur,found)
        if len(cur) == ln:
            cnt += 1
            if cur == line:
                found = True
                print(cnt)
                return
        for i in range(1,ln+1):
            if i in visited:
                continue
            visited.add(i)
            backtrack(cur + [i],found)
            visited.remove(i)
    backtrack([],False)
    
def main():
    for _ in range (int(input())):
        checkPermutationOrder()

main()