# Vương quốc PTIT sử dụng bảng chữ cái gồm N chữ cái Latinh viết hoa. Quy tắc đặt tên của gia đình Hoàng gia  PTIT là chọn ra K chữ cái (không trùng nhau) và sắp xếp lại theo thứ tự từ điển.
# Hãy liệt kê tất cả các cái tên có thể có của gia đình Hoàng gia PTIT
# Input
# Dòng đầu ghi số bộ test T (không quá 10)
# Mỗi bộ test ghi 2 số N và K (3 < K < N < 16)
# Output
# Với mỗi bộ test, ghi ra tất cả các cái tên có thể được tạo ra, mỗi kết quả viết trên một dòng.
# Ví dụ
# Input
# 1
# 4 2
# Output
# AB
# AC
# AD
# BC
# BD
# CD

def generateName(maxChar, ln):
    def backtrack(cur, head):
        if len(cur) == ln:
            print(cur)
            return
        prefix = 65  # 65 is A, 66 is B, etc.
        for choice in range(head, maxChar):
            backtrack(cur + chr(prefix+choice), choice+1)
    backtrack('', 0)


for test in range(int(input())):
    maxChar, ln = [int(x) for x in input().split()]
    generateName(maxChar, ln)
