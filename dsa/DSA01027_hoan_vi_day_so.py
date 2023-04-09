# Cho dãy số A[] có N phần tử là các số nguyên dương khác nhau từng đôi một. Hãy liệt kê tất cả các hoán vị của dãy số A[] theo thứ tự tăng dần, tức là hoán vị đầu tiên có giá trị tăng dần từ trái qua phải, hoán vị cuối cùng giảm dần từ trái qua phải.
# Input
# Dòng đầu ghi số N(1 < N < 9)
# Dòng thứ 2 ghi N số của dãy A[](0 < A[i] < 10000)
# Output
# Ghi mỗi hoán vị của dãy số trên một dòng
# Ví dụ
# Input
# 3
# Output
# 77 88 99
# 77 99 88
# 88 77 99
# 88 99 77
# 99 77 88
# 99 88 77

def permute(arr: list):
    def backtrack(cur: list, visited: set):
        if len(visited) == len(arr):
            print(" ".join([str(x) for x in cur]))
            return
        for choice in arr:
            if choice not in visited:
                visited.add(choice)
                backtrack(cur+[choice], visited)
                visited.remove(choice)
    backtrack([], set())


def main():
    _ = input()
    arr = sorted([int(x) for x in input().split()])
    permute(arr)


main()
