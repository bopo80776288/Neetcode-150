from typing import List
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # Input: tokens = ["1","2","+","3","*","4","-"]
        # we want to do it as reverse polish notation where:
        # 1, 2, +, will be 1 + 2 
        # 3, 4, / will be 3 / 4 
    
        stack = []
        for c in tokens:
            # for + and * the order doesn't matter 
            if c == "+":
                stack.append(stack.pop() + stack.pop())
            
            # for - and / order matter, so the item pop needs to be assign to a, b later for assigning the correct order
            elif c == "-": 
                a, b = stack.pop(), stack.pop()
                stack.append(b - a)
            # for + and * the order doesn't matter 
            elif c == "*":
                stack.append(stack.pop() * stack.pop())
            
            # for - and / order matter, so the item pop needs to be assign to a, b later for assigning the correct order
            elif c == "/":
                a, b = stack.pop(), stack.pop()
                stack.append(int(b / a))
            else:
                stack.append(int(c))
        
        return stack[0]

# Test cases
solution = Solution()

# Example test case 1
tokens=["2","1","+","3","*"]

print(solution.evalRPN(tokens))
        
