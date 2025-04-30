# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # create result variable to store the number of goodnodes
        count = 0

        def dfs(node, currMax):
            # nonlocal to access global variable
            nonlocal count
            # base case
            if not node:
                return 
            # check the condition while moving down the tree, if satisfy count += 1 
            # update current max
            if node.val >= currMax:
                count += 1 
                currMax = max(currMax, node.val)
            
            dfs(node.left, currMax)
            dfs(node.right, currMax)

            return count 
        
        return dfs(root, root.val)

        
            


