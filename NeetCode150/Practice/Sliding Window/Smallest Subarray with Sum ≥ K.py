# Given an array nums and an integer k, find the length of the smallest contiguous subarray whose sum is at least k. 
# If no such subarray exists, return 0.

# Input: nums = [2, 3, 1, 2, 4, 3], k = 7  
# Output: 2  
# Explanation: The smallest subarray with sum ≥ 7 is [4,3] or [3,4], both of length 2.

nums = [2, 3, 1, 2, 4, 3]
k = 7  

l = 0 
res = float('inf')
currentsum = 0

for r in range(len(nums)):
    currentsum += nums[r]
    while currentsum >= k:
        res = min(res, r - l + 1)
        currentsum -= nums[l]
        l += 1 
    
# If no valid subarray was found, return 0
print(res if res != float('inf') else 0)  # Output: 2
