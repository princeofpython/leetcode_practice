# https://leetcode.com/explore/challenge/card/june-leetcoding-challenge-2021/605/week-3-june-15th-june-21st/3783/

def getSum(BIT,i):
    sum_ = 0 
    i = i+1  
    while i > 0:
        sum_ += BIT[i]
        i -= i & (-i)
    return sum_
  
def updateBIT(BIT , n , i ,val):  
    i += 1
    while i <= n:
        BIT[i] += val
        i += i & (-i)
class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.n = len(nums)
        self.BIT  = [0]*(self.n+1)
        for i in range(self.n):
            updateBIT(self.BIT, self.n, i, nums[i])
    def update(self, index: int, val: int) -> None:
        updateBIT(self.BIT, self.n, index, val- self.nums[index])
        self.nums[index] = val

    def sumRange(self, left: int, right: int) -> int:
        return getSum(self.BIT, right)- getSum(self.BIT, left-1) 
