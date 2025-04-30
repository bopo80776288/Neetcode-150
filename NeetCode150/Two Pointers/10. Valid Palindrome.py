class Solution:
    def isPalindrome(self, s: str) -> bool:
        # we set for a two pointer one starting from the beggining of the str on starting from the end
        l, r = 0, len(s) - 1
        # we want to keep going and stop before left pointer past right pointer
        while l < r:
            # if current l or r pointing at a non-alphanumerical object in str, it will result a "not False"
            # double negative which gives us a "True" and execute the l or r += 1, which we skip this object
            while l < r and not self.alphaNum(s[l]):
                 l += 1 
            while l < r and not self.alphaNum(s[r]):
                 r -= 1 
            # if the object doesn't match for what l and r is pointing, this is not a palindrome
            if s[l].lower() != s[r].lower():
                return False
            # move l, r one step further 
            l, r = l + 1, r - 1 
        return True
    
    # this function detect any non-alphanumerical objects in the str
    def alphaNum(self, c):
        return (ord("A")<= ord(c)<= ord("Z") or 
                ord("a")<= ord(c)<= ord("z") or 
                ord("0")<= ord(c)<= ord("9"))

# Test cases
solution = Solution()

# Example test case 1
s="Was it a car or a cat I saw?"

print(solution.isPalindrome(s))