# Cho dãy số A[] có N phần tử. Hãy liệt kê tất cả các tổ hợp chập K của tập các 
# phần tử khác nhau trong A[]. Các tổ hợp cần liệt kê theo thứ tự từ điển (tức 
# là trong mỗi tổ hợp thì giá trị từ nhỏ đến lớn, và tổ hợp sau lớn hơn tổ hợp trước).
# Input
# Dòng đầu ghi hai số N và K.
# Dòng thứ 2 ghi N số của mảng A[]. Các giá trị không quá 1000.
# Dữ liệu đảm bảo số phần tử khác nhau của A[] không quá 20 và K không quá 10.
# Output
# Ghi ra lần lượt các tổ hợp tìm được, mỗi tổ hợp trên một dòng.
# Ví dụ
# Input
# 8 3
# 2 4 4 3 5 1 3 4
# Output
# 1 2 3
# 1 2 4
# 1 2 5
# 1 3 4
# 1 3 5
# 1 4 5
# 2 3 4
# 2 3 5
# 2 4 5
# 3 4 5

def main():
  _, ln = [int(x) for x in input().split()]
  arr = [int(x) for x in input().split()]
  arr = sorted(arr)
  countUniqueIncrementingSubArray(arr, ln)

def countUniqueIncrementingSubArray(arr: list, ln: int):
  res = []
  end = len(arr)
  def countSubArrayStartsFrom(indx: int, cur: list):
    nonlocal res
    if len(cur) == ln:
      if isIncrementing(cur):
        res += [' '.join(str(n) for n in cur)]
      return
    for i in range(indx, end):
      if i > 0 and arr[i] == arr[i-1]:
        continue
      countSubArrayStartsFrom(i+1, cur + [arr[i]])
  countSubArrayStartsFrom(0, [])
  for s in res:
    print(s)

def isIncrementing(arr: list) -> bool:
  for i in range(0, len(arr)):
    if i > 0 and arr[i] < arr[i-1]:
      return False
  return True
    
main()
