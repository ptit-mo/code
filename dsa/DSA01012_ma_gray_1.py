# Số nhị phân được xem là cách mặc định biểu diễn các số. Tuy nhiên, trong nhiều ứng dụng của điện tử và truyền thông lại dùng một biến thể của mã nhị phân đó là mã Gray. Mã Gray độ dài n có mã đầu tiên là n số 0, mã kế tiếp của nó là một xâu nhị phân độ dài n khác biệt với xâu trước đó một bít. Ví dụ với n=3 ta có 23 mã Gray như sau: 000, 001, 011, 010, 110, 111, 101, 100. Hãy viết chương trình liệt kê các mã Gray có độ dài n.
# Input:
# Dòng đầu tiên là số lượng test T.
# T dòng kế tiếp ghi lại mỗi dòng một test. Mỗi test là một số tự nhiên n.
# T, n thỏa mãn ràng buộc: 1≤T, n≤10.
# Output:
# Đưa ra kết quả mỗi test theo từng dòng.
# 
# Input:
# 2
# 3
# 4
# Output:
# 000 001 011 010 110 111 101 100
# 0000 0001 0011 0010 0110 0111 0101 0100 1100 1101 1111 1110 1010 1011 1001 1000

def main():
  for _ in range(int(input())):
    # https://en.wikipedia.org/wiki/Gray_code
    ln = int(input())
    biggest = 1 << ln
    res = [x ^ x >> 1 for x in range(biggest)]
    s = []
    for i in res:
      s += [f"{i:0{ln}b}"]
    print(' '.join(s))
main()