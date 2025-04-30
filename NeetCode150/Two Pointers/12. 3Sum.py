from typing import List
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        for i in range(len(nums)):
            # if the number is not the beggining of a array and the number before the current i is the same as it
            # we want to skip it to avoid duplicate result
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            # set l to the right of current i and r to the end of the array
            l = i + 1 
            r = len(nums) - 1 
            while l < r: 
                # similar to the twosum problem, if it is greater than 0, we reduce the r to get a smaller value
                if nums[i] + nums[l] + nums[r] > 0:
                    r -= 1 
                elif nums[i] + nums[l] + nums[r] < 0:
                    l += 1
                # if we find a result, we append it to the list 
                else:
                    res.append([nums[i], nums[l], nums[r]])
                    # move l by one
                    l += 1 
                    # and check for if the current number is the same as the previous
                    # if yes we want to skip to avoid duplicate 
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1 
        return res
            
# Test cases
solution = Solution()

# Example test case 1
nums = [0,0,0]
print(solution.threeSum(nums))