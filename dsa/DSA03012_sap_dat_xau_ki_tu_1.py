# Cho xâu ký tự S bao gồm các ký tự in thường. Nhiệm vụ của bạn là kiểm tra xem
# ta có thể sắp đặt lại các ký tự trong S để hai ký tự giống nhau đều không kề
# nhau hay không? Đưa ra 1 nếu có thể sắp đặt lại các ký tự trong S thỏa mãn yêu
# cầu bài toán, ngược lại đưa ra - 1.
# Input:
# Dòng đầu tiên đưa vào số lượng bộ test T.
# Những dòng kế tiếp đưa vào các bộ test. Mỗi bộ test là một xâu ký tự S được
# viết trên một dòng.
# T, S thỏa mãn ràng buộc: 1≤T≤100
# 1≤length(S)≤10000.
# Output:
# Đưa ra kết quả mỗi test theo từng dòng.
# Ví dụ:
# Input
# 3
# geeksforgeeks
# bbbabaaacd
# bbbbb
# Output
# 1
# 1
# -1

# ===> as long as the mostly used char is not more than sum of the rest of char,
# it's capable


def isCapableOfMakingDiffByPairChain(chain: str):
    s = {}
    maxC = 0
    for c in chain:
        s[c] = s.get(c, 0)+1
        if s[c] >= maxC:
            maxC = s[c]
    if maxC - 1 <= len(chain) - maxC:
        print(1)
        return
    print(-1)


for _ in range(int(input())):
    isCapableOfMakingDiffByPairChain(input())
