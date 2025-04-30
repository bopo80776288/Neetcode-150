class Solution:
    def subsetswithduplicates(self, nums):
        n = len(nums)
        res, sol = [], []

        def backtrack(i):
            if i == n:
                res.append(sol[:])
                return 

            #don't pick nums[i]
            backtrack(i+1)
            

            #check duplicates before we want to pick a num
            if i > 0 and nums[i] == nums[i-1]:
                return 

            #pick nums[i]
            sol.append(nums[i])
            backtrack(i+1)
            sol.pop()
        
        backtrack(0)
        return res

nums = [1, 2, 2]        

solution = Solution()

print(solution.subsetswithduplicates(nums))

        