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

# def fibChainNTab(n: int, tab: list) -> str:
#     while n>2:
#         tab[2] = tab[0] + tab[1]
#         tab[1],tab[0] = tab[2],tab[1]
#         n -= 1
    
#     return tab[2]

def fibChainN(n: int) -> str:
    prev2, prev1, cur = 'A', 'B', ''
    while n>2:
        cur = prev2 + prev1
        prev1, prev2 = cur, prev1
        n -= 1
        # print(n,cur)
    return cur

def main():
    for _ in range(int(input())):
        n, k = [int(x) for x in input().split(maxsplit=2)]
        # print(fibChainNTab(n,['A','B','']))
        print(fibChainN(n)[k-1])
        
main()