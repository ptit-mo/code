# Ta gọi số nguyên dương K là một số BDN nếu các chữ số trong K chỉ bao gồm các 0
# hoặc 1 có nghĩa. Ví dụ số K = 1, 10, 101. Cho số tự nhiên N (N<2^63). Hãy cho
# biết có bao nhiêu số BDN nhỏ hơn N. Ví dụ N=100 ta có 4 số BDN bao gồm các số:
# 1, 10, 11, 100.
# Input:
# Dòng đầu tiên ghi lại số tự nhiên T là số lượng Test;
# T dòng kế tiếp mỗi dòng ghi lại một bộ Test. Mỗi test là một số tự nhiên N.
# Đưa ra kết quả mỗi test theo từng dòng.
# Ví dụ:
# Input
# 3
# 10
# 100
# 200
# Output
# 2
# 4
# 7

def main():
    for _ in range(int(input())):
        num = input()
        # number of smaller BDNs = maxBDN
        # if num == 200 => maxBDN = 111 => bdn = 1 10 11 100 101 110 111 => 1 -> 7 = 7
        # if num == 102 => maxBDN = 101 => bdn = 1 10 11 100 101 => 1 -> 5 = 5
        # we need to fid maxBDN
        maxBDN = ''
        # switch from firstBiggerThan1 to 1
        firstBiggerThan1 = len(num)
        for i, char in enumerate(num):
            if char > '1':
                firstBiggerThan1 = i
                break
        maxBDN = num[:firstBiggerThan1] + '1' * (len(num) - firstBiggerThan1)
        print(int(maxBDN, 2))


def find(num):
    queue = ['1']
    count = 0
    while True:
        n = queue.pop(0)
        if int(n) > num:
            return count
        count += 1
        queue.append(n + '0')
        queue.append(n + '1')
    print(count)


main()
