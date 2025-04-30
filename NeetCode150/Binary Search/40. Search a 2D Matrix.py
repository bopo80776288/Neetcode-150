from typing import List

class Solution:
    # matrix = [[1,2],[3,4],[5,6],[7,8],[9,10],[11,12],[13,14]]
    # target = 13
    
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])

        l, r = 0, rows - 1 

        while l <= r:
            middle = (l + r) // 2

            if target > matrix[middle][-1]:
                l = middle + 1 
            elif target < matrix[middle][0]:
                r = middle - 1 
            else:
                break 
        # this line is quite important for logic cause if after we exhaust the while loop and we didn't break, that means that there are no
        # potential rows that has the target in it so we can just return False
        if not l <= r:
            return False
        
        row_left, row_right = 0, cols - 1

        while row_left <= row_right:
            mid = (row_left + row_right) // 2 
            if target > matrix[middle][mid]:
                row_left = mid + 1 
            elif target < matrix[middle][mid]:
                row_right = mid - 1 
            else:
                return True
        
        return False

        
