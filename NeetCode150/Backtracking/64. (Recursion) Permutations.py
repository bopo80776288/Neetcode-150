from typing import List
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # [1, 2, 3]
        
        # base case
        if len(nums) == 0:
            return [[]]
        # think of this as taking away number one by one and we will hit the base case where there is no number left
        # then we add back each number recursively 
        perms = self.permute(nums[1:])
        res = []
        for p in perms:
            for i in range(len(p) + 1):
                p_copy = p.copy()
                p_copy.insert(i, nums[0])
                res.append(p_copy)
        return res
