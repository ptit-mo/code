# Cho ma trận A[M][N]. Nhiệm vụ của bạn hãy tìm số bước đi ít nhất dịch chuyển
# từ vị trí A[1][1] đến vị trí A[M][N]. Biết mỗi bước đi ta chỉ được phép dịch
# chuyển đến vị trí A[i][j+A[i][j]] hoặc vị trí A[i+A[i][j]][j] bên trong ma trận.
# Input:
# Dòng đầu tiên đưa vào số lượng test T.
# Dòng tiếp theo đưa vào các bộ test. Mỗi bộ test gồm hai phần: phần thứ nhất
# là hai số M, N; phần thứ hai là các phần tử của ma trận A[][]; các số được
# viết cách nhau một vài khoảng trống.
# T, M, N, A[i][j] thỏa mãn ràng buộc: 1≤T≤100; 1≤M, N, A[i][j]≤10^3.
# Output:
# Đưa ra kết quả mỗi test theo từng dòng. In ra -1 nếu không tìm được đáp án.
# Ví dụ:
# Input
# 1
# 3  3
# 2  1  2
# 1  1  1
# 1  1  1
# Output
# 2
# at each position, we can move X right or down where X is the value at current position

def main():
    for _ in range(int(input())):
        rows, cols = [int(x) for x in input().split()]
        mat = []
        for _ in range(rows):
            mat.append([int(x) for x in input().split(maxsplit=cols)])
        findMaxStepToReachRightCorner(mat)


def findMaxStepToReachRightCorner(matrix):
    rows, cols = len(matrix), len(matrix[0])
    MAX = 3000
    steps = [[MAX for _ in range(cols)] for _ in range(rows)]
    for r in reversed(range(rows)):
        for c in reversed(range(cols)):
            if r == rows - 1 and c == cols - 1:
                steps[r][c] = 0
                continue
            v = matrix[r][c]
            r1, c1 = r + v, c + v
            right = steps[r1][c] if r1 < rows else MAX
            down = steps[r][c1] if c1 < cols else MAX
            steps[r][c] = min(right, down) + 1
    # for r in steps:
    #     print(r)
    if steps[0][0] >= MAX:
        steps[0][0] = -1
    print(steps[0][0])


main()
