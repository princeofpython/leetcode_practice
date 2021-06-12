#https://leetcode.com/explore/challenge/card/june-leetcoding-challenge-2021/604/week-2-june-8th-june-14th/3776/

class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        n = len(stations)
        dp = [0 for _ in range(n+1)]
        
        dp[0] = startFuel

        for i in range(0,n):
            for j in range(i, -1, -1):
                if dp[j] >= stations[i][0]:
                    dp[j+1] = max(dp[j+1], dp[j] + stations[i][1])
                    
        return bisect.bisect_left(dp, target) if bisect.bisect_left(dp, target) <= n else -1
                
