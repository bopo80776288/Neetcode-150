from typing import List
class Solution:
    def trap(self, height: List[int]) -> int:
        # empty list will return False
        if not height: 
            return 0
        # set left, right pointer
        l, r = 0, len(height) - 1
        leftMax, rightMax = height[l], height[r]
        res = 0
        # Move, update, append
        while l < r:
            if leftMax <= rightMax:
                l += 1  # Move left pointer
                leftMax = max(leftMax, height[l])  # Update leftMax first
                res += max(0, leftMax - height[l])  # Ensure no negative values
            else:
                r -= 1  # Move right pointer
                rightMax = max(rightMax, height[r])  # Update rightMax first
                res += max(0, rightMax - height[r])  # Ensure no negative values
        return res
    
# Test cases
solution = Solution()

# Example test case 1
heights = [0,2,0,3,1,0,1,3,2,1]
print(solution.trap(heights))