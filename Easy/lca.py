# https://leetcode.com/explore/challenge/card/july-leetcoding-challenge-2021/610/week-3-july-15th-july-21st/3819/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        p = p.val
        q = q.val
        if  p > q:
            p , q = q, p
        def lca(root, p, q):
            if p <= root.val <= q:
                return root
            if q < root.val:
                return lca(root.left, p, q)
            if p > root.val:
                return lca(root.right, p, q)
            
        return lca(root, p, q)
