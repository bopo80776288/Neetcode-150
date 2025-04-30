from typing import List
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # using two pointer to solve for the Sorted list two sum problem
        l, r = 0, len(numbers) - 1
        while l < r:
            # if the current sum is larger than the target, we move the right pointer down since that will give us lesser value
            if (numbers[l] + numbers[r]) > target:
                r -= 1 
            # if the current sum is smaller than target then we move left pointer up to increase the value
            elif (numbers[l] + numbers[r]) < target:
                l += 1 
            # eventually we get to that the sum = target and we return the index + 1 since the index count is starting from 1 
            else:
                return [l + 1, r + 1]
            
# Test cases
solution = Solution()

# Example test case 1
numbers = [1,2,3,4]
target = 3
print(solution.twoSum(numbers, target))