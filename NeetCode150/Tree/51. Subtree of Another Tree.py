 # Definition for a binary tree node.
from typing import Optional

class TreeNode:
     def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def isSameTree(p, q):
            if not p and not q:
                return True
            # base case when structure not the same OR values not the same
            if not p or not q or p.val != q.val:
                return False 
        
            # recursion part where we want to further check the left tree and right tree for both 
            return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)
        
        if not root:
            return False
        
        if root.val == subRoot.val:
            if isSameTree(root, subRoot):
                return True
        
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        
        

        
        
        


