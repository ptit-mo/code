# Cho biểu thức P chỉ bao gồm các ký tự mở ngoặc ‘(’ hoặc đóng ngoặc ‘)’. Biểu thức P có thể viết đúng hoặc không đúng. Nhiệm vụ của bạn là tìm tổng độ dài lớn nhất của các biểu thức con viết đúng trong P(các biểu thức đúng không nhất thiết phải liên tiếp nhau).
# Chú ý: Độ dài của biểu thức đúng ngắn nhất là 2.
#
# Input:
# Dòng đầu tiên đưa vào số lượng bộ test T(không quá 100)
# Những dòng tiếp theo mỗi dòng đưa vào một bộ test. Mỗi bộ test là một biểu thức P được viết trên một dòng(độ dài của P không quá 100).
# Output:
# Đưa ra kết quả mỗi test theo từng dòng.
# Ví dụ:
# Input
# 4
# (()(
# ()()((
# ((()()())))
# ()(())(
# Output
# 2
# 4
# 10
# 6

# ==> cứ mỗi lần pop thì res + 2 là đươc :)

def cal(chain: str) -> int:
    res = 0
    stack = []
    for c in chain:
        if c == '(' or c == '[' or c == '{':
            stack.append(c)
        else:
            if (len(stack) == 0) or (
                    c == ')' and stack[-1] != '(') or (
                    c == ']' and stack[-1] != '[') or (
                    c == '}' and stack[-1] != '{'):
                stack.clear()
                continue
            res += 2
            stack.pop()
    return res


for _ in range(int(input())):
    print(cal(input()))
