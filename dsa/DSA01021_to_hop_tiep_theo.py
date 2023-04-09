# Cho số nguyên dương (1<N<40) và số nguyên dương K<N. Với 1 tổ hợp chập K phần tử của N, hãy cho biết tổ hợp tiếp theo sẽ có bao nhiêu phần tử mới. Nếu tổ hợp đã cho là cuối cùng thì kết quả là K.
# Dữ liệu vào: Dòng đầu ghi số bộ test, không quá 20. Mỗi bộ test viết trên hai dòng
# Dòng 1: hai số nguyên dương N và K (K<N)
# Dòng 2 ghi K số của tổ hợp ban đầu. Theo đúng thứ tự tăng dần, không có số nào trùng nhau.
# Kết quả: Với mỗi bộ dữ liệu in ra số lượng phần tử mới.
#  Ví dụ:
# INPUT
# 3
# 5 3
# 1 3 5
# 5 3
# 1 4 5
# 6 4
# 3 4 5 6
# OUTPUT
# 1
# 2
# 4

tests = int(input())


class Solution:
    def __init__(self):
        self.found = False
        self.done = False

    def do(self):
        maxNum, ln = [int(x) for x in input().split()]
        given = [int(x) for x in input().split()]

        def combine(head, cur):
            if self.done:
                return
            if len(cur) == ln:
                # print(cur)
                if self.found == True:
                    # print(cur, given)
                    print(len(set(cur).difference(set(given))))
                    self.done = True
                    return
                if cur == given:
                    self.found = True
                return
            for i in range(head, maxNum+1):
                combine(i+1, cur+[i])
        combine(1, [])
        if not self.done:
            print(ln)


for t in range(tests):
    Solution().do()
