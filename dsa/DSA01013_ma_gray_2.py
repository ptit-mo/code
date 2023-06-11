# Số nhị phân được xem là cách mặc định biểu diễn các số. Tuy nhiên, trong nhiều ứng dụng của điện tử và truyền thông lại dùng một biến thể của mã nhị phân đó là mã Gray. Mã Gray độ dài n có mã đầu tiên là n số 0, mã kế tiếp của nó là một xâu nhị phân độ dài n khác biệt với xâu trước đó một bít. Ví dụ với n=3 ta có 23 mã Gray như sau: 000, 001, 011, 010, 110, 111, 101, 100. Hãy viết chương trình chuyển đổi một xâu mã Gray X có độ dài n thành một xâu mã nhị phân.
# Input::
# Dòng đầu tiên là số lượng test T.
# T dòng kế tiếp ghi lại mỗi dòng một test. Mỗi test là một xâu mã Gray độ dài n.
# T, n thỏa mãn ràng buộc: 1≤T, n≤10.
# Output:
# Đưa ra kết quả mỗi test theo từng dòng.
# Input:
# 2
# 01101
# 01011
# Output:
# 01001
# 01101


def main():
  for _ in range(int(input())):
    bin = input()
    graycode = int(bin, 2)
    # https://en.wikipedia.org/wiki/Gray_code
    mask = graycode
    while mask > 0:
      mask >>= 1
      graycode ^= mask
    print(f"{graycode:0{len(bin)}b}")

main()