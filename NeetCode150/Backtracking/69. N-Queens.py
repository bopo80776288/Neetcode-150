class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        # check if there is already a Q being placed
        col = set()
        # (r + c) helds a constant for the same diag
        posDiag = set()
        # (r - c) helds a constant for the same diag
        negDiag = set()

        result = []
        board = [["."] * n for i in range(n)]

        def backtrack(r):

            # base case 
            if r == n:
                copy = ["".join(row) for row in board]
                result.append(copy)
                return 
            
            for c in range(n):
                if c in col or (r + c) in posDiag or (r - c) in negDiag:
                    continue
                col.add(c)
                posDiag.add(r + c)
                negDiag.add(r - c)
                board[r][c] = "Q"

                backtrack(r + 1)

                col.remove(c)
                posDiag.remove(r + c)
                negDiag.remove(r - c)
                board[r][c] = "."
        
        backtrack(0)
        return result


