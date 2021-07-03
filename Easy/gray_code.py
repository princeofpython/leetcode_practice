# https://leetcode.com/submissions/detail/516881450/?from=explore&item_id=3799

class Solution:
    def grayCode(self, n: int) -> List[int]:
        if n==1:
            return [0,1]
        prev= [0,1]
        for each in range(1,n):
            value = 2**(each)
            ans = []
            for i in prev:
                ans.append(i)
            for i in reversed(prev):
                ans.append(value+i)
            
            prev = ans[:]
        return ans
