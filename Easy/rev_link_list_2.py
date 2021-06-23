#https://leetcode.com/explore/challenge/card/june-leetcoding-challenge-2021/606/week-4-june-22nd-june-28th/3789/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        listt = [head]
        ptr = head
        while(ptr.next):
            listt.append(ptr.next)
            ptr = ptr.next
        newlistt = listt[:(left-1)] + list(reversed(listt[(left-1):(right)])) + listt[(right):]

        ptr = newlistt[0]
        for each in newlistt[1:]:
            ptr.next = each
            ptr = each
        newlistt[-1].next = None
        return newlistt[0]
