class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        i = 0
        j = m*n - 1
        while i <= j:
            s = i + (j-i)//2
            row = s // n
            col = s % n
            if matrix[row][col] > target:
                j = s - 1
            elif  matrix[row][col] < target:
                i = s + 1
            else: 
                return True 
        return False
