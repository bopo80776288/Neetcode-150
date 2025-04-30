# Definition for a binary tree node.
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
from typing import Optional

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # root = [1,2,3,4,5,6,7]
        # Output = [1,3,2,7,6,5,4]
        
        # this is the base case where we hit the bottom of the tree
        if root is None:
            return None
        
        # initialize to swith the left node with the right node
        root.left, root.right = root.right, root.left

        # do it recursively on both side
        self.invertTree(root.left)

        self.invertTree(root.right)

        return root