#!/usr/bin/python3

tests = int(input())

for i in range(tests):
    count = int(input())
    nums = [ int(x) for x in input().split(maxsplit=count)]
    pivot = count - 2
    while pivot >= 0 and nums[pivot] > nums[pivot+1]:
        pivot -= 1
    if pivot < 0:
        nums = range(1,count+1)
    else:
        cur = count - 1
        while cur > pivot and nums[cur] < nums[pivot]:
            cur -= 1
        nums[cur], nums[pivot] = nums[pivot], nums[cur]
        nums[pivot+1:] = sorted(nums[pivot+1:])
    print(' '.join([str(x) for x in nums]))
