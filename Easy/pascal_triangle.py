# https://leetcode.com/explore/challenge/card/june-leetcoding-challenge-2021/605/week-3-june-15th-june-21st/3786/

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        answer = [[] for _ in range(numRows)]
        answer[0] = [1]
        if numRows == 1:
            return answer
        for i in range(1, numRows):
            answer[i] = [1]*(i+1)
            for j in range(1, i):
                answer[i][j] = answer[i-1][j-1] +answer[i-1][j] 
        return answer
