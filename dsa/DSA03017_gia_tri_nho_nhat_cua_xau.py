# Cho xâu ký tự S. Ta gọi giá trị của xâu S là tổng bình phương số lần xuất hiện mỗi ký tự trong S. Hãy tìm giá trị nhỏ nhất của xâu S sau khi thực hiện K lần loại bỏ ký tự.
# Input:
# Dòng đầu tiên đưa vào số lượng bộ test T.
# Những dòng kế tiếp đưa vào các bộ test. Mỗi bộ test gồm hai phần: phần thứ nhất là số K; phần thứ hai là một xâu ký tự S được viết trên một dòng.
# T, S, K thỏa mãn ràng buộc: 1≤T≤100;  1≤length(S)≤10000; 1≤K≤1000.
# Output:
# Đưa ra kết quả mỗi test theo từng dòng.
# Ví dụ:
# Input
# 2
# 2
# ABCCBC
# 2
# AAAB
# Output
# 6
# 2


def main():
  for _ in range(int(input())):
    toRemove = int(input())
    s = input()
    charCount = {}
    for char in s:
      charCount[char] = charCount.get(char, 0) + 1
    sortedCount = [v for _, v in charCount.items()]
    while (toRemove > 0):
      sortedCount = sorted(sortedCount, reverse=True)
      sortedCount[0] -= 1
      toRemove -= 1
    res = 0
    for cnt in sortedCount:
      res += cnt * cnt
    print(res)
  
main()