#!/usr/bin/python3

def replaceStrIndexWith(str, indx, char):
    return str[:indx] + char + str[indx+1:]

count = int(input())

for i in range(count):
    str = input()
    cur = len(str) - 1
    while str[cur] == '1' and cur >= 0:
        str = replaceStrIndexWith(str, cur, '0')
        cur -= 1
    if cur >=0:
        str = replaceStrIndexWith(str, cur, '1')
    print(str)


