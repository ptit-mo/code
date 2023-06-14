# Cho biểu thức toán học đúng, bạn cần tìm tất cả các biểu thức đúng có thể bằng cách xóa bỏ các cặp dấu ngoặc tương ứng với nhau từ biểu thức ban đầu.
# Ví dụ: Cho biểu thức: (2+(2*2)+2) Các biểu thức tìm được:
# (2+2*2+2)
# 2+(2*2)+2
# 2+2*2+2
# Các biểu thức(2+2*2)+2 và 2+(2*2+2) không được chấp nhận vì không xóa đi các cặp dấu ngoặc tương ứng với nhau
# Input: Một dòng chứa biểu thức gồm các số nguyên không âm, các dấu + , -, *, / và dấu ngoặc đơn.
# Biểu thức không quá 200 kí tự, có chứa ít nhất 1 và không quá 10 cặp dấu ngoặc.
# Output: In ra tất các các biểu thức khác nhau thỏa mãn đầu bài theo thứ tự từ điển
# Ví dụ
# Input
# (1+(2*(3+4)))
# Output
# (1+(2*3+4))
# (1+2*(3+4))
# (1+2*3+4)
# 1+(2*(3+4))
# 1+(2*3+4)
# 1+2*(3+4)
# 1+2*3+4

def main():
  s = input()
  stack = []
  choices = [] # holds positions of pairs of parentheses
  for i, char in enumerate(s):
    if char == '(':
      stack.append(i)
    elif char == ')':
      choices.append([stack.pop(), i])

  # plan how to treat choices
  res = []
  def plan(cur: list, head: int):
    if len(cur) == len(choices):
      x = removeWithChoicePlan(s, choices, cur)
      if x != s:
        res.append(x)
      return
    for c in range(head, len(choices)):
      plan(cur + [0], c+1)
      plan(cur + [1], c+1)
  plan([], 0)

  #
  res = sorted(set(res))
  for i in res:
    print(''.join(i))

def removeWithChoicePlan(s: str, choices: list, choicesPlan: list) -> str:
  toRemove = []
  for i, plan in enumerate(choicesPlan):
    if plan == 0:
      toRemove = toRemove + [choices[i][0]] + [choices[i][1]]
  res = ''
  for i, char in enumerate(s):
    if i not in toRemove:
      res += char
  return res

main()