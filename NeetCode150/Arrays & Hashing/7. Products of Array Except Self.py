from typing import List
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # using prefix and postfix to solve this question
        # should focus on how to make the correct loop for the next prefix to be correct
        # one key point is to set prefix and postfix = 1 at the beginning 
        # ex. [1, 2, 3, 4]
        
        res = [1] * len(nums)
        
        # think of there as a imaginary prefix to the left of the first item, and it will make more sense for the updating
        prefix = 1 
        for i in range(len(nums)):
            res[i] = prefix 
            prefix = prefix * nums[i]
        
        postfix = 1 
        for i in range(len(nums)-1, -1, -1):
            res[i] = res[i] * postfix 
            postfix = postfix * nums[i]
        
        return res

# Test cases
solution = Solution()

# Example test case 1
nums=[1,2,4,6]

print(solution.productExceptSelf(nums))

