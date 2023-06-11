# Hãy viết chương trình nhận vào một chuỗi (có thể khá dài) các ký tự số và đưa ra màn hình hoán vị kế tiếp của các ký tự số đó (với ý nghĩa là hoán vị có giá trị lớn hơn tiếp theo nếu ta coi chuỗi đó là một giá trị số nguyên). Chú ý: Các ký tự số trong dãy có thể trùng nhau.
# Ví dụ:               123 -> 132
# 279134399742 -> 279134423799  
# Cũng có trường hợp sẽ không thể có hoán vị kế tiếp. Ví dụ như khi đầu vào là chuỗi 987.  
# Dữ liệu vào: Dòng đầu tiên ghi số nguyên  t là số bộ test (1 ≤ t ≤ 1000).  Mỗi bộ test có một dòng, đầu tiên là số thứ tự bộ test, một dấu cách, sau đó là chuỗi các ký tự số, tối đa 80 phần tử.  
# Kết quả: Với mỗi bộ test hãy đưa ra một dòng gồm thứ tự bộ test, một dấu cách, tiếp theo đó là hoán vị kế tiếp hoặc chuỗi “BIGGEST” nếu không có hoán vị kế tiếp. 
# Ví dụ:
# INPUT
# 3
# 1 123
# 2 279134399742
# 3 987
# OUTPUT
# 1 132
# 2 279134423799
# 3 BIGGEST

def main():
  for _ in range(int(input())):
    ord, curP = [x for x in input().split()]
    res = findNextPermutation(list(curP))
    print(f"{ord} {''.join(res)}")

def findNextPermutation(curP: list) -> str:
  # find first position [ab] where b > a -> a the pivot
  # find first num from the right equal or bigger than pivot, swap with pivot
  # sort from pivot to end
  pivot = -1
  res = ''
  for i in reversed(range(len(curP))):
    if i > 0 and curP[i] > curP[i-1]:
      pivot = i-1
      break
  if pivot == -1: #already the biggest permutation
    return 'BIGGEST'
  for i in reversed(range(pivot,len(curP))):
    if curP[i] >= curP[pivot]:
      curP[pivot], curP[i] = curP[i], curP[pivot] 
      res = curP[:pivot+1] + sorted(curP[pivot+1:])
      break
  return res

main()