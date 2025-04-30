# Input: ["neet","code","love","you"]
# we want to encode the list of strs into a single str, and then decode back a list of strs 
# our input after the encode function would look like:
# ["4#need4#code4#love3#you"]
# Output:["neet","code","love","you"]
from typing import List
class Solution:
    def encode(self, strs: List[str]) -> str:
        # for the encode function, we want to make the list of strs into a single str that has the format of:
        # (the number of characters)#str and so on 
        res = ""
        for s in strs:
            res += str(len(s)) + '#' + s
        return res 
        
    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        # we want to set a two pointer loop for i, j 
        while i < len(s):
            j = i
            # the j loop will get to the number length and stop 
            while s[j] != '#':
                j += 1 
            # we get the number length by this line 
            length = int(s[i:j])
            # we assign i to j + 1 to be the start of the string that we want
            i = j + 1 
            # and assign j to i + length to be the end of the string 
            j = i + length
            # append the string to our result list
            res.append(s[i:j])
            # lastly we need to reset i = j for the next loop 
            i = j

        return res
    
# Test cases
solution = Solution()

# Example test case 1
strs = ["neet","code","love","you"]

print(solution.encode(strs))

str = solution.encode(strs)

print(solution.decode(str))