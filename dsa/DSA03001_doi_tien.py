#!/usr/bin/python3
# Tại ngân hàng có các mệnh giá bằng 1, 2, 5, 10, 20, 50, 100, 200, 500, 1000. Tổng số tiền cần đổi có giá trị bằng N.  Hãy xác định xem có ít nhất bao nhiêu tờ tiền sau khi đổi tiền?
# Input:
# Dòng đầu tiên là số lượng bộ test T (T ≤ 50).  Mỗi test gồm 1 số nguyên N ( 1 ≤ N ≤ 100 000).
# Output:  Với mỗi test, in ra đáp án trên một dòng.
# Ví dụ:
# Input:
# 2
# 70
# 121
# Output
# 2
# 3

def main():
    choices = [1, 2, 5, 10, 20, 50, 100, 200, 500, 1000]
    for _ in range(int(input())):
        target = int(input())
        res = 0
        for choice in reversed(choices):
            while target >= choice:
                target -= choice
                res+=1
        print(res)
main()