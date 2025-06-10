from typing import List 

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        def backtracking(i, subset):
            # base case
            if i == len(nums):
                res.append(subset.copy())
                return 

            # pick 
            subset.append(nums[i])
            backtracking(i + 1, subset)
            subset.pop()

            # check if there is duplicate
            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1 
            
            # don't pick
            backtracking(i + 1, subset)
        
        backtracking(0, [])

        return res