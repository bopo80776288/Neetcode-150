# A permutation is an ordering of all elements.
# For [1, 2, 3] → all possible ways to rearrange all 3 numbers.

# At each recursive level, we add one more number to a partial list (path)
# We stop when path has the same length as the input → that's a valid permutation

from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtrack(path, used):
            if len(path) == len(nums):
                res.append(path[:])  # base case: a full permutation
                return

            for i in range(len(nums)):
                if used[i]:
                    continue

                # ✅ CHOOSE
                used[i] = True
                path.append(nums[i])

                # 🔁 EXPLORE
                backtrack(path, used)

                # ❌ UN-CHOOSE (backtrack)
                path.pop()
                used[i] = False

        backtrack([], [False] * len(nums))
        return res
