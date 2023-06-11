# Một xâu kí tự S = (s1, s2, .., sn) được gọi là xâu AB độ dài n nếu với mọi 
# si thì si hoặc là kí tự A hoặc si là kí tự B . Ví dụ xâu S = “ABABABAB” là một xâu AB độ dài 8. 
# Cho số tự nhiên N và số tự nhiên K (1£K<N£15 được nhập từ bàn phím), 
# hãy viết chương trình liệt kê tất cả các xâu AB có độ dài N chứa duy nhất một dãy K kí tự A liên tiếp.
# Dữ liệu vào chỉ có một dòng ghi hai số N và K.
# Kết quả ghi ra màn hình theo khuôn dạng:
# Dòng đầu tiên ghi lại số các xâu AB thỏa mãn yêu cầu bài toán;
# Những dòng kế tiếp, mỗi dòng ghi lại một xâu AB thỏa mãn. Các xâu được ghi ra theo thứ tự từ điển.
# Ví dụ:
# INPUT
# 5 3 
# OUTPUT
# 5
# AAABA
# AAABB
# ABAAA
# BAAAB
# BBAAA

def main():
  total, sub = [int(x) for x in input().split()]
  if total == sub:
    print(1)
    print('A' * sub)
    return
  left = total - sub
  combineAB(left, 'A' * sub) 

# room is number of slots for A B
# flag is the adjacent string A
def combineAB(room: int, flag: str):
  resAB = []
  def backtrack(cur: str):
    nonlocal resAB
    if len(cur) == room:
      resAB += [cur]
      return
    for i in ['A', 'B']:
      if (cur+i).__contains__(flag):
        continue
      backtrack(cur + i)
  backtrack('')
  # insert flag into each result
  res = []
  for s in resAB:
    for i in range(0, len(s)):
      if s[i] != 'B':
        continue
      # we got a B, we can decide to append before or after this position
      if i == 0:
        res += [flag+s]
      if i > 0 and s[i-1] == 'B':
        res += [s[:i] + flag + s[i:]]
      if i == len(s) - 1:
        res += [s+flag]
  print(len(res))
  for s in sorted(res):
    print(s)
         
main()
