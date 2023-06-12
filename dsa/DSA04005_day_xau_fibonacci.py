#!/usr/bin/python3

# Một dãy xâu ký tự G chỉ bao gồm các chữ cái A và B được gọi là dãy xâu Fibonacci nếu thỏa mãn tính chất:    G(1) = A; G(2) = B; G(n) = G(n-2)+G(n-1). Với phép cộng (+) là phép nối hai xâu với nhau.  Bài toán đặt ra là tìm ký tự ở vị trí thứ i (tính từ 1) của xâu Fibonacci thứ n.
# Dữ liệu vào: Dòng 1 ghi số bộ test. Mỗi bộ test ghi trên một dòng 2 số nguyên N và i (1<N<93). Số i đảm bảo trong phạm vi của xâu G(N) và không quá 18 chữ số. Kết quả: Ghi ra màn hình kết quả tương ứng với từng bộ test.
# Input
# 2
# 6 4
# 8 19
# Output
# A
# B

def findKInFibN():
    # https://www.youtube.com/watch?v=k8OTyO46tbQ&ab_channel=V%C5%A9Th%C3%A0nhC%C3%B4ng
    n, k = [int(x) for x in input().split()]
    length = [0] * (n+1)
    length[1] = 1
    for i in range(2,n+1):
        length[i] = length[i-2] + length[i-1]
    # we are finding k in Gn
    # Gn = Gn-2 + Gn-1
    # if k <= Gn-2 -> k is in Gn-2, we can find k there
    # else k is in Gn-1, at position (k-G(n-2)) of Gn-1
    # recursively we can subtract until n == 1 or n == 2
    while (n > 2):
        if k <= length[n-2]:
            n -= 2 # we find in Gn-2 instead
        else:
            k -= length[n-2] # we find in this position of Gn-1 instead
            n -= 1
    if n == 1:
        print('A')
    else:
        print('B')

def main():
    for _ in range(int(input())):
        findKInFibN()
        
main()