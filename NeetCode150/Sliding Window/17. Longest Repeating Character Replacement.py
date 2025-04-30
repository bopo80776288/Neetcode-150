class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # set a hashmap to count the occurrence of each character
        count = {}
        # set result to 0 
        res = 0
        # set a left pointer that starts from 0 
        l = 0 
        # we increment r and count the character that we seen 
        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)
            
            # this is the condition where the window size - the maximum count character
            # exceeds our character change limit
            # that means that this current window is not valud and we need to shrink
            # we push left by one and at the same time decrease the count of that character on l
            while (r - l + 1) - max(count.values()) > k:
                count[s[l]] -= 1 
                l += 1 
            # r - l + 1 is the size of the window, and we want
            # the maximum of it to be our result 
            res = max(res, r - l + 1)
        return res

# Test cases
solution = Solution()

# Example test case 1
s="XYYX"
k=2
print(solution.characterReplacement(s, k))