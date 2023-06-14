# Cho số tự nhiên N (N<10^9) và hai phép biến đổi (a), (b) dưới đây.
# Thao tác (a): Trừ N đi 1 (N=N-1). Ví dụ N=17, thao tác (a) biến đổi
# N = N-1 =16.
# Thao tác (b): N = max(u,v) nếu u*v =N (u>1, v>1). Ví dụ N=16, thao tác (b) có
# thể biến đổi N = max(2, 8)=8 hoặc N=max(4, 4)=4.
# Chỉ được phép sử dụng hai thao tác (a) hoặc (b), hãy biến đổi N thành 1 sao số
# các thao tác (a), (b) được thực hiện ít nhất. Ví dụ với N=17, số các phép (a),
# (b) nhỏ nhất biến đổi N thành 1 là 4 bước như sau:
# Thao tác (a): N = N-1 = 17-1 = 16
# Thao tác (b): 16 = max(4,4) = 4
# Thao tác (b): 4 = max(2,2) = 2
# Thao tác (a): 2 = 2-1 = 1
# Input:
# Dòng đầu tiên ghi lại số tự nhiên T là số lượng Test;
# T dòng kế tiếp mỗi dòng ghi lại một bộ Test. Mỗi test là một số N.
# Đưa ra kết quả mỗi test theo từng dòng.
# Ví dụ:
# Input
# 3
# 17
# 50
# 100
# Output
# 4
# 5
# 5


def main():
    for _ in range(int(input())):
        target = int(input())
        make1(target)


def make1(target: int):
    stepsFromTargetTo = {target: 0}
    calCulated = [target]
    while (not stepsFromTargetTo.get(1)):
        x = calCulated.pop(0)
        if x - 1 > 0 and not stepsFromTargetTo.get(x-1):
            stepsFromTargetTo[x-1] = stepsFromTargetTo[x] + 1
            calCulated.append(x-1)
        sqrt: int = int(x ** 0.5)
        for i in range(2, sqrt + 1):
            if x % i == 0:
                bigger = x // i
                if not stepsFromTargetTo.get(bigger):
                    stepsFromTargetTo[bigger] = stepsFromTargetTo[x] + 1
                    calCulated.append(bigger)
    print(stepsFromTargetTo[1])


main()
