# Cho ma trận A[M][N]. Nhiệm vụ của bạn là đếm tất cả các đường đi từ phần tử A[0][0] đến phần tử A[M-1][N-1].
# Bạn chỉ được phép dịch chuyển xuống dưới hoặc sang phải phần tử liền kề với vị trí hiện tại.
# Input:
# Dòng đầu tiên đưa vào số lượng bộ test T.
# Những dòng kế tiếp đưa vào các bộ test. Mỗi bộ test gồm hai phần: phần thứ nhất là hai số M, N tương ứng với số hàng và số cột của ma trận
# dòng tiếp theo đưa vào các phần tử của ma trận A[][]
# các số được viết cách nhau một vài khoảng trống.
# T, M, N, A[i][j] thỏa mãn ràng buộc: 1≤T ≤10
# 1≤M, N, A[i][j]≤100.
# Output:
# Đưa ra số cách di chuyển của mỗi test theo từng dòng.
# Giải thích test 1: Có 3 cách di chuyển là[1 4 5 6], [1 2 5 6] và[1 2 3 6].
#
# Input
# 2
# 2  3
# 1  2  3
# 4  5  6
# 2  2
# 1  2
# 3  4
# Output
# 3
# 2

def countWayToMoveInMatrix(row: int, col: int):
    # this problem just needs counting, we just care about row and col, not value
    cache = [[0]*col]*row
    # fill first row and first col of cache with 1, as there is 1 way to go from [0,0]
    # to those position
    for c in range(col):
        cache[0][c] = 1
    for r in range(row):
        cache[r][0] = 1
    for r in range(1, row):
        for c in range(1, col):
            cache[r][c] = cache[r-1][c] + cache[r][c-1]
    # print(cache)
    return cache[row-1][col-1]


for _ in range(int(input())):
    row, col = [int(x) for x in input().split()]
    # skip row values
    for _ in range(row):
        input()
    print(countWayToMoveInMatrix(row, col))
