# Cho đồ thị có hướng G=<V, E> được biểu diễn dưới dạng danh sách cạnh. Hãy viết thuật toán duyệt theo chiều sâu bắt đầu tại đỉnh uÎV (DFS(u)=?)
# Input:
# Dòng đầu tiên đưa vào T là số lượng bộ test.
# Những dòng tiếp theo đưa vào các bộ test. Mỗi bộ test gồm 2 dòng: dòng đầu tiên đưa vào ba số |V|, |E|, uÎV tương ứng với số đỉnh, số cạnh và đỉnh bắt đầu duyệt; Dòng tiếp theo đưa vào các bộ đôi uÎV, vÎV tương ứng với một cạnh của đồ thị.
# T, |V|, |E| thỏa mãn ràng buộc: 1≤T≤200; 1≤|V|≤103; 1≤|E|≤|V|(|V|-1)/2;
# Output:
# Đưa ra danh sách các đỉnh được duyệt theo thuật toán DFS(u) của mỗi test theo khuôn dạng của ví dụ dưới đây.
#     Ví dụ:
# Input:
# 1
# 6 9 5
# 1 2 2 5 3 1 3 2 3 5 4 3 5 4 5 6 6 3
# Output:
# 5 4 3 1 2 6


def main():
    for _ in range(int(input())):
        _, e, start = [int(x) for x in input().split(maxsplit=3)]
        edgesL = [int(x) for x in input().split(maxsplit=2*e)]
        edges = []
        for k in range(0, 2*e, 2):
            edges.append([edgesL[k], edgesL[k+1]])
        graph: dict = switch(edges)
        # for k, v in graph.items():
        #     print(f"{k}: {' '.join([str(x) for x in v])}")
        dfs(graph, start)


def dfs(graph: dict | list, start: int):
    visited = set([start])
    stack = [start]
    while stack:
        cur = stack.pop()
        for v in graph[cur]:
            if v not in visited:
                stack.append(v)
                visited.add(v)
        print(cur, end=' ')
    print()


def switch(edges):
    vertices = {}
    for edge in edges:
        vertices[edge[0]] = [edge[1]] + vertices.get(edge[0], [])
    return vertices


main()
