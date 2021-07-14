#https://leetcode.com/explore/challenge/card/july-leetcoding-challenge-2021/609/week-2-july-8th-july-14th/3813/

class Solution:
    def customSortString(self, order: str, string: str) -> str:
        alphabet = 'abcdefghijklmnopqrstuvwxyz'
        dictt = {}
        
        listt = list(string)
        listt = sorted(listt, key = lambda x: order.find(x))
        
        return ''.join(listt)
