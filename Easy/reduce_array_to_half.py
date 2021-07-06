from collections import Counter
class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        frq= Counter(arr)
        print(frq)
        n = len(arr)
        count = 0
        rem = 0
        for value in sorted(frq.values(), reverse = True):
            rem += value
            print(rem)
            count+=1
            if rem >= n/2:
                break
        return count
