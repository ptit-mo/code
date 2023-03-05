#!/usr/bin/python3

tests = int(input())

for i in range(tests):
    maxNum, count = [ int(x) for x in input().split()]
    nums = [ int(x) for x in input().split(maxsplit=count)]
    cur = count - 1
    while nums[cur] >= maxNum and cur >= 0:
        cur -= 1
        maxNum -= 1
    if cur < 0:
        nums = range(1,count+1)
    else:
        nums[cur] += 1
        for i in range(cur+1, count):
            nums[i] = nums[i-1]+1
    print(' '.join([str(x) for x in nums]))
