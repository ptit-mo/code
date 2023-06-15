# Cho hai số nguyên dương L, R. Hãy đưa ra số các số K trong khoảng [L, R] thỏa mãn điều kiện:
# Tất cả các chữ số của K đều khác nhau.
# Tất cả các chữ số của K đều nhỏ hơn hoặc bằng 5.
# Ví dụ với L = 4, R = 13 ta có 5 số thỏa mãn yêu cầu là 4, 5, 10, 12, 13,
# Input:
# Dòng đầu tiên đưa vào số lượng test T.
# Dòng tiếp theo đưa vào các bộ test. Mỗi bộ test được là một cặp L, R được viết trên một dòng.
# T, L, R thỏa mãn ràng buộc: 1≤T≤100; 0≤L≤R≤105.
# Output:
# Đưa ra kết quả mỗi test theo từng dòng.
# Ví dụ:
# Input
# 2
# 4  13
# 100  1000
# Output
# 5
# 100

def main():
    for _ in range(int(input())):
        f, s = [int(x) for x in input().split()]
        find(f, s)


def find(f: int, s: int):
    queue = ['1', '2', '3', '4', '5']
    cnt = 0
    while queue:
        x = queue.pop(0)
        if int(x) >= f and int(x) <= s:
            cnt += 1
        for i in range(0, 6):
            if str(i) not in str(x):
                queue.append(str(x) + str(i))
    print(cnt)


main()
