# Cho hai số nguyên dương S và T(S, T < 10000) và hai thao tác(a), (b) dưới đây:
# Thao tác(a): Trừ S đi 1  (S=S-1)
# Thao tác(b): Nhân S với 2 (S=S*2)
# Hãy dịch chuyển S thành T sao cho số lần thực hiện các thao tác(a), (b) là ít nhất.
# Ví dụ với    S = 2, T = 5 thì số các bước ít nhất để dịch chuyển S thành T thông qua 4 thao tác sau:
# Thao tác(a): 2*2 = 4
# Thao tác(b): 4-1 = 3
# Thao tác(a): 3*2 = 6
# Thao tác(b): 6-1 = 5
# Input:
# Dòng đầu tiên ghi lại số tự nhiên T là số lượng Test
# T dòng kế tiếp mỗi dòng ghi lại một bộ Test. Mỗi test là một bộ đôi S và T.
# Output: Đưa ra kết quả mỗi test theo từng dòng.
# Ví dụ:
# Input
# 3
# 2 5
# 3 7
# 7 4
# Output
# 4
# 4
# 3

def calST(s: int, t: int):
    notfound = 0
    # stepsFromSto saves results of number of steps to go from s to number index in stepsFromSto
    stepsFromSto = [notfound] * 20001
    calFrom = [s]  # calFrom holds numbers calculated to evaluate next numbers
    while (stepsFromSto[t] == 0):
        num = calFrom.pop(0)  # num is already calculated
        if (num - 1 > 0 and stepsFromSto[num-1] == notfound):
            stepsFromSto[num-1] = stepsFromSto[num] + 1
            calFrom.append(num-1)
        if (num * 2 < 20000 and stepsFromSto[num*2] == notfound):
            stepsFromSto[num*2] = stepsFromSto[num] + 1
            calFrom.append(num*2)
    print(stepsFromSto[t])


for _ in range(int(input())):
    s, t = [int(x) for x in input().split()]
    calST(s, t)
