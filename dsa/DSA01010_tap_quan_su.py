## Tại Chương Mỹ Resort, vào nửa đêm, cả trung đội nhận lệnh tập trung ở sân. Mỗi 
## chiến sỹ được đánh số từ 1 đến N (1<N<40). Giám thị yêu cầu chọn ra một dãy K 
## chiến sỹ để tập đội ngũ và cứ lần lượt duyệt hết tất cả các khả năng chọn K 
## người như vậy từ nhỏ đến lớn (theo số thứ tự). Bài toán đặt ra là cho một nhóm 
## K chiến sỹ hiện đang phải tập đội ngũ, hãy tính xem trong lượt chọn K người 
## tiếp theo thì mấy người trong nhóm cũ sẽ được tạm nghỉ. Nếu đã là nhóm cuối 
## cùng thì tất cả đều sẽ được nghỉ.
## Dữ liệu vào: Dòng đầu ghi số bộ test, không quá 20. Mỗi bộ test viết trên hai 
## dòng
## Dòng 1: hai số nguyên dương N và K (K<N)
## Dòng 2 ghi K số thứ tự của các chiến sỹ đang phải tập đội ngũ (viết từ nhỏ đến 
## lớn)
## Kết quả: Với mỗi bộ dữ liệu in ra số lượng chiến sỹ được tạm nghỉ.
##  Ví dụ:
## INPUT
## 3
## 5 3
## 1 3 5
## 5 3
## 1 4 5
## 6 4
## 3 4 5 6
## OUTPUT
## 1
## 2
## 4
# def main():
#  test = int(input())
#  for _ in range(test):
#    total, sub = [int(x) for x in input().split()]
#    curPermutation = [int(x) for x in input().split()]
#    countNewElementInNextPermutation(total, sub, curPermutation)
# def countNewElementInNextPermutation(total: int, sub: int, curP: list):
#  found = 0
#  res = 0
#  def backtrack(cur, head):
#    nonlocal found, res
#    if len(cur) == sub:
#      diff = countDiff(cur, curP)
#      if found == 1:
#        # print (curP, cur, diff, found)
#        res = diff
#        found += 1
#      elif cur == curP:
#        found = 1
#      return
#    for i in range(head, total+1):
#      backtrack(cur+[i], i+1)
#      if found > 1:
#        break
#  backtrack([], 1)
#  if res == 0: # last combination
#    print(sub)
#    return
#  print(res)
#  
# def countDiff(a: list, b: list)-> int:
#  return len([x for x in a if x not in b])
# main()
