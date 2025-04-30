# Two binary trees are considered equivalent if they share the exact same structure and the nodes have the same values.
# Definition for a binary tree node.
from typing import Optional

class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # base case when same 
        if not p and not q:
            return True
        # base case when structure not the same OR values not the same
        if not p or not q or p.val != q.val:
            return False 
        
        # recursion part where we want to further check the left tree and right tree for both 
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)


