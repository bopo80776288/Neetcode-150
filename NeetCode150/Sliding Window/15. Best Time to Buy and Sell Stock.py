from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # left is buying, right is selling 
        l, r = 0, 1 
        maxP = 0
        while r < len(prices):
            # buy low sell high, this is waht we want
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                maxP = max(maxP, profit)
            # if prices[l] is higher, we want to set all the way for l = r, so that l is now at the lowest
            else:
                 l = r
            r += 1 

        return maxP
    
# Test cases
solution = Solution()

# Example test case 1
prices = [2,20,4,10,3,4,5]

print(solution.maxProfit(prices))