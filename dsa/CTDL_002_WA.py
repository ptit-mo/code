#!/usr/bin/python3

res = []
count, target = [int(x) for x in input().split()]
nums = [int(x) for x in input().split(maxsplit=count)]
ln = len(nums)

visited = set()
def backtrackSum(curSet=[], target=0, startIdx = 0):
    if target < 0 or startIdx > ln:
        return
    if target == 0:
        if len(curSet) > 0:
            res.append(curSet)
        return
    for idx, num in enumerate(nums): 
        if idx < startIdx:
            continue
        if not idx in visited:
            visited.add(idx)
            backtrackSum(curSet + [num],target-num, idx+1)
            visited.remove(idx)

backtrackSum([], target)
for arr in res:
    print(' '.join([str(x) for x in arr]))
print(len(res))
