#!/usr/bin/python3
# Một xâu nhị phân độ dài n được gọi là thuận nghịch hay đối xứng nếu đảo ngược 
# xâu nhị phân đó ta vẫn nhận được chính nó. Cho số tự nhiên n (n nhập từ bàn phím). 
# Hãy viết chương trình liệt kê tất cả các xâu nhị phân thuận nghịch có độ dài n.  
# Hai phần tử khác nhau của xâu thuận nghịch được ghi cách nhau một khoảng trống.
# Ví dụ với n = 4 ta tìm được 4 xâu nhị phân thuận nghịch như dưới đây.
# 0 0 0 0         
# 0 1 1 0         
# 1 0 0 1         
# 1 1 1 1
# Ví dụ
# Input
# 4	
# Output
# 0 0 0 0
# 0 1 1 0
# 1 0 0 1
# 1 1 1 1

res = []
def backtrackBinary(str,left):
    if left == 0:
        res.append(str)
        return 
    for b in [ '0', '1' ]:
        backtrackBinary(str + b, left-1)


ln = int(input())
backtrackBinary('', ln//2)

for str in res:
    left = ' '.join(str)
    right = left[::-1]
    if (ln % 2) == 0:
        print(left+ ' ' +right)
    else:
        print(left+' 0 '+right)
        print(left+' 1 '+right)


