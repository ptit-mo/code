# Hãy viết chương trình tính toán giá trị của biểu thức tiền tố.
# Input:
# Dòng đầu tiên đưa vào số lượng bộ test T;
# Những dòng tiếp theo mỗi dòng đưa vào một bộ test. Mỗi bộ test là một biểu thức
# tiền tố exp. Các số xuất hiện trong biểu thức là các số đơn có 1 chữ số.
# Output:
# Đưa ra kết quả mỗi test theo từng dòng, chỉ lấy giá trị phần nguyên.
# Ràng buộc:
# T, exp thỏa mãn ràng buộc: 1≤T≤100; 2≤length(exp)≤20.
# Ví dụ:
# Input
# 2
# -+8/632
# -+7*45+20
# Output
# 8
# 25

# -+8/632 => -+8(6/3)2 => -+822 => -(8+2)2 => 10-2 = 8
# -+7*45+20 => -+7*452 => -+7(20)2 => -(27)2 => 27-2 = 25
# => see DSA07013, similar but input() is reversed and order in execution is reversed too

def main():
    for _ in range(int(input())):
        cal(input()[::-1])  # here is reversed vs DSA07013


def cal(st: str):
    queue = []
    for char in st:
        if char == '+':
            s, f = queue.pop(), queue.pop()
            queue.append(f+s)
        elif char == '-':
            s, f = queue.pop(), queue.pop()
            queue.append(s-f)  # here is reversed vs DSA07013
        elif char == '*':
            s, f = queue.pop(), queue.pop()
            queue.append(f*s)
        elif char == '/':
            s, f = queue.pop(), queue.pop()
            queue.append(s//f)  # here is reversed vs DSA07013
        else:
            queue.append(int(char))
    print(queue.pop())


main()
