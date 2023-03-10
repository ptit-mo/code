#!/usr/bin/python3

toMod = 1e9 + 7
def pow(base: int, expo: int) -> int:
    if expo == 0:
        return base
    tmp = pow(base, expo//2) %toMod
    if expo % 2 == 1:
        return int((base * tmp * tmp)% toMod)
    return int((tmp * tmp)% toMod)

def main():
    for _ in range(int(input())):
        base, expo = [int(x) for x in input().split(maxsplit=2)]
        print(pow(base, expo))
        
main()