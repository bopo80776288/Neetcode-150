# Given an array nums and an integer k, find the length of the longest subarray whose sum is ≤ k.
# nput: nums = [3, 1, 2, 5, 1, 1, 2, 3], k = 5
# Output: 3
# Explanation: The longest valid subarray is [1, 2, 2] or [5] or [1, 1, 2].

nums = [3, 1, 2, 5, 1, 1, 2, 3]
k = 5
l = 0
res = 0
currentsum = 0  # Start from 0 since no elements are added yet

for r in range(len(nums)):  # Start from 0, so the first element is included
    currentsum += nums[r]  # First, add the current number to the sum

    while currentsum > k:  # If sum exceeds k, shrink the window
        currentsum -= nums[l]
        l += 1

    res = max(res, r - l + 1)  # Update max length when window is valid

print(res)  # Output: 3
