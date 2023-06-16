# Cho đồ thị có trọng số không âm G=<V, E> được biểu diễn dưới dạng danh sách
# cạnh trọng số. Hãy viết chương trình tìm đường đi ngắn nhất từ đỉnh uÎV đến
# tất cả các đỉnh còn lại trên đồ thị.
# Input:
# Dòng đầu tiên đưa vào T là số lượng bộ test.
# Những dòng tiếp theo đưa vào các bộ test. Mỗi bộ test gồm |E|+1 dòng: dòng đầu
# tiên đưa vào hai ba số |V|, |E| tương ứng với số đỉnh và uÎV là đỉnh bắt đầu;
# |E| dòng tiếp theo mỗi dòng đưa vào bộ ba uÎV, vÎV, w tương ứng với một cạnh
# cùng với trọng số canh của đồ thị.
# T, |V|, |E| thỏa mãn ràng buộc: 1≤T≤100; 1≤|V|≤103; 1≤|E|≤|V|(|V|-1)/2;
# Output:
# Đưa ra kết quả của mỗi test theo từng dòng. Kết quả mỗi test là trọng số đường
# đi ngắn nhất từ đỉnh u đến các đỉnh còn lại của đồ thị theo thứ tự tăng dần các
# đỉnh.
#     Ví dụ:
# Input:
# 1
# 9  12 1
# 1  2   4
# 1  8   8
# 2  3   8
# 2  8   11
# 3  4   7
# 3  6   4
# 3  9   2
# 4  5   9
# 4  6  14
# 5  6  10
# 6  7  2
# 6  9  6
# Output:
# 0 4 12 19 26 16 18 8 14

# https://www.youtube.com/watch?v=XBkzljyis8w&list=PLm-wSyLgPb6Epw3Lut6PdMLDpDKLHHps6&index=19&ab_channel=VietAnhNGUYEN
def main():
    for _ in range(int(input())):
        MAX = 1e9
        nV, nE, start = [int(x) for x in input().split()]
        distance = [[MAX for _ in range(nV+1)] for _ in range(nV+1)]
        for _ in range(nE):
            v1, v2, d = [int(x) for x in input().split()]
            distance[v1][v2] = d
            distance[v2][v1] = d
        terminal = [i for i in range(1, nV+1) if i != start]
        cur = [distance[start][i] for i in range(1, nV+1) if i != start]
        traces = [start]
        while terminal:
            idx = pickShortestCurDistance(cur)
            x = terminal.pop(idx)

            updateCurDistanceWithTerminalX(cur, x)


def pickShortestCurDistance(d: list):
    res = 0
    for i in range(len(d)):
        if d[i] < d[res]:
            res = i
    return res


main()
