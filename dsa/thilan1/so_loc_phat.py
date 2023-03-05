#!/usr/bin/python3

tests = int(input())

for i in range(tests):
    ln = int(input())
    res = []
    def backtrack(cur, left):
        if left == 0:
            res.append(cur)
            return
        for i in ['6','8']:
            backtrack(cur+ i,left-1)
    backtrack("",ln)
    print(len(res))
    print(" ".join(res))
