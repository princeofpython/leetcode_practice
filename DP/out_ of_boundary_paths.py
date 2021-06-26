# https://leetcode.com/explore/challenge/card/june-leetcoding-challenge-2021/606/week-4-june-22nd-june-28th/3790/


class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        if maxMove == 0:
            return 0
        ans = [[0 for _ in range(n)] for __ in range(m)]
        for _ in range(n):
            ans[0][_] += 1
            ans[m-1][_] += 1
        for _ in range(m):
            ans[_][0] += 1
            ans[_][n-1] += 1
        temp = copy.deepcopy(ans)
        final = ans[startRow][startColumn] 
        
        print(ans)
        def valid(i,j):
            return (-1 < i < m) and (-1 < j < n)
        for move in range(maxMove -1):
            for i in range(m):
                for j in range(n):
                    ans[i][j] = 0
                    if valid(i-1, j):
                        ans[i][j] += temp[i-1][j]
                    if valid(i, j -1):
                        ans[i][j] += temp[i][j-1]
                    if valid(i + 1, j):
                        ans[i][j] += temp[i+1][j]
                    if valid(i, j + 1):
                        ans[i][j] += temp[i][j+1]
            final += ans[startRow][startColumn]
            print(ans)
            print(temp)
            temp = copy.deepcopy(ans)
            
        return final%(10**9 + 7)

# recursion      
class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        MOD = 10**9 + 7
        
        @lru_cache(None)
        def dp(x,y, maxMove):
            if maxMove < 0: return 0
            
            if x<0 or x >= m or y<0 or y>= n: return 1
            
            left = dp(x-1,y,maxMove - 1)
            right = dp(x+1,y,maxMove - 1)
            up = dp(x,y-1,maxMove - 1)
            down = dp(x,y+1,maxMove - 1)
            
            total = up+down+left+right
            
            return total
        
        return dp(startRow, startColumn, maxMove) % MOD
      
#dp      
class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        if maxMove == 0: return 0
        dpCurr = [[0] * (n+2) for _ in range(m+2)]
        dpLast = [[0] * (n+2) for _ in range(m+2)]
        for i in range(1, m+1):
            dpCurr[i][1] += 1
            dpCurr[i][n] += 1
        for j in range(1, n+1):
            dpCurr[1][j] += 1
            dpCurr[m][j] += 1
        ans = dpCurr[startRow+1][startColumn+1]
        for d in range(maxMove-1):
            dpCurr, dpLast = dpLast, dpCurr
            for i, j in product(range(1, m+1), range(1, n+1)):
                dpCurr[i][j] = (dpLast[i-1][j] + dpLast[i+1][j] + dpLast[i][j-1] + dpLast[i][j+1]) % 1000000007
            ans = (ans + dpCurr[startRow+1][startColumn+1]) % 1000000007
        return ans
