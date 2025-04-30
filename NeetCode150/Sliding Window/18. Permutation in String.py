class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1count = [0] * 26 
        for c in s1:
            s1count[ord(c) - ord('a')] += 1 
        
        for l in range(len(s2) - len(s1) + 1):
            s2count = [0] * 26
            for r in range(l, l + len(s1)):
                s2count[ord(s2[r]) - ord('a')] += 1 
                if s1count == s2count:
                    return True
        return False
    
# Test cases
solution = Solution()

# Example test case 1
s1 = "ab"
s2 = "lecabee"

print(solution.checkInclusion(s1, s2))