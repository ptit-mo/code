#!/usr/bin/python3

def main():
    for i in range(int(input())):
        buildTriangle()

def buildTriangle():
    ln = int(input())
    nums = [int(x) for x in input().split(maxsplit=ln)]
    def makeTriangle(nums,ln):
        if ln == 0:
            return
        out = " ".join([str(x) for x in nums])
        print(f"[{out}]")
        ln -= 1
        newNums = [0]*ln
        for i in range(ln):
            newNums[i] = nums[i] + nums[i+1]
        makeTriangle(newNums, ln)
    makeTriangle( nums, ln)
        
main()
