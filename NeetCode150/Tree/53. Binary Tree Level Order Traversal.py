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
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        # initialize the result as a list
        res = []

        # base case when list root is an empty list
        if not root:
            return []
        
        # create a queue
        queue = deque()

        # input the first root node into the queue
        queue.append(root)

        # while the queue is not empty
        while queue:

            # create a variable to track the length of the current queue
            level_size = len(queue)
            # create a temp list to store the node at the current level
            level_nodes = []

            # level_size gives us the count of how many times we would run through each node in the queue
            for i in range(level_size):
                # for each action we popleft which is the first node in the level
                node = queue.popleft()
                # append the node to our temp list, make sure it is the value of the node
                level_nodes.append(node.val)

                # check if the current node we at has a left node to it
                # add it to the queue for next round
                if node.left:
                    queue.append(node.left)
                
                # check if the current node we at has a right node to it
                # add it to the queue for next round
                if node.right:
                    queue.append(node.right)
                
                # as one loop we append the node to the temp list and add its left and right node to the queue for next round

            # after the run through of each node at current level
            # append the temp list to result
            res.append(level_nodes)
        
        return res
