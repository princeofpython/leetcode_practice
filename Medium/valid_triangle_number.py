# https://leetcode.com/explore/challenge/card/july-leetcoding-challenge-2021/610/week-3-july-15th-july-21st/3815/

class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 3:
            return 0
        nums.sort()
        ans = 0
        for i in range(n):
            if nums[i] == 0:
                continue
            for j in range(i+1,n):
                if nums[j]== 0:
                    continue
                ans += (bisect.bisect_left(nums, nums[i]+ nums[j]) - j - 1)
        return ans
