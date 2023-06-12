# Cho hai số A, B ở hệ cơ số K. Hãy tính tổng hai số đó ở hệ cơ số K.
# Input: Dòng đầu ghi số bộ test T (T<10). Mỗi bộ test ghi 3 số K,A,B.
#             (2≤K≤10; A và B nếu biểu diễn trong hệ cơ số 10 đều nhỏ hơn 109)
# Output: In ra tổng của A và B trong hệ cơ số K
# Ví dụ:
# Input
# 1
# 2 1 10
# Output
# 11 # 01 + 10 hệ số 2 là 11
#  

def main():
  for _ in range(int(input())):
    _base, longer, shorter = [x for x in input().split()]
    base = int(_base)
    if len(longer) < len(shorter): 
      longer, shorter = shorter, longer
    ln = len(longer)
    while len(shorter) < ln: #make 2 nums equal length
      shorter = '0' + shorter
    remainder = 0
    res = ''
    for i in reversed(range(ln)):
      sum = int(shorter[i]) + int(longer[i]) + remainder
      res = str(sum % base) + res
      remainder = sum // base
    if remainder > 0:
      res = str(remainder) + res
    print(res)
    
main()