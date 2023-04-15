# Bài toán Tháp Hà Nội đã rất nổi tiểng. Bắt đầu có các đĩa xếp chồng lên cột A
# theo thứ tự kích thước giảm dần, nhỏ nhất ở trên cùng. Cột B và cột C ban đầu không có đĩa nào cả.
#
# Mục tiêu của bạn là di chuyển toàn bộ các đĩa theo đúng thứ tự về cột C, tuân
# theo các quy tắc sau:
# Mỗi lần chỉ có thể di chuyển một đĩa.
# Mỗi lần di chuyển sẽ lấy đĩa trên từ một trong các cột và đặt nó lên trên một
# cột khác.
# Không được đặt đĩa lên trên đĩa nhỏ hơn..
# Input:
# Số tự nhiên  0 < N < 10
# Output:
# In ra lần lượt từng bước theo mẫu trong ví dụ. Chú ý giữa các chữ cái và dấu
# -> có khoảng trống.
# Ví dụ:
# Input
# 3
# Ouput
# A -> C
# A -> B
# C -> B
# A -> C
# B -> A
# B -> C
# A -> C

def hanoiTower(level: int, start: chr, mid: chr, end: chr):
    if level == 1:
        print(f"{start} -> {end}")
        return
    hanoiTower(level-1, start, end, mid)
    print(f"{start} -> {end}")
    hanoiTower(level-1, mid, start, end)


hanoiTower(int(input()), 'A', 'B', 'C')
