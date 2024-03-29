# Một người có cái túi thể tích V (V<1000). Anh ta có N đồ vật cần mang theo (N≤1000),
# mỗi đồ vật có thể tích là A[i] (A[i]≤100) và giá trị là C[i] (C[i]≤100).
# Hãy xác định tổng giá trị lớn nhất của các đồ vật mà người đó có thể mang theo,
# sao cho tổng thể tích không vượt quá V.
# Input
# Dòng đầu ghi số bộ test T (T<10)
# Mỗi bộ test gồm ba dòng. Dòng đầu ghi 2 số N và V. Dòng tiếp theo ghi N số của
# mảng A. Sau đó là một dòng ghi N số của mảng C.
# Dữ liệu vào luôn đảm bảo không có đồ vật nào có thể tích lớn hơn V.
# Output
# Với mỗi bộ test, ghi trên một dòng giá trị lớn nhất có thể đạt được.
# Ví dụ
# Input
# 1
# 15 10
# 5 2 1 3 5 2 5 8 9 6 3 1 4 7 8
# 1 2 3 5 1 2 5 8 7 4 1 2 3 2 1
# Output
# 15

# ref https://vnoi.info/wiki/translate/topcoder/dynamic-programming

def main():
    for _ in range(int(input())):
        ln, target = [int(x) for x in input().split()]
        volume = [int(x) for x in input().split()]
        value = [int(x) for x in input().split()]
        stuff = [[0, 0]]
        for i in range(ln):
            stuff.append([volume[i], value[i]])
        tab = [[0 for _ in range(0, target+1)] for _ in range(len(stuff))]
        for i in range(1, len(stuff)):
            curVol = stuff[i][0]
            for curTarget in range(1, target+1):
                if curVol > curTarget:  # this vol cant make curTarget
                    # is there any prev vols can make curTarget?
                    tab[i][curTarget] = tab[i-1][curTarget]
                else:
                    tab[i][curTarget] = max(
                        tab[i-1][curTarget], tab[i-1][curTarget - curVol] + stuff[i][1])
        print(tab[-1][-1])


main()
