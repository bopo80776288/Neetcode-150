# Definition for a binary tree node.
from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # set global varaibles cnt and res 
        cnt = k
        res = root.val 


        def dfs(node):

            nonlocal cnt, res 

            if not node:
                return 
            # traverse the tree by the order left -> current -> right
            dfs(node.left)
            cnt -= 1
            if cnt == 0:
                res = node.val
                return
            
            dfs(node.right)

        dfs(root)
        return res
        