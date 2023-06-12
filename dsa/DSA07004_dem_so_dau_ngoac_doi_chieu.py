# Cho một xâu chỉ gồm các kí tự ‘(‘, ‘) và có độ dài chẵn. Hãy đếm số lượng dấu ngoặc cần phải đổi chiều ít nhất, sao cho xâu mới thu được là một dãy ngoặc đúng.
# Input:
# Dòng đầu tiên là số lượng bộ test T (T ≤ 20).
# Mỗi test gồm 1 xâu S có độ dài không vượt quá 100 000, chỉ gồm dấu ( và ).
# Output: 
# Với mỗi test, in ra đáp án tìm được trên một dòng.
# Ví dụ:
# Input:
# 4
# ))((
# ((((
# (((())
# )(())(((
# Output
# 2
# 2
# 1
# 3

def main():
  for _ in range(int(input())):
    s = input()
    solve(s)

def solve(s: str):
  stack = []
  count = 0
  for i in s:
    if i == '(':
      stack.append(i)
    elif len(stack) == 0:
      stack.append('(')
      count+=1
    else:
      stack.pop()
  # if stack is not empty now, it must have all (. We need half of those ( turned into )
  res = count + len(stack)//2
  print(res)
  
main()