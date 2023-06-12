# Hoàng yêu thích các số may mắn. Ta biết rằng một số là số may mắn nếu biểu diễn thập phân của nó chỉ chứa các chữ số may mắn là 4 và 7. Ví dụ, các số 47, 744, 4 là số may mắn và 5, 17, 467 không phải. Hoàng muốn tìm số may mắn bé nhất có tổng các chữ số bằng n. Hãy giúp anh ấy
# Dữ liệu vào: Dòng đầu ghi số bộ test, mỗi bộ test có một dòng chứa số nguyên n (1 ≤ n ≤ 106) — tổng các chữ số của số may mắn cần tìm.
# Kết quả: In ra trên 1 dòng số may mắn bé nhất, mà tổng các chữ số bằng n. Nếu không tồn tại số thỏa mãn, in ra -1.
# Ví dụ:
# Input
# 2
# 11
# 10
# Output
# 47
# -1

def main():
  for _ in range(int(input())):
    target = int(input())
    res = ''
    while target > 0:
      if (target - 7) % 4 == 0 or (target - 7) % 7 == 0:
        res += '7'
        target -= 7
      elif (target - 4) % 4 == 0 or (target - 4) % 7 == 0:
        res = '4' + res
        target -=4
      else:
        res = -1
        break
    print(res)
main()