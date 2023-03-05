#!/usr/bin/python3


res = []
def backtrackBinary(str,left):
    if left == 0:
        res.append(str)
        return 
    for b in [ '0', '1' ]:
        backtrackBinary(str + b, left-1)


ln = int(input())
backtrackBinary('', ln//2)

for str in res:
    left = ' '.join(str)
    right = left[::-1]
    if (ln % 2) == 0:
        print(left+ ' ' +right)
    else:
        print(left+' 0 '+right)
        print(left+' 1 '+right)


