from typing import List
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # converting the list of nums to a set can make lookup efficient as O(1)
        numSet = set(nums)
        # setting up a longest and compare the current length with the longest can avoid there is a longer consecutive sequence
        # at the later of the array that we will miss out
        # also to correctlly count each length of the sequences
        longest = 0
    
        for n in numSet:
            # key idea here is that for a start of a consecutive sequence, the num must not have a number to the left of it
            if (n - 1) not in numSet:
                length = 0
                # a brillian way to check how long the sequence is as looping through, since each num in the sequence
                # would have a diff of 1 with the previous 
                while (n + length) in numSet:
                    length += 1 
                # to check the current longest length
                longest = max(length, longest)
        return longest
    
# Test cases
solution = Solution()

# Example test case 1
nums=[2,20,4,10,3,4,5]

print(solution.longestConsecutive(nums))