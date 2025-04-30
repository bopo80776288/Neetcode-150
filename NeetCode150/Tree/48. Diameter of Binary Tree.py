from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.res = 0
        
        # funtion to help us return the height
        def dfs(curr):
            # base case, reach the bottom of the tree
            if not curr:
                return 0
            
            left = dfs(curr.left)
            right = dfs(curr.right)

            # update the maximum of the sum of left and right height from each node
            # we count the edges between node so there is no "1" added 
            self.res = max(self.res, left + right)
            
            # return the height from each node
            return 1 + max(left, right)
        
        # call the function 
        dfs(root)

        # return result 
        return self.res