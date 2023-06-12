# Trên trục Ox tính từ vị trí 0, người ta muốn xếp nhiều nhất các đoạn thẳng sao
# cho không đoạn nào chồng lấn lên nhau. Đoạn thẳng thứ i có vị trí bắt đầu là 
# X1[i] và kết thúc tại X2[i], với X1[i] <= X2[i].
# Hãy tính số đoạn thẳng nhiều nhất có thể được lựa chọn để đưa lên trục Ox và 
# không có đoạn nào chồng lấn lên nhau.
# Input
# Dòng đầu tiên ghi số bộ test, không quá 10.
# Với mỗi bộ test: dòng đầu ghi số N là số đoạn thẳng (không quá 105)
# Tiếp theo là N dòng, mỗi dòng có 2 số nguyên mô tả đoạn thẳng. Các giá trị tọa
# độ đều là các số nguyên không âm và không quá 106.
# Output
# Với mỗi test, viết trên 1 dòng số lượng đoạn thẳng nhiều nhất có thể được lựa 
# chọn thỏa mãn điều kiện đề bài.
# Ví dụ
# Input
# 1
# 10
# 39 55
# 37 74
# 0 1
# 19 25
# 65 76
# 51 52
# 19 21
# 5 94
# 46 65
# 32 40
# Output
# 5

def main():
  for _ in range(int(input())):
    lines = []
    for _ in range(int(input())):
      lines.append([int(x) for x in input().split()])
    lines.sort(key=lambda x: x[1])
    prev = 0
    res = 1
    for i in range(1, len(lines)):
      if lines[i][0] >= lines[prev][1]:
        res+=1
        prev=i
    print(res)
main()