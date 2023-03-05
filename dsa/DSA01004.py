#!/usr/bin/python3

tests = int(input())


for i in range(tests):
    res = []
    maxNum, count = [ int(x) for x in input().split()]
    def backtrack(curStr,start):
        if len(curStr) == count:
            res.append(curStr)
            return
        for i in range(start,maxNum+1):
            backtrack(curStr+str(i),i+1)
    backtrack('',1)
    print(' '.join(res))
