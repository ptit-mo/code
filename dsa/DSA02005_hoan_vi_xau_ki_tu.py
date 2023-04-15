# Cho xâu ký tự S bao gồm các ký tự in hoa khác nhau. Hãy đưa ra tất cả các hoán vị của xâu ký tự S. Ví dụ S =”ABC” ta có kết quả {ABC ACB BAC BCA CAB CBA}.
# Input:
# Dòng đầu tiên đưa vào số lượng bộ test T.
# Những dòng tiếp theo đưa vào các bộ test. Mỗi bộ test là một xâu ký tự S được viết trên 1 dòng.
# T, S thỏa mãn ràng buộc: 1≤T≤10
# 1≤length(S) ≤10
# Output:
# Đưa ra kết quả mỗi test theo từng dòng.
# Input
# 2
# AB
# ABC
# Output
# AB BA
# ABC ACB BAC BCA CAB CBA

def permute(chain: str):
    visited = set()
    ln = len(chain)
    res = []

    def backtrack(cur):
        if len(cur) == ln:
            res.append(cur)
            return
        for c in chain:
            if c not in visited:
                visited.add(c)
                backtrack(cur+c)
                visited.remove(c)
    backtrack('')
    print(' '.join(res))


for _ in range(int(input())):
    permute(input())
