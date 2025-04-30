from typing import List
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        temp = temperatures
        res = [0] * len(temp)
        stack = [] # we want the [temp, index]

        # loop through the temp list and append to stack with pair of [temperature, index]
        for i, t in enumerate(temp):
            # if stack is not empty and the temp is greater than the last item in stack
            while stack and t > stack[-1][0]:
                # pop the last item
                stackT, stackInd = stack.pop()
                # record the result of that index and calculate the index different 
                res[stackInd] = (i - stackInd)
            # append the value to stack
            stack.append((t, i))
        return res



        