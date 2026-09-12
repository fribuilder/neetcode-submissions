class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = len(board)
        col = len(board[0])

        for i in range(row):
            col_record = set()
            row_record = set()
            square = set()
            for j in range(col):
                if board[i][j] in row_record:
                    print(i,j)
                    return False
                if board[i][j] != '.':
                    row_record.add(board[i][j]) 

                if board[j][i] in col_record:
                    print(i,j)
                    return False
                if board[j][i] != '.':
                    col_record.add(board[j][i])

                if board[i // 3 * 3 + j // 3][i % 3 * 3 + j % 3] in square:
                    print(i,j, 'square')
                    return False
                if  board[i // 3 * 3 + j // 3][i % 3 * 3 + j % 3] != '.':
                    square.add( board[i // 3 * 3 + j // 3][i % 3 * 3 + j % 3])
        
        return True