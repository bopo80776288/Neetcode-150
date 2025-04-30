# Definition for a binary tree node.
from typing import List
from typing import Optional
from collections import deque

class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        if not root:
            return []

        result = []

        queue = deque()

        queue.append(root)

        while queue:
            level_length = len(queue)
            level_list = []

            for i in range(level_length):                
                node = queue.popleft()
                level_list.append(node.val)

                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)
            
            
            result.append(level_list[-1])
        
        return result
        
