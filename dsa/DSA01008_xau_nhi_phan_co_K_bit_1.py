#!/usr/bin/python3

# input:
#     tests
#     len_arr1 num_bit_1_in_arr1
#     len_arr2 num_bit_1_in_arr2
#     ...
def main():
    for _ in range(int(input())):
        ln,num1 = [int(x) for x in input().split()]
        res = []
        def backtrack(cur,num1):
            if len(cur) == ln:
                res.append(cur)
                return
            choices = ['0','1']
            if num1 == 0:
                choices = ['0']
            if ln - len(cur) == num1:
                choices = ['1']
            for i in choices:
                backtrack(cur+ i,num1-1 if i == '1' else num1)
        backtrack("",num1)
        for val in res:
            print(val)

main()