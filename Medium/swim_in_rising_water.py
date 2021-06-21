# https://leetcode.com/explore/challenge/card/june-leetcoding-challenge-2021/605/week-3-june-15th-june-21st/3785/

def getMin(visited, dist):
    min_dist = float('inf')
    min_vert = len(visited)
    
    for i in range(len(dist)):
        if not visited[i]:
            if dist[i] < min_dist:
                min_dist = dist[i]
                min_vert = i
    return min_vert, min_dist
            
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        visited = [False for _ in range(n*n)]
        
        dist = [float('inf')]*(n*n)
        dist[0] = grid[0][0]
        ans = 0
        for _ in range(n*n -1):
            vert, distance = getMin(visited, dist)

            if vert == n*n:
                break
            visited[vert] = True
            
            ans = max(ans, distance)
            for each in [vert- n, vert-1 if vert%n != 0 else -1, vert+ 1 if (vert+1)%n !=0 else -1, vert+ n]:
                if (-1 < each < n*n) and (not visited[each]):
                    dist[each] = max(ans, grid[each//n][each%n])
        return dist[n*n-1]
