from typing import List
class Solution:
    def findMin(self, nums: List[int]) -> int:
        # [3,4,5,6,1,2]
        # set binary search
        l, r = 0, len(nums) - 1 
        # seta default res to be the first number in array 
        res = nums[0]

        while l <= r:
        # the condition where the range between l and r is completely sorted, which we just take nums[l] as min
            if nums[l] < nums[r]:
                res = min(res, nums[l])
                break
            # also need to compare mid to res as mid might possibly be sitting on the first element in the right portion which is the min
            mid = (l + r) // 2 
            res = min(res, nums[mid])
            # this case means we are in the left portion so we want to search right 
            if nums[mid] >= nums[l]:
                l = mid + 1 
            # we in the right portion so we want to search left to find the min
            else:
                r = mid - 1 
        
        return res