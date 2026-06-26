class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # 1) quick check that every cell is '1'–'9' or '.'
        valid = set(str(d) for d in range(1, 10)) | {'.'}
        for row in board:
            for cell in row:
                if cell not in valid:
                    return False

        # 2) check rows, columns, and 3×3 boxes in one pass
        for i in range(9):
            seen_row = set()
            seen_col = set()
            seen_box = set()
            for j in range(9):
                # --- row i
                v = board[i][j]
                if v != '.':
                    if v in seen_row:
                        return False
                    seen_row.add(v)

                # --- col i
                v = board[j][i]
                if v != '.':
                    if v in seen_col:
                        return False
                    seen_col.add(v)

                # --- box i
                # box row = 3*(i//3) + j//3
                # box col = 3*(i % 3) + j % 3
                br = 3 * (i // 3) + (j // 3)
                bc = 3 * (i % 3)  + (j % 3)
                v = board[br][bc]
                if v != '.':
                    if v in seen_box:
                        return False
                    seen_box.add(v)

        # if we never returned False, it's valid
        return True
