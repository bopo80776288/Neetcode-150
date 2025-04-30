class Solution:
    def subsets(self, nums):
        # Input: nums = [1,2,3]
        # Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
        n = len(nums)
        res, sol = [], []
        
        def backtrack(i):
            if i == n:
                res.append(sol[:])
                return

            # Don't pick nums[i]
            backtrack(i+1)

            # Pick nums[i]
            sol.append(nums[i])
            backtrack(i+1)
            sol.pop()

        backtrack(0)
        return res

