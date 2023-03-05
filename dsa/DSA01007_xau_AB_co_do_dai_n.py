#!/usr/bin/python3

# input:
#     tests
#     len1
#     len2
#     ...
def main():
    for _ in range(int(input())):
        ln = int(input())
        res = []
        def backtrack(cur):
            if len(cur) == ln:
                res.append(cur)
                return
            for i in ['A','B']:
                backtrack(cur+ i)
        backtrack("")
        val = " ".join(res)
        print(f"{val}")

main()