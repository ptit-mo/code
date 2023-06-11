# Cho ma trận vuông Ci,j cấp N (1<= i, j <= N<10) gồm N2 số tự nhiên và số tự 
# nhiên K (các số trong ma trận không nhất thiết phải khác nhau và đều không quá
# 100, K không quá 104). Hãy viết chương trình lấy mỗi hàng, mỗi cột duy nhất một
# phần tử sao cho tổng các phần tử này đúng bằng K.
# Dữ liệu vào: Dòng 1 ghi hai số N và K. N dòng tiếp theo ghi ma trận C. 
# Kết quả: dòng đầu ghi số cách tìm được. Mỗi dòng tiếp theo ghi một cách theo 
# vị trí của số đó trong lần lượt từng hàng của ma trận. Xem ví dụ để hiểu rõ hơn. 
# Ví dụ:
# INPUT
# 3 10
# 2 4 3
# 1 3 6
# 4 2 4
# OUTPUT
# 2
# 1 3 2
# 3 2 1

def main():
  dimension, target = [int(x) for x in input().split()]
  matrix = [[int(x) for x in input().split()] for _ in range(dimension)]
  res = find(dimension, matrix, target)
  print(len(res))
  for found in res:
    print(' '.join(str(x+1) for x in found))
  
def find(dimension: int, matrix: list, target: int) -> list:
  res = []
  def backtrack(cur: list, curSum: int, startRow: int):
    nonlocal res
    if curSum > target:
      return
    if curSum == target:
      if len(cur) == dimension:
        res.append(list(cur))
      return
    for row in range(startRow, dimension):
      for col in range(0, dimension):
        if col in cur:
          continue
        backtrack(cur+[col], curSum + matrix[row][col], row+1)
  backtrack([], 0, 0)
  return res
  
main()