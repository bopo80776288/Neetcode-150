from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # to find if there are two nums in the given list that can make up the target
        # and we want to return the index of the two nums
        
        # we can set a hash table to match number : index
        numstable = {}
        for i, num in enumerate(nums):
            # we want to look for if there exist a diff = target - num in our table 
            # such like if [1, 2] target = 3 can be found, there will be a diff of 3 - 2 = 1 in our numslist , which there is in this case
            diff = target - num
            # check if diff exist in our hashtable, we return the index of that diff, and the current num index
            if diff in numstable:
                return [numstable[diff], i]
            # otherwise, we asign the num to the index into the hashtable
            numstable[num] = i

# Test cases
solution = Solution()

# Example test case 1
nums=[3,4,5,6]
target=7
print(solution.twoSum(nums, target)) 