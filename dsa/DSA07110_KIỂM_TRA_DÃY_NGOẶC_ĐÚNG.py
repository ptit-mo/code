# Cho một xâu chỉ gồm các kí tự ‘(‘, ‘)’, ‘[‘, ‘]’, ‘{‘, ‘}’. Một dãy ngoặc đúng được định nghĩa như sau:
# -     Xâu rỗng là 1 dãy ngoặc đúng.
# -     Nếu A là 1 dãy ngoặc đúng thì(A), [A], {A} là 1 dãy ngoặc đúng.
# -     Nếu A và B là 2 dãy ngoặc đúng thì AB là 1 dãy ngoặc đúng.
# Cho một xâu S. Nhiệm vụ của bạn là xác định xâu S có là dãy ngoặc đúng hay không?
# Input:
# Dòng đầu tiên là số lượng bộ test T(T ≤ 20).
# Mỗi test gồm 1 xâu S có độ dài không vượt quá 100 000.
# Output:
# Với mỗi test, in ra “YES” nếu như S là dãy ngoặc đúng, in ra “NO” trong trường hợp ngược lại.
# Ví dụ:
# Input:
# 2
# [()]{}{[()()]()}
# [(])
# Output:
# YES
# NO

def checkValidChain(chain: str):
    stack = []
    for c in chain:
        if c == '(' or c == '[' or c == '{':
            stack.append(c)
        else:
            if (len(stack) == 0) or (
                    c == ')' and stack[-1] != '(') or (
                    c == ']' and stack[-1] != '[') or (
                    c == '}' and stack[-1] != '{'):
                print("NO")
                return
            stack.pop()
    if len(stack) > 0:
        print("NO")
        return
    print("YES")


for _ in range(int(input())):
    checkValidChain(input())
