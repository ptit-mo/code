# Cho dãy số nguyên A[] có N phần tử.
# Gọi f(i,j) = |ai| + |ai+1| + … + |aj|
# Goij g(i,j) = ai + ai+1 + … + aj
# Với tất cả các cặp 1 ≤ i ≤ j ≤ N.
# Hãy tính giá trị lớn nhất của f(i,j) + g(i,j).
# Input
# Dòng đầu ghi số N (1 ≤ N ≤ 50000)
# Dòng thứ 2 ghi N số nguyên của dãy A[]
# Output
# Ghi ra giá trị lớn nhất của f(i,j) + g(i,j)
# Ví dụ
# Input
# 5
# -3 5 -10 8 -2
# Output
# 26


def main():
  # because if i pick ai < 0, i'll add with |ai| > 0 and they'll become 0
  # there's no need to pick negative nums
  # just pick positve nums
  m = int(input())
  arr = [int(x) for x in input().split(maxsplit=m)]
  res = 0
  for i in arr:
    if i > 0:
      res += i 
  print(res * 2)
main()