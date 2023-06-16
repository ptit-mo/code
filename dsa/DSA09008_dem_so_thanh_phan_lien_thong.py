# Cho đồ thị vô hướng G=<V, E> được biểu diễn dưới dạng danh sách cạnh. Hãy tìm
# số thành phần liên thông của đồ thị.
# Input:
# Dòng đầu tiên đưa vào T là số lượng bộ test.
# Những dòng tiếp theo đưa vào các bộ test. Mỗi bộ test gồm 2 dòng: dòng đầu tiên
# đưa vào hai số |V|, |E| tương ứng với số đỉnh và số cạnh; Dòng tiếp theo đưa
# vào các bộ đôi uÎV, vÎV tương ứng với một cạnh của đồ thị.
# T, |V|, |E| thỏa mãn ràng buộc: 1≤T≤100; 1≤|V|≤103; 1≤|E|≤|V|(|V|-1)/2;
# Output:
# Đưa ra số thành phần liên thông của đồ thị.
#      Ví dụ:
# Input:
# 3
# 5 2
# 1 2 1 3
# 4 2
# 1 2 3 4
# 5 6
# 1 2 1 3 2 3 3 4 3 5 4 5
# Output:
# 3
# 2
# 1

def main():
    for _ in range(int(input())):
        verticesNum, edgesNum = [int(x) for x in input().split()]
        arr = [int(x) for x in input().split(maxsplit=edgesNum*2)]
        graph = {}
        for i in range(0, len(arr), 2):
            graph[arr[i]] = graph.get(arr[i], []) + [arr[i+1]]
            graph[arr[i+1]] = graph.get(arr[i+1], []) + [arr[i]]
        for i in range(1, verticesNum+1):
            if i not in graph:
                graph[i] = []
        findSCC(graph)


def findSCC(graph: dict):
    res = 0
    visited = set()
    queue = []
    for v in graph.keys():
        if v in visited:
            continue
        # print(v)
        visited.add(v)
        queue.append(v)
        while queue:
            cur = queue.pop(0)
            for neighbor in graph.get(cur, []):
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
        res += 1
    print(res)


main()
