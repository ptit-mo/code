#!/usr/bin/python3
# Cho số nguyên dương N và K. Hãy tính NK modulo 109+7.
# Input:
# Dòng đầu tiên là số lượng bộ test T (T ≤ 20).
# Mỗi test gồm 1 số nguyên N và K (1 ≤ N ≤ 1000, 1 ≤ K ≤ 109).
# Output: 
# Với mỗi test, in ra đáp án trên một dòng.
# Ví dụ:
# Input:
# 2
# 2 3
# 4 2
# Output
# 8
# 16

toMod = int(1e9 + 7)
def pow(base: int, expo: int) -> int:
    if expo == 0:
        return 1
    if expo == 1:
        return base
    tmp = pow(base, expo//2) %toMod
    if expo % 2 == 1:
        return (base * tmp * tmp)% toMod
    return (tmp * tmp)% toMod

def main():
    for _ in range(int(input())):
        base, expo = [int(x) for x in input().split(maxsplit=2)]
        print(pow(base, expo))
        
main()