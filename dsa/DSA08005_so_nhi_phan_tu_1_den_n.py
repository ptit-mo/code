# Cho số tự nhiên n. Hãy in ra tất cả các số nhị phân từ 1 đến n.
# Input:
# Dòng đầu tiên ghi lại số lượng test T(T≤100).
# Mỗi test là một số tự nhiên n được ghi trên một dòng(n≤10000).
# Output:
# Đưa ra kết quả mỗi test trên một dòng.
# Ví dụ:
# Input
# 2
# 2
# 5
# Output
# 1 10
# 1 10 11 100 101

def printFrom1ToN(n: int):
    queue = ['1']
    res = []
    while (n > 0):
        top = queue.pop(0)
        res.append(top)
        queue.append(top + '0')
        queue.append(top + '1')
        n -= 1
    s = ' '.join(res)
    print(s)


for _ in range(int(input())):
    printFrom1ToN(int(input()))
