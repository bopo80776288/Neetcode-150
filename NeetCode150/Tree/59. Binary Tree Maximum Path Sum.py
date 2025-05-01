# Definition for a binary tree node.
from typing import Optional

class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # for a path to be valid it can ONLY SPLIT ONCE
        # our goal is to traverse through each node as being the spliting point
        # store the maximum result in a global variable 
        
        # set a global variable to keep track of the result
        # reason to make it a list is for modification
        res = [root.val]

        # return max path sum without split 
        def dfs(root):
            # base case
            if not root:
                return 0
            # recursively find leftmax and right max
            leftMax = dfs(root.left)
            rightMax = dfs(root.right)
            
            # to eliminate negative values
            leftMax = max(leftMax, 0)
            rightMax = max(rightMax, 0)
            
            # compute max path sum WITH split 
            res[0] = max(res[0], root.val + leftMax + rightMax)

            # return the maxpath value without spliting 
            return root.val + max(leftMax, rightMax)
        # call the function 
        dfs(root)
        # return the result
        return res[0]
            

            


            

            

