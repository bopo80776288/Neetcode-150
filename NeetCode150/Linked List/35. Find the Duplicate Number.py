from typing import List

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow, fast = 0, 0
        # think of each index as a listnode, and the nums is the linked pointer
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        # when slow == fast, we want to break and start another run forming a slow2
        # make slow2 and slow go one step at a time and if they meet, return that value
        # as it will be where the loop starts
        slow2 = 0
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2:
                return slow

        