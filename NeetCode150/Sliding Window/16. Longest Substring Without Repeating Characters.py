class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # we need a charSet
        # we need l , r pointers
        # we need a res set to 0 
        charSet = set()
        l = 0
        res = 0
        
        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1 
            charSet.add(s[r])
            res = max(res, r - l + 1 )
        return res
    

# Test cases
solution = Solution()

# Example test case 1
s = "pwwkew"
print(solution.lengthOfLongestSubstring(s))