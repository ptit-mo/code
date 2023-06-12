# Cho dãy số A[] gồm n số nguyên dương. Tam giác đặc biệt của dãy số A[] là tam 
# giác được tạo ra bởi n hàng, trong đó hàng thứ n là dãy số A[], hàng i là tổng
# hai phần tử liên tiếp của hàng i+1 (1≤i≤n-1). Ví dụ A[] = {1, 2, 3, 4, 5}, khi
# đó tam giác được tạo nên như dưới đây:
# [48]
# [20, 28]
# [8, 12, 16]     
# [3, 5, 7, 9 ]
# [1, 2, 3, 4, 5 ]
# Input:
# Dòng đầu tiên đưa vào số lượng bộ test T.
# Những dòng tiếp theo đưa vào các bộ test. Mỗi bộ test gồm hai dòng: dòng thứ 
# nhất đưa vào N là số lượng phần tử của dãy số A[]; dòng tiếp theo đưa vào N số
# của mảng A[].
# T, N, A[i] thỏa mãn ràng buộc: 1≤T≤100; 1≤N, A[i] ≤10;
# Output:
# Đưa ra kết quả mỗi test theo từng dòng. Mỗi dòng của tam giác tổng được bao 
# bởi ký tự [, ].
# Input
# 1
# 5
# 1 2 3 4 5
# Output
# [48] [20 28] [8 12 16] [3 5 7 9 ] [1 2 3 4 5 ]

def main():
  for _ in range(int(input())):
    _ = input()
    base = [int(x) for x in input().split()]
    buildTriangle(base)

def buildTriangle(base: list):
  res = [base]
  maxHeight = len(base) - 1
  for i in reversed(range(maxHeight)):
    cur = [0] * (i+1)
    for i in range(1, len(base)):
      cur[i-1] = base[i] + base[i-1]
    res.append(cur)
    base = cur
  s = ''
  for level in reversed(res):
    s += f"[{' '.join(str(x) for x in level)}] "
  print(s)
    
    
main()