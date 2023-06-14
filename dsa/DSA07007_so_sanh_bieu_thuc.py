# Cho P1, P2 là hai biểu thức đúng chỉ bao gồm các ký tự mở ngoặc ‘(’ hoặc đóng ngoặc ‘)’ và các toán hạng in thường. Nhiệm vụ của bạn là định xem P1 và P2 có giống nhau hay không.
# Input:
# Dòng đầu tiên đưa vào số lượng bộ test T;
# Những dòng tiếp theo mỗi dòng đưa vào một bộ test. Mỗi bộ test gồm hai dòng: dòng thứ nhất đưa vào P1, dòng tiếp theo đưa vào P2.
# Output:
# Đưa ra kết quả mỗi test theo từng dòng.
# Ràng buộc:
# T, P thỏa mãn ràng buộc: 1≤T≤100; 1≤length(P) ≤100.
# Ví dụ:
# Input
# 2
#-(a+b+c)
#-a-b-c
# a-b-(c-d)
# a-b-c-d
# Output
# YES
# NO

def main():
  for _ in range(int(input())):
    long, short = input(), input()
    if shorten(long) == shorten(short):
      print('YES')
    else:
      print('NO')

def shorten(expression: str) -> str:
  exp = list(expression)
  stack = []
  for i, char in enumerate(exp):
    if char == '(':
      stack.append(i)
    elif char == ')':
      start = stack.pop() - 1
      if start == -1 or exp[start] == '+':
        continue
      elif exp[start] == '-':
        for p in range(start+1, i):
          if exp[p] == '-':
            exp[p] = '+'
          elif exp[p] == '+':
            exp[p] = '-'
  return ''.join(exp).replace('(','').replace(')','')
        
main()