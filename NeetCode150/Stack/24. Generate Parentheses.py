from typing import List
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        sol = []
        res = []

        def backtrack(openN, closedN):
            # base case where we have the max pair of close and open 
            if openN == closedN == n:
                # append the current sol to res using the join()
                res.append("".join(sol))
                return
            # if open is less than the n (since we have max of n pairs of (), either open or close cannot exceed n)
            if openN < n:
                sol.append("(")
                backtrack(openN + 1, closedN)
                sol.pop()
            # can add a close if close is less than open 
            if closedN < openN:
                sol.append(")")
                backtrack(openN, closedN + 1)
                sol.pop()
        
        backtrack(0 , 0)

        return res