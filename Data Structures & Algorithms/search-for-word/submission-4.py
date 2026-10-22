class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        n = len(board)
        m = len(board[0])
        explore = [[0]*m for _ in range(n)]
        res = False


        def backtrack(i, j, idx):
            directions = [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]
            nonlocal res

            if idx == len(word):
                res = True
                return 
                            
            for h, l in directions:
                if 0 <= h < n and 0 <= l < m:
                    if board[h][l] == word[idx] and explore[h][l] != 1:
                        explore[h][l] = 1
                        backtrack(h, l, idx + 1)
                        explore[h][l] = 0

        for i in range(n):
            for j in range(m):
                if board[i][j] == word[0]:
                    explore[i][j] = 1
                    backtrack(i,j,1)
                    if res:
                        return res
                    explore[i][j] = 0
        
        return False
