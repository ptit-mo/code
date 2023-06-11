# Cho số nguyên dương N. Hãy đếm số bước ít nhất để đưa N về 1 bằng cách thực
# hiện ba thao tác dưới đây:
# Nếu N chia hết cho 2 bạn có thể giảm N = N/2.
# Nếu N chia hết cho 3 bạn có thể giảm N = N/3.
# Giảm N đi 1.
# Input:
# Dòng đầu tiên đưa vào số lượng bộ test T.
# Những dòng kế tiếp đưa vào các bộ test. Mỗi bộ test là một số N được viết trên
# một dòng.
# T, N thỏa mãn ràng buộc:
# 1≤T≤100
# 1≤N ≤100000.
# Output:
# Đưa ra kết quả mỗi test theo từng dòng.
# Ví dụ:
# Input
# 2
# 10
# 6
# Output
# 3
# 2

def findMinStepsToGoFrom1ToN(n: int) -> int:
    tab = [0] * (n+1)
    for i in range(2, n+1):
        tab[i] = min(
            tab[i-1]+1,
            tab[i//2]+1 if i % 2 == 0 else n,
            tab[i//3]+1 if i % 3 == 0 else n
        )
    return tab[n]


for _ in range(int(input())):
    print(findMinStepsToGoFrom1ToN(int(input())))
