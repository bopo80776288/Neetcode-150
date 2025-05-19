from typing import List
class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        
        def dfs(i, cur, total):
            # base case
            if total == target:
                res.append(cur.copy())
                return
            if i >= len(nums) or total > target:
                return 
            
            # include number
            cur.append(nums[i])
            dfs(i, cur, total + nums[i])
            
            # not include number 
            cur.pop()
            dfs(i + 1, cur, total)
        
        dfs(0, [], 0)
        return res
                
            
            


            
