#!/usr/bin/python3

num = int(input())

def replaceStrIndexWith(str, indx, char):
    return str[:indx] + char + str[indx+1:]
for i in range (num):
    line = input()
    ln = len(line) - 1
    while ln >= 0 and line[ln] == '0':
        line = replaceStrIndexWith(line, ln, '1')
        ln -= 1
    if ln >=0 and line[ln] == '1':
        line = replaceStrIndexWith(line, ln, '0')
    print(line)
