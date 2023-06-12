# Cho hai số nguyên dương S và D, trong đó S là tổng các chữ số và D là số các chữ số của một số. Nhiệm vụ của bạn là tìm số nhỏ nhất thỏa mãn S và D? Ví dụ với S = 9, D = 2 ta có số nhỏ nhất thỏa mãn S và D là 18.
# Input:
# Dòng đầu tiên đưa vào số lượng bộ test T.
# Những dòng kế tiếp đưa vào các bộ test. Mỗi bộ test là bộ 2 số S và D được viết trên một dòng.
# T, S, D thỏa mãn ràng buộc: 1≤T≤100;  1≤ S,D≤1000.
# Output:
# Đưa ra kết quả mỗi test theo từng dòng. Nếu không có đáp án, in ra -1.
# Ví dụ:
# Input
# 2
# 9 2
# 20 3
# Output
# 18
# 299

def main():
  for _ in range(int(input())):
    target, num = [int(x) for x in input().split()]
    if num == 1 and target <= 9:
      print(target)
      continue
    if num * 9 < target:
      print(-1)
      continue
    res = ''
    toSub = 9
    while(target >= 0 and toSub >= 0 ):
      while(len(res) < num and target >= toSub):
        target -= toSub
        res = str(toSub) + res
      toSub-=1
    if res[0] == '0':
      # find first element bigger than 1
      found = -1
      for i, char in enumerate(res):
        if char > '0':
          found = i
          break
      if found == -1:
        print(-1)
        continue
      res = '1' + str(res[1:found]) + str(int(res[found])-1) + str(res[found+1:])
    print(res)
main()