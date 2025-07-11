class Solution:
    def isValid(self, s: str) -> bool:
        # use the concept of stack as always want to check if the last open element is valid
        stack = []
        # link the close character to the open for later check 
        table = {")":"(" , "}":"{", "]":"["}


        for c in s:
            # checking if it is a close
            # when we use if x in dict, we are checking if there is a key named x, not the value
            if c in table:
                # checking if the stack is empty and the last open item in the stack matches the close 
                if stack and stack[-1] == table[c]:
                    stack.pop()
                else:
                    return False
            # if not a close, append to stack 
            else:
                stack.append(c)
        
        return not stack 
    
# Test cases
solution = Solution()

# Example test case 1
s=")("


print(solution.isValid(s))
        