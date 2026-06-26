from typing import List

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        if not board or not board[0]:
            return

        n_row, n_col = len(board), len(board[0])
        O_explore = set()

        for i in range(n_row):
            for j in range(n_col):
                if board[i][j] == 'O':
                    O_explore.add((i, j))

        dirs = [(0,-1),(0,1),(-1,0),(1,0)]

        def surround(i: int, j: int, explored: List[tuple]) -> bool:
            # out of bounds => touches border => NOT surrounded
            if i < 0 or i >= n_row or j < 0 or j >= n_col:
                return False
            # hit X => this direction is closed (ok)
            if board[i][j] == 'X':
                return True
            # already visited O => don't redo work
            if (i, j) not in O_explore:
                return True

            # visit current O
            O_explore.remove((i, j))
            explored.append((i, j))

            sur = True
            for di, dj in dirs:
                sur = surround(i + di, j + dj, explored) and sur
            return sur

        for i in range(n_row):
            for j in range(n_col):
                if board[i][j] == 'O' and (i, j) in O_explore:
                    explored = []
                    sur = surround(i, j, explored)
                    if sur:
                        for r, c in explored:
                            board[r][c] = 'X'
