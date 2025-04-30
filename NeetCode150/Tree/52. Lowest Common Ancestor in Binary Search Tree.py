# Definition for a binary tree node.
from typing import Optional

class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        
        # default case where p and q are in different side
        curr = root

        # look into left subtree
        while curr:
            
            # look into right subtree
            if p.val > curr.val and q.val > curr.val:
                curr = curr.right
            
            # look into left subtree
            elif p.val < curr.val and q.val < curr.val:
                curr = curr.left
            
            # they are in different subtree, return curr
            else:
                return curr
        
        
        

        
        