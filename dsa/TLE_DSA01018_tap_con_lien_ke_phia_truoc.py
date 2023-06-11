# Cho hai số N, K và một tập con K phần tử X[] =(X1, X2,.., XK) của 1, 2, .., N. Nhiệm vụ của bạn là hãy đưa ra tập con K phần tử trước đó của X[]. Ví dụ N=5, K=3, X[] ={2, 3, 5} thì tập con trước đó của X[] là {2, 3, 4}. Chú ý nếu tập con trong input là đầu tiên thì trước đó là tập con cuối cùng.
# Input:
# Dòng đầu tiên đưa vào số lượng test T.
# Những dòng kế tiếp đưa vào các bộ test. Mỗi bộ test gồm hai dòng: dòng thứ nhất
# là hai số N và K; dòng tiếp theo đưa vào K phần tử của X[] là một tập con K 
# phần tử của 1, 2, .., N.
# T, K, N, X[] thỏa mãn ràng buộc: 1≤T≤100; 1≤K≤N≤103.
# Output:
# Đưa ra kết quả mỗi test theo từng dòng.
# Ví dụ:
# Input
# 2
# 5  3
# 2  3  5
# 5  3
# 1  2  3
# Output
# 2 3 4
# 3 4 5

def main():
  for _ in range(int(input())):
    biggest, _ = [int(x) for x in input().split()]
    arr = [int(x) for x in input().split()]
    findPrevPerm(arr, biggest)
  
def findPrevPerm(target: list, biggest: int):
  found = 0
  ln = len(target)
  prev = []
  res = []
  def bactrack(cur, head):
    nonlocal found, prev, res
    if len(cur) == ln:
      if found == 1:
        found+=1
      if cur == target:
        res = prev
        found = 1
      prev = cur
      return
    for i in range(head, biggest+1):
      bactrack(cur+[i], i+1)
      if found > 1:
        break
  bactrack([], 1)
  if not res:
    res = range(biggest-ln+1, biggest+1)
  print(' '.join([str(x) for x in res]))
main()
  