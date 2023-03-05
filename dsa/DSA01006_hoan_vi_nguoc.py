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
        visited = set()
        def backtrack(cur):
            if len(cur) == ln:
                res.append(cur)
                return
            for i in range(ln,0,-1):
                if i in visited:
                    continue
                visited.add(i)
                backtrack(cur+ str(i))
                visited.remove(i)
        backtrack("")
        val = " ".join(res)
        print(f"{val}")

main()