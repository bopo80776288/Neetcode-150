# Definition for a binary tree node.
from typing import Optional

class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # this is the base case and we NEED it 
        if root is None:
            return 0 
        
        leftDepth = self.maxDepth(root.left)
        rightDepth = self.maxDepth(root.right)
        
        # the 1 is the height of the currecnt node itself
        # think of if we are at the bottom of the tree simply just return the height = 1 for the last node 
        # recursively building up 
        return 1 + max(leftDepth, rightDepth)