# https://leetcode.com/explore/challenge/card/july-leetcoding-challenge-2021/609/week-2-july-8th-july-14th/3811/

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        dictt1 = {}
        dictt2 = {}

        for i in range(len(s)):
            if s[i] in dictt1:
                if dictt1[s[i]]!=t[i]:
                    return False
            if t[i] in dictt2:
                if dictt2[t[i]]!=s[i]:
                    return False
            else:
                dictt1[s[i]] = t[i]
                dictt2[t[i]] = s[i]
        return True
