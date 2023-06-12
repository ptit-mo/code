# Cho hai số nguyên dương N và S. Hãy lựa chọn các chữ số phù hợp để tạo ra số nhỏ nhất và số lớn nhất có N chữ số sao cho tổng chữ số đúng bằng S.
# Input
# Chỉ có một dòng ghi hai số N và S. (0 < N <= 100; 0 <= S <= 900)
# Output
# Ghi ra hai số nhỏ nhất và lớn nhất tìm được, cách nhau một khoảng trống.
# Nếu không thể tìm được thì ghi ra “-1 -1”
# Ví dụ
# Input
# 3 20
# Output
# 299 992
# Input
# 2 900
# Output
# -1 -1
# Input
# 3 0
# Output
# -1 -1

def main():
  num, target = [int(x) for x in input().split()]
  if 9*num < target:
    print('-1 -1')
    return
  if target == 0 and num == 1:
    print("0 0")
    return
  biggest = ''
  toSub = 9
  while(target >= 0 and toSub >= 0):
    while(len(biggest) < num and target >= toSub):
      target -= toSub
      biggest += str(toSub)
    toSub-=1
  if len(biggest) != num:
    print('-1 -1')
    return
  smallest = biggest[::-1]
  if smallest[0] == '0':
    firstPositive = -1
    for i, char in enumerate(smallest):
      if char > '0':
        firstPositive = i
        break
    if firstPositive == -1:
      print('-1 -1')
      return
    smallest = '1' + str(smallest[1:firstPositive]) + str(int(smallest[firstPositive]) - 1) + str(smallest[firstPositive+1:])
  print(f"{smallest} {biggest} ")
main()