#https://leetcode.com/explore/challenge/card/june-leetcoding-challenge-2021/604/week-2-june-8th-june-14th/3776/

class Solution:
    #n^2
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        n = len(stations)
        dp = [0 for _ in range(n+1)]
        
        dp[0] = startFuel

        for i in range(0,n):
            for j in range(i, -1, -1):
                if dp[j] >= stations[i][0]:
                    dp[j+1] = max(dp[j+1], dp[j] + stations[i][1])
                    
        return bisect.bisect_left(dp, target) if bisect.bisect_left(dp, target) <= n else -1
    
    
    #nlogn
    def minRefuelStops(self, target: int, tank: int, stations: List[List[int]]) -> int:
        pq = []  # A maxheap is simulated using negative values
        stations.append((target, float('inf')))

        ans = prev = 0
        for location, capacity in stations:
            tank -= location - prev
            while pq and tank < 0:  # must refuel in past
                tank += -heapq.heappop(pq)
                ans += 1
            if tank < 0: return -1
            heapq.heappush(pq, -capacity)
            prev = location

        return ans
