from typing import List
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        # setup a dict that matches number : count 
        count = {}
        
        # setup lists that equals to the number of count that is possible
        # for example array of 5 will have a min count of 0 and max of 5
        # so the amount of lists will be 6 (0, 1, 2, 3, 4, 5)
        freq = [[] for i in range(len(nums) + 1 )]
        
        # match the number to the count of the number // number:count
        for n in nums:
            count[n] = 1 + count.get(n, 0)
        
        # append each number according to the frequence to the list 
        for n, c in count.items():
            freq[c].append(n)
        
        # create a list to store the result of the kth frequent element that we want 
        res = []

        # run through the freq list and append each number from the end of the list 
        # so that we can get the most frequent element first 
        # stop when the result list has exact k item that we want 
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res

# Test cases
solution = Solution()

# Example test case 1
nums1 = [1, 1, 1, 2, 2, 3]
k1 = 2
print(solution.topKFrequent(nums1, k1))  # Expected output: [1, 2]