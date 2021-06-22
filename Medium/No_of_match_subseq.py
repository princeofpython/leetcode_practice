# https://leetcode.com/explore/challenge/card/june-leetcoding-challenge-2021/606/week-4-june-22nd-june-28th/3788/
class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
      
        memory = {}
        
        def is_subsequence(word, s):
            if word in mem.keys():
                return mem[word]
            
            i = -1
            for c in word:
                i = s.find(c, i + 1)
                if i == -1:
                    mem[word] = False
                    return mem[word]

            mem[word] = True
            return mem[word]
        
        ans = 0
        for word in words:
            if len(word) > len(s):
                continue
            if is_subsequence(word, s):
                ans += 1

        return ans
            
