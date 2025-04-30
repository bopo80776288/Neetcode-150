from typing import List

# only brute, too hard to understand 
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        n = len(heights)
        max_area = 0

        for i in range(n):  # Choose the starting bar
            min_height = heights[i]  # Initialize min height
            for j in range(i, n):  # Expand to the right
                min_height = min(min_height, heights[j])  # Track min height
                width = j - i + 1  # Calculate width
                max_area = max(max_area, min_height * width)  # Update max area

        return max_area

# Example usage
solution = Solution()
heights = [2, 1, 5, 6, 2, 3]
print(solution.largestRectangleArea(heights))  # Output: 10
        