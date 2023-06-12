# Cho biểu thức đúng P chỉ bao gồm các phép toán +, -, các toán hạng cùng với các ký tự ‘(’, ‘)’. Hãy bỏ tất cả các ký tự ‘(’, ‘)’ trong P để nhận được biểu thức tương đương. Ví dụ với P = a – (b + c) ta có kết quả P = a – b – c .
# Input:
# Dòng đầu tiên đưa vào số lượng bộ test T;
# Những dòng tiếp theo mỗi dòng đưa vào một bộ test. Mỗi bộ test là một biểu thức P được viết trên một dòng.
# Output:
# Đưa ra kết quả mỗi test theo từng dòng.
# Ràng buộc:
# T, P thỏa mãn ràng buộc: 1≤T≤100; 1≤length(P)≤103.
# Ví dụ:
#  
# Input
# 2
# a–(b+c)
# a-(b-c-(d+e))-f
# Output
# a-b-c
# a-b+c+d+e-f

def main():
  for _ in range(int(input())):
    solve(list(input()))

def solve(s: list):
  # save position of ( , when meeting ), trace from ( to ) to see if there should be sign switches
  stack = []
  for pos, char in enumerate(s):
    if char == '(':
      stack.append(pos)
    elif char == ')':
      start = stack.pop()
      if start == 0 or s[start-1] == '+':
        continue # no need to switch for first () without sign or with sign +
      elif s[start-1] == '-':
        for i in range(start, pos):
          if s[i] == '+':
            s[i] = '-'
          elif s[i] == '-':
            s[i] = '+'
  res = ''
  for char in s:
    if char != '(' and char != ')':
      res += char
  print(res)
       
      
main()