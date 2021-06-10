#https://leetcode.com/explore/challenge/card/june-leetcoding-challenge-2021/604/week-2-june-8th-june-14th/3774/

class MyCalendar(object):

    def __init__(self):
        self.slots=[]

    def book(self, start, end):
        index = bisect.bisect_left(self.slots, (start, end))
        
        start_valid = (index == 0 or start >= self.slots[index-1][1])
        end_valid = (index == len(self.slots) or end <= self.slots[index][0])
        
        if start_valid and end_valid:
            self.slots.insert(index, (start, end))
            return True
        return False
