# Cho mảng A[], B[] đều có N phần tử. Nhiệm vụ của bạn là tìm giá trị nhỏ nhất của  biểu thức P = A[0]*B[0] + A[1]*B[1] + ..+A[N-1]*B[N-1] bằng cách tráo đổi vị trí các phần tử của cả mảng A[] và B[].
# Input:
# Dòng đầu tiên đưa vào số lượng bộ test T.
# Những dòng kế tiếp đưa vào các bộ test. Mỗi bộ test gồm 3 dòng: dòng thứ nhất đưa vào số phần tử của mảng N; dòng tiếp theo đưa vào N số A[i]; dòng cuối cùng đưa vào N số B[i] các số được viết cách nhau một vài khoảng trống.
# T, N, A[i], B[i] thỏa mãn ràng buộc: 1≤T≤100;  1≤ N ≤107; 0≤A[i], B[i] ≤1018.
# Output:
# Đưa ra kết quả mỗi test theo từng dòng.
# Ví dụ:
# Input
# 2
# 7
# 1 6 3 4 5 2 7
# 1 1 1 2 3 4 3
# 7
# 1 6 3 5 5 2 2
# 0 1 9 0 1 2 3
# Output
# 45
# 27

def main():
  for _ in range(int(input())):
    ln = int(input())
    first = sorted([int(x) for x in input().split(maxsplit=ln)])
    sec = sorted([int(x) for x in input().split(maxsplit=ln)])[::-1]
    res = 0
    for i in range(ln):
      res += first[i] * sec[i]
    print(res)
  
main()