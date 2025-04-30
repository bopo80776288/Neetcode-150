from collections import defaultdict
from typing import List
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # the idea is to create dicts for rows, columns, and squares (9x9)
        # store values as we loop through the sudoku and return False if we seen the value twice
        cols = defaultdict(set)
        rows = defaultdict(set)
        squares = defaultdict(set)

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                if (board[r][c] in rows[r] or 
                    board[r][c] in cols[c] or
                    # key right here is to set the key for square to be the r // 3, c //3 since we will only get pairs of
                    # (0, 1, 2), (0, 1, 2) that can locate the square that the number is in
                    board[r][c] in squares[r // 3, c // 3]):
                    return False
                cols[c].add(board[r][c])
                rows[r].add(board[r][c])
                squares[(r //3, c // 3)].add(board[r][c])
        return True

# Test cases
solution = Solution()

# Example test case 1
board=[["1","2",".",".","3",".",".",".","."],["4",".",".","5",".",".",".",".","."],[".","9","8",".",".",".",".",".","3"],["5",".",".",".","6",".",".",".","4"],[".",".",".","8",".","3",".",".","5"],["7",".",".",".","2",".",".",".","6"],[".",".",".",".",".",".","2",".","."],[".",".",".","4","1","9",".",".","8"],[".",".",".",".","8",".",".","7","9"]]


print(solution.isValidSudoku(board))
        