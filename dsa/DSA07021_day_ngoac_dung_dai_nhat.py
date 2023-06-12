# Cho một xâu chỉ gồm các kí tự ‘(‘ và ‘)’. Một dãy ngoặc đúng được định nghĩa như sau:
# -     Xâu rỗng là 1 dãy ngoặc đúng.
# -     Nếu A là 1 dãy ngoặc đúng thì (A) là 1 dãy ngoặc đúng.
# -     Nếu A và B là 2 dãy ngoặc đúng thì AB là 1 dãy ngoặc đúng.
# Cho một xâu S. Nhiệm vụ của bạn là hãy tìm dãy ngoặc đúng dài nhất xuất hiện trong xâu đã cho.
# Input: Dòng đầu tiên là số lượng bộ test T (T ≤ 20).
# Mỗi test gồm một xâu S có độ dài không vượt quá 105 kí tự.
# Output:  Với mỗi test in ra một số nguyên là độ dài dãy ngoặc đúng dài nhất tìm được.
# Ví dụ:
# Input:
# 4
# ((()
# )()())
# ()(()))))
# ((())(()()()
# Output
# 2
# 4
# 6
# 6

def main():
  for _ in range(int(input())):
    s = input()
    solve(s)
    
def solve(s: str):
  # instead of saving (,), we save their positions :D
  stack = [-1]
  res = 0
  for i, char in enumerate(s):
    if char == '(':
      stack.append(i)
    elif len(stack) > 1 and s[stack[-1]] == '(':
      stack.pop()
      res = max(res, i - stack[-1])
    else:
      stack[-1] = i #new start
  print(res)

main()