#!/usr/bin/python3

tests = int(input())

def calNumberOfListsSumEqualTarget(n: int) -> int:
    if n <= 1:
        return n
    return calNumberOfListsSumEqualTarget(n-1)+1

for i in range(tests):
    num = int(input())
    print(calNumberOfListsSumEqualTarget(num))