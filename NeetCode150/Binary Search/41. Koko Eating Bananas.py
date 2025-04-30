from typing import List
import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # there is no point to eat more banana than the max banana per pile
        l , r = 1, max(piles)
        # set r = res = max(piles) as we expect to decrease or optimize result by trying to decrease k 
        res = r 

        while l <= r :
            k = (l + r) // 2 

            total_time = 0
            for p in piles:
                total_time += math.ceil(float(p / k))
            if total_time <= h:
                res = k
                r = k - 1
            else:
                l = k + 1 
        return res