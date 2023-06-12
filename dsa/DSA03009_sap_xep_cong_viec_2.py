# Cho N công việc. Mỗi công việc được biểu diễn như một bộ 3 số nguyên dương <JobId, Deadline, Profit>, trong đó JobId là mã của việc, Deadline là thời gian kết thúc của việc, Profit là lợi nhuận đem lại nếu hoàn thành việc đó đúng hoặc trước thời gian. Thời gian tối thiểu để hoàn thành mỗi công việc là 1 đơn vị thời gian. Hãy cho biết lợi nhuận lớn nhất có thể thực hiện các việc với giả thiết mỗi việc được thực hiện đơn lẻ.
# Input:
# Dòng đầu tiên đưa vào số lượng bộ test T.
# Những dòng kế tiếp đưa vào các bộ test. Mỗi bộ test gồm hai phần: phần thứ nhất là số lượng Job N; phần thứ hai đưa vào 3×N số tương ứng với N job.
# T, N, JobId, Deadline, Profit thỏa mãn ràng buộc:1≤T≤100;  1≤N≤1000; 1≤ JobId ≤1000; 1≤ Deadline ≤1000; 1≤ Profit ≤1000.
# Output:
# Đưa số lượng công việc tương ứng và lợi nhuận lớn nhất có thể đạt được.
# Ví dụ:
# Input
# 2
# 4
# 1 4 20
# 2 1 10
# 3 1 40
# 4 1 30
# 5
# 1 2 100
# 2 1 19
# 3 2 27
# 4 1 25
# 5 1 15
# Output
# 2 60
# 2 127

def main():
  for _ in range(int(input())):
    jobs = []
    for _ in range(int(input())):
      jobs.append([int(x) for x in input().split(maxsplit=3)])
    jobs.sort(key=lambda x: x[2], reverse=True)
    # https://www.youtube.com/watch?v=EaA7OmCUXRU&ab_channel=V%C5%A9Th%C3%A0nhC%C3%B4ng
    # occupied records which slots were used to do the work before so other jobs cant be done in this slot
    occupied = [False]*1001
    picked, profit = 0, 0
    for job in jobs:
      timestampToDo = job[1] # timestampToDo is as close as the deadline as possible, nuoc den chan moi nhay :D
      while(occupied[timestampToDo] and timestampToDo > 0):
        timestampToDo -= 1
      if timestampToDo > 0:
        picked += 1
        profit += job[2]
        occupied[timestampToDo] = True
    print(f"{picked} {profit}")

main()