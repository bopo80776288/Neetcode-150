from typing import List

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        res = []
        # sorting allows us to uswe the duplicate elimination 
        candidates.sort()

        def dfs(i, tempList, total):
            # valid combination
            if total == target:
                res.append(tempList.copy())
                return 
            # invalid combination 
            if i >= len(candidates) or total > target:
                return 
            
            # pick candidate
            tempList.append(candidates[i])
            # no reuse so pass in i + 1
            dfs(i + 1, tempList, total + candidates[i])
            tempList.pop()
            
            # if the next candidate is the same as the current one, skip
            # use the i + 1 < len(candidates) to make sure index in range
            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1

            # skip candidates
            dfs(i + 1, tempList, total)

        dfs(0, [], 0)
        return res