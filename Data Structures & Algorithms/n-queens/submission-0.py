from typing import List

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        
        # board as list of strings; start with all '.'
        board = [["."] * n for _ in range(n)]
        
        cols = set()   # used columns
        diag1 = set()  # r - c
        diag2 = set()  # r + c
        
        def backtrack(r: int):
            # if we've placed queens in all rows, record a solution
            if r == n:
                # convert each row to string
                res.append(["".join(row) for row in board])
                return
            
            # try placing a queen at (r, c) for all c
            for c in range(n):
                if c in cols or (r - c) in diag1 or (r + c) in diag2:
                    continue  # conflict, skip this column
                
                # place queen
                board[r][c] = "Q"
                cols.add(c)
                diag1.add(r - c)
                diag2.add(r + c)
                
                # move to next row
                backtrack(r + 1)
                
                # backtrack: remove queen
                board[r][c] = "."
                cols.remove(c)
                diag1.remove(r - c)
                diag2.remove(r + c)
        
        backtrack(0)
        return res
