# https://leetcode.com/explore/challenge/card/june-leetcoding-challenge-2021/606/week-4-june-22nd-june-28th/3793/

class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        ans = [0]*n
        ans[0] = 1
        for i in range(1,n):
            ans[i] = ans[i-1] + 1 if ratings[i] > ratings[i-1] else 1
        for i in range(n-2,-1,-1):
            ans[i] = max(ans[i], ans[i+1] + 1 if ratings[i] > ratings[i+1] else 1)
        return sum(ans)
