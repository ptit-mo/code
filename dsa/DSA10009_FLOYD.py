# Cho đơn đồ thị vô hướng liên thông G = (V, E) gồm N đỉnh và M cạnh, các đỉnh được đánh số từ 1 tới N và các cạnh được đánh số từ 1 tới M.
# Có Q truy vấn, mỗi truy vấn yêu cầu bạn tìm đường đi ngắn nhất giữa đỉnh X[i] tới Y[i].
# Input:
# Dòng đầu tiên hai số nguyên N và M (1 ≤ N ≤ 100, 1 ≤ M ≤ N*(N-1)/2).
# M dòng tiếp theo, mỗi dòng gồm 3 số nguyên u, v, c cho biết có cạnh nối giữa đỉnh u và v có độ dài bằng c (1 ≤ c ≤ 1000).
# Tiếp theo là số lượng truy vấn Q (1 ≤ Q ≤ 100 000).
# Q dòng tiếp theo, mỗi dòng gồm 2 số nguyên X[i], Y[i].
# Output:
# Với mỗi truy vấn, in ra đáp án là độ dài đường đi ngắn nhất tìm được.
# Ví dụ:
# Input:
# 5 6
# 1 2 6
# 1 3 7
# 2 4 8
# 3 4 9
# 3 5 1
# 4 5 2
# 3
# 1 5
# 2 5
# 4 3
# Output
# 8
# 10
# 3

# https://www.youtube.com/watch?v=eRlwaxXvly0&ab_channel=VietAnhNGUYEN
def main():
    nV, nE = [int(x) for x in input().split()]
    # seed default value from A to B = ∞ , from A to B = 0
    distance = [[1e9 for _ in range(nV)] for _ in range(nV)]
    for i in range(nV):
        distance[i][i] = 0
    # fix with distance from input
    for _ in range(nE):
        v1, v2, d = [int(x) for x in input().split()]
        distance[v1 - 1][v2 - 1] = d
        distance[v2 - 1][v1 - 1] = d
    floyd(distance)
    # answer questions
    for _ in range(int(input())):
        v1, v2 = [int(x) for x in input().split()]
        print(distance[v1 - 1][v2 - 1])


def floyd(distance: list):
    n = len(distance)
    for mid in range(n):
        for r in range(n):
            for c in range(n):
                distance[r][c] = min(
                    distance[r][c], distance[r][mid] + distance[mid][c])
    # for r in distance:
    #     print(r)


main()
