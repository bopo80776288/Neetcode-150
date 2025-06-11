from typing import List 

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # make the length of rows and column explicit
        ROWS, COLS = len(board), len(board[0])
        path = set()
        
        # current cell address visiting, current index in the word  
        def dfs(r, c, i):
            # success case where we reach the end of word
            if i == len(word):
                return True 
            
            # fail case where condition violated
            if (r < 0 or c < 0 or
                r >= ROWS or c >= COLS or
                word[i] != board[r][c] or
                (r, c) in path):
                return False
            
            # if all condition checked pass
            path.add((r, c))
            res = (dfs(r + 1, c, i + 1) or
                    dfs(r - 1, c, i + 1) or
                    dfs(r, c + 1, i + 1) or 
                    dfs(r, c - 1, i + 1))
            path.remove((r, c))
            return res
        
        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r, c, 0): return True
        
        return False
                