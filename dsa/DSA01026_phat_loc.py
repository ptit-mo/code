#!/usr/bin/python3
# Một xâu ký tự số chỉ bao gồm các chữ số 6 và 8 sẽ được gọi là “phát lộc” nếu thỏa mãn các điều kiện sau:
# Độ dài xâu ít nhất là 6
# Chữ số đầu tiên là chữ số 8, chữ số cuối cùng là chữ số 6
# Không có 2 chữ số 8 nào ở cạnh nhau
# Không có nhiều hơn 3 chữ số 6 ở cạnh nhau.
# Viết chương trình liệt kê các xâu ký tự phát lộc độ dài N theo thứ tự tăng dần.
# Input
# Chỉ có 1 dòng ghi số N (5 < N < 16).
# Output
# Ghi ra các xâu ký tự phát lộc độ dài N, mỗi xâu trên một dòng.
# Ví dụ
# Input
# 6
# Output
# 866686
# 866866
# 868666
# 868686

def main():
    ln = int(input())
    if ln < 6:
        return
    def backtrack(cur):
        if len(cur) == ln:
            print(cur)
            return
        choices = ['6','8']
        if len(cur) == 0 or (len(cur) >= 3 and cur[-3:] == '666'):
            choices = ['8']
        elif len(cur) == ln-1 or cur[-1] == '8':
            choices = ['6']
        for i in choices:
            backtrack(cur + i)
    backtrack("")
main()