from typing import List
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # setup a empty list to store value that appears
        numslist = []
        # run through the nums input, if seen num in numslist, return True
        # otherwise append the num to numslist
        # eventaully after run through the nums input we could know if there are duplicates 
        for num in nums:
            if num in numslist:
                return True
            numslist.append(num)
        return False 

# Test cases
solution = Solution()      

# Example test case 1
nums = [1, 2, 3, 3]
print(solution.hasDuplicate(nums))

# Example test case 2
nums = [1, 2, 3, 4]
print(solution.hasDuplicate(nums))