#!/usr/bin/python3

# input:
#     tests
#     len_arr1
#     len_arr2
#     ...
def main():
    for _ in range(int(input())):
        ln = int(input())
        res = []
        def backtrack(cur):
            if len(cur) == ln:
                res.append(cur)
                return
            choices = ['A','H']
            if len(cur) == 0:
                choices = ['H']
            elif len(cur) == ln-1 or cur[-1] == 'H':
                choices = ['A']
            for i in choices:
                backtrack(cur+ i)
        backtrack("")
        for val in res:
            print(val)

main()