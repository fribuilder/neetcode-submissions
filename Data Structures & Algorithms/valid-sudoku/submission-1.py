class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        valid = set(str(d) for d in range(1,10)) | {'.'}
        length, width = len(board), len(board[0])
        for i in range(length):
            for j in range(width):
                if board[i][j] not in valid:
                    return False
        
        for i in range(length):
            row_seen = set()
            col_seen = set()
            box_seen = set()
            for j in range(width):
                if board[i][j] != '.':
                    if board[i][j] not in row_seen:
                        row_seen.add(board[i][j])
                    else:
                        return False

                if board[j][i] != '.':
                    if board[j][i] not in col_seen:
                        col_seen.add(board[j][i])
                    else:
                        return False
                
                ele = board[(i // 3) * 3 + j // 3][(i % 3) * 3 + j % 3] 
                if ele != '.':
                    if ele not in box_seen:
                        box_seen.add(ele)
                    else:
                        return False

        return True 
