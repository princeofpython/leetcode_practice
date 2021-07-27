#https://leetcode.com/explore/challenge/card/july-leetcoding-challenge-2021/611/week-4-july-22nd-july-28th/3828/

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        n= len(nums)
        a = float('inf')
        for i in range(n-2):
            for j in range(i+1, n-1):
                inde = bisect.bisect_left(nums[j+1:], target-(nums[i]+ nums[j])) + j + 1
                for index in [inde- 1, inde]:
                    if index == j or index == n:
                        continue
                    ind = nums[index]
                    
                    if ind+nums[i]+nums[j] == target :
                        return target
                    if abs(target - (ind+nums[i]+nums[j])) < abs(target -a ):
                        a = (ind+nums[i]+nums[j])
        return a
#2-pointer solution     
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        diff = float('inf')
        nums.sort()
        for i in range(len(nums)):
            lo, hi = i + 1, len(nums) - 1
            while (lo < hi):
                sum = nums[i] + nums[lo] + nums[hi]
                if abs(target - sum) < abs(diff):
                    diff = target - sum
                if sum < target:
                    lo += 1
                else:
                    hi -= 1
            if diff == 0:
                break
        return target - diff
