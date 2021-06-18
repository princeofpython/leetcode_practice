# https://leetcode.com/explore/challenge/card/june-leetcoding-challenge-2021/605/week-3-june-15th-june-21st/3782/

class Solution:
    def numSubarrayBoundedMax(self, nums: List[int], left: int, right: int) -> int:
        add = 1
        sub = 1
        plus = 0
        minus = 0
        for i, each in enumerate(nums):
            if each <= right:
                plus += add
                add += 1
            else:
                add = 1
            if each< left:
                minus += sub
                sub += 1
            else:
                sub = 1
        return plus - minus
