class Solution:
    def isValid(self, s: str) -> bool:
        # use the concept of stack as always want to check if the last open element is valid
        stack = []
        # link the close character to the open for later check 
        table = {")":"(" , "}":"{", "]":"["}

        for c in s:
            if c not in table:
                stack.append(c)
            else:
                if not stack or stack[-1] != table[c]:
                    return False
                stack.pop()
        
        return not stack
# Test cases
solution = Solution()

# Example test case 1
s=")("


print(solution.isValid(s))
        