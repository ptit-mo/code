#!/usr/bin/python3

#maxSumArrLenN = E(Arr[i]*i | i ∈ [0,N))
def calMaxSum(arr: list) -> int:
    arr.sort()
    maxSum = 0
    for a,b in enumerate(arr):
        maxSum = int((maxSum + a*b)%(1e9 + 7))
    return maxSum
    
def main():
    for _ in range (int(input())):
        cnt = int(input())
        arr = [int(x) for x in input().split(maxsplit=cnt)]
        print(calMaxSum(arr))

main()