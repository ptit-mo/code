# Cho số tự nhiên N. Hãy tìm số nguyên dương X nhỏ nhất được tạo bởi số 9 và số
# 0 chia hết cho N. Ví dụ với N = 5 ta sẽ tìm ra  X = 90.
# Input:
# Dòng đầu tiên ghi lại số lượng test T (T≤100).
# Những dòng kế tiếp mỗi dòng ghi lại một test. Mỗi test là một số tự nhiên N
# được ghi trên một dòng (N≤100).
# Output:
# Đưa ra theo từng dòng số X nhỏ nhất chia hết cho N tìm được .
# Ví dụ:
# Input
# 2
# 5
# 7
# Output
# 90
# 9009

def main():
    for _ in range(int(input())):
        print(find(int(input())))


def find(num):
    queue = ['9']
    while queue:
        choice = queue.pop(0)
        if int(choice) % num == 0:
            return choice
        queue.append(choice + '0')
        queue.append(choice + '9')
    return -1


main()
