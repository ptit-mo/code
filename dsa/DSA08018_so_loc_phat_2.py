# Một số được gọi là lộc phát nếu chỉ có 2 chữ số 6 và 8. Cho số tự nhiên N. Hãy liệt kê các số lộc phát có không quá N chữ số.
# Input:
# Dòng đầu tiên ghi lại số tự nhiên T là số lượng bộ test (T<10);
# T dòng kế tiếp mỗi dòng ghi số N (1<N<15).
#  Output:
# Dòng đầu tiên là số lượng số lộc phát tìm được. Dòng thứ hai in đáp án theo thứ tự tăng dần.
#  Ví dụ:
# Input
# 2
# 2
# 3
# Output
# 6
# 6 8 66 68 86 88
# 14
# 6 8 66 68 86 88 666 668 686 688 866 868 886 888

def main():
    for _ in range(int(input())):
        num = int(input())
        res = []
        queue = ['6', '8']
        while queue:
            x = queue.pop(0)
            if len(x) > num:
                break
            res.append(x)
            queue.append(x + '6')
            queue.append(x + '8')
        print(len(res))
        print(' '.join(res))


main()
