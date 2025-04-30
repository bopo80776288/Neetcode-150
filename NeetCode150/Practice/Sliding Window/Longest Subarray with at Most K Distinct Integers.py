# Given an array nums and an integer k, find the length of the longest subarray that contains at most k distinct integers.

# Input: nums = [1, 2, 1, 2, 3], k = 2  
# Output: 4  
# Explanation: The longest subarray with at most 2 distinct numbers is [1,2,1,2].

nums = [1, 2, 1, 2, 3]
k = 2  

freq = {}

l = 0 
res = 0

for r in range(len(nums)):
    freq[nums[r]] = freq.get(nums[r], 0) + 1 
    while len(freq) > k:
        freq[nums[l]] -= 1 
        if freq[nums[l]] == 0:
            del freq[nums[l]]
        l += 1 
    res = max(res, r - l + 1)
print(res)


