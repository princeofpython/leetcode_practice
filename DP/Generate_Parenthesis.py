# https://leetcode.com/explore/challenge/card/june-leetcoding-challenge-2021/605/week-3-june-15th-june-21st/3781/

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        listt = [[] for _ in range(n+ 1)]
        listt[0].append("")
        listt[1].append("()")
        for i in range(2, n+1):
            for j in range(0, i):
                k = i- j -1
                for each in listt[j]:
                    for each2 in listt[k]:
                        listt[i].append('('+ each + ')'+ each2)
        return listt[n]
