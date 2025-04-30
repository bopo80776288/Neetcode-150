from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(node, left, right):
            
            # base case return True since empty bst can be valid
            if not node:
                return True
            
            if not (node.val < right and node.val > left):
                return False
            
            # checking left subtree, so updating the right boundry 
            # since every node value to the left must be less than the current node

            # think of it at every level of recursive function call, the parent has a set of (node, left, right) 
            # the children has to take the value and apply to their own function, so the range will update
            return (dfs(node.left, left, node.val) and 
                    dfs(node.right, node.val, right))
            
        return dfs(root, float("-inf"), float("inf"))
            


            


            
            
