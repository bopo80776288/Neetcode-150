from typing import List
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # make a sublist of pairs of position : speed 
        pair = [(p, s) for p, s in zip(position, speed)]
        # sort it in reverse order since we want to consider the closest to the target first
        pair.sort(reverse = True)
        # a stack structure can help maintaining the condition that the current added car should not have a lesser time arrive to the target
        # comparing to the closest car (bec that means it will be capped by the closest car and formed a fleet)
        # therefore if it is faster or the same, we pop, otherwise we add to the stack
        # we count the len() of the stqack to check how many fleet there are 
        stack = []
        # we want to maintain the stack starting to add from the closest position car
        for p, s in pair:
            # how we claculate the time to arrive to target
            stack.append((target - p) / s)
            # it is very easy fail setting stack[-1] >= stack[-2]: but since we are recording "Time", the smaller means it is faster 
            # so if it is faster (time smaller), we pop it since it is capped and formed a fleet
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)
