'''
https://leetcode.com/explore/featured/card/june-leetcoding-challenge-2021/604/week-2-june-8th-june-14th/3773/
Medium
DP
'''
class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        n = len(nums)
        dp = [0 for _ in range(n)]
        dp[n-1] = nums[n-1]
        heap = [(-dp[n-1], n-1)]
        heapq.heapify(heap)
        for i in range(n-2, -1, -1):
            large, index = heap[0]
            while(index > i + k):
                heapq.heappop(heap)
                if len(heap) > 0:
                    large, index = heap[0]
            dp[i] = nums[i]  - large
            heapq.heappush(heap,(-dp[i], i))
        return dp[0]
