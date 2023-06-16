# Cho đồ thị vô hướng G=<V, E> được biểu diễn dưới dạng danh sách cạnh. Hãy viết
# thuật toán duyệt theo chiều sâu bắt đầu tại đỉnh uÎV (DFS(u)=?)
# Input:
# Dòng đầu tiên đưa vào T là số lượng bộ test.
# Những dòng tiếp theo đưa vào các bộ test. Mỗi bộ test gồm |E| +1 dòng: dòng đầu
# tiên đưa vào ba số |V|, |E| tương ứng với số đỉnh và số cạnh của đồ thị, và u
# là đỉnh xuất phát; |E| dòng tiếp theo đưa vào các bộ đôi uÎV, vÎV tương ứng với
# một cạnh của đồ thị.
# T, |V|, |E| thỏa mãn ràng buộc: 1≤T≤200; 1≤|V|≤103; 1≤|E|≤|V|(|V|-1)/2;
# Output:
# Đưa ra danh sách các đỉnh được duyệt theo thuật toán DFS(u) của mỗi test theo
# khuôn dạng của ví dụ dưới đây.
# Ví dụ:
# Input:
# 1
# 6 9 5
# 1 2
# 1 3
# 2 3
# 2 4
# 3 4
# 3 5
# 4 5
# 4 6
# 5 6
# Output:
# 5 3 1 2 4 6

def main():
    for _ in range(int(input())):
        verticesNum, edgesNum, start = [int(x) for x in input().split()]
        graph = {}
        for _ in range(edgesNum):
            a, b = [int(x) for x in input().split()]
            graph[a] = [b] + graph.get(a, [])
            graph[b] = [a] + graph.get(b, [])
        for i in range(1, verticesNum+1):
            if i not in graph:
                graph[i] = []
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
        vertices[edge[1]] = [edge[0]] + vertices.get(edge[1], [])
    return vertices


main()
