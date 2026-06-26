class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not board:
            return False

        n_row = len(board)
        n_col = len(board[0])

        def backtrack(i, j, n):
            # if we've matched all characters
            if n == len(word):
                return True

            # out of bounds
            if i < 0 or i >= n_row or j < 0 or j >= n_col:
                return False

            # current char does not match
            if board[i][j] != word[n]:
                return False

            # mark visited
            tmp = board[i][j]
            board[i][j] = '#'

            # explore neighbors
            Found = (backtrack(i+1, j, n+1) or
                     backtrack(i-1, j, n+1) or
                     backtrack(i, j+1, n+1) or
                     backtrack(i, j-1, n+1))

            # unmark visited
            board[i][j] = tmp

            return Found

        for i in range(n_row):
            for j in range(n_col):
                if backtrack(i, j, 0):
                    return True

        return False
