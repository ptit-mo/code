# Cho hai đa thức có bậc không quá 10000 (chỉ viết ra các phần tử có hệ số khác 0). Hãy sử dụng danh sách liên kết đơn để viết chương trình tính tổng hai đa thức đó.
# Dữ liệu vào: Dòng đầu ghi số bộ test. Mỗi bộ test có hai dòng, mỗi dòng ghi một đa thức theo mẫu như trong ví dụ. Số phần tử của đa thức không quá 20.
# Chú ý: Bậc của các hạng tử luôn theo thứ tự giảm dần, trong đa thức chỉ có phép cộng và luôn được viết đầy đủ hệ số + số mũ (kể cả mũ 0).
# Kết quả: Ghi ra một dòng đa thức tổng tính được (theo mẫu như ví dụ)
# Ví dụ:
# Input
# 1
# 3*x^8 + 7*x^2 + 4*x^0
# 11*x^6 + 9*x^2 + 2*x^1 + 3*x^0
# Output
# 3*x^8 + 11*x^6 + 16*x^2 + 2*x^1 + 7*x^0

def main():
  for _ in range(int(input())):
    f,s = input(), input()
    combine(f,s)

def combine(f: list, s: list):
  fh: dict = mapX(f)
  sh: dict = mapX(s)
  for k in sh:
    if fh.get(k):
      fh[k] += sh[k]
    else:
      fh[k] = sh[k]
  print(' + '.join(f"{v}*{k}" for k, v in sorted(fh.items(), reverse=True)))

def mapX(s: str):
  res = {}
  terms = s.split(' + ')
  for term in terms:
    num, x = [ele.strip() for ele in term.split(sep='*')]
    res[x] = res.get(x, 0) + int(num)
  return res

main()