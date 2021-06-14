#https://leetcode.com/explore/challenge/card/june-leetcoding-challenge-2021/604/week-2-june-8th-june-14th/3778/

class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key = lambda x: x[1], reverse = True)
        units = 0
        boxes = 0

        for i, j in boxTypes:
            if truckSize > boxes + i:
                units+= i* j
                boxes+= i
            else:
                units += ((truckSize - boxes) * j)
                break
        return units
        
