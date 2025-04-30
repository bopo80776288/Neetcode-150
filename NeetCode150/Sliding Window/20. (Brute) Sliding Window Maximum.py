from typing import List
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        output = []

        for i in range(len(nums) - k + 1):
            maxn = nums[i]
            for j in range(i, i + k):
                maxn = max(maxn, nums[j])
            output.append(maxn)
    
        return output
                
# Test cases
solution = Solution()

# Example test case 1
nums=[1,2,1,0,4,2,6]
k=3

print(solution.maxSlidingWindow(nums, k))