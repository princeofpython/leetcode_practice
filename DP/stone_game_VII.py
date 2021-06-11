#https://leetcode.com/explore/challenge/card/june-leetcoding-challenge-2021/604/week-2-june-8th-june-14th/3775/

def f(i, j, stones, summ, dp):
        if i==j:
            return 0
        if dp[i][j]!=-1:
            return dp[i][j]
        dp[i][j] = max(summ - stones[i] - f(i+1, j, stones, summ - stones[i], dp), summ - stones[j]- f(i, j-1,stones, summ - stones[j], dp))
        return dp[i][j]
class Solution:

    def stoneGameVII(self, stones: List[int]) -> int:
        dp = [[-1 for _ in range(len(stones))] for __ in range(len(stones))]
        return f(0, len(stones)-1, stones, sum(stones), dp)
