# Definition for a binary tree node.
from typing import Optional

class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        self.diff = 0

        def dfs(curr):
            
            # base case
            if not curr:
                return 0 

            # recursion 
            leftHeight = dfs(curr.left)
            rightHeight = dfs(curr.right)
            
            # condition check 
            if abs(leftHeight - rightHeight) > 1:
                self.diff = 1
                

            return 1 + max(leftHeight, rightHeight)
        
        dfs(root)
        
        if self.diff == 0:
            return True
        else:
            return False


        

