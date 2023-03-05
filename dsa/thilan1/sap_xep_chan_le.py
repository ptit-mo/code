#!/usr/bin/python3

ln = int(input())

nums = [int(x) for x in input().split(maxsplit=ln)]

odd, even = [], []

for i in nums:
    if i % 2 == 0:
        even.append(i)
    else:
        odd.append(i)

even.sort()
odd.sort(reverse=True)

ep, op = 0, 0

for (idx, num) in enumerate(nums):
    if num%2 == 0:
        nums[idx] = even[ep]
        ep += 1
    else:
        nums[idx] = odd[op]
        op += 1

print(' '.join([str(x) for x in nums]))
