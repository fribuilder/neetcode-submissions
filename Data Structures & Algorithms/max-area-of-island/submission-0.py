class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        n_row = len(grid)
        n_col = len(grid[0])
        max_area = 0

        def island(i,j,area):
            if i < 0 or i >= n_row:
                return 0
            if j < 0 or j >= n_col:
                return 0

            if grid[i][j] == 1:
                grid[i][j] = '#'
                area = 1 + island(i+1,j,area) + island(i-1,j,area) + island(i,j+1,area) + island(i,j-1,area)
            
            return area
        
        for i in range(n_row):
            for j in range(n_col):
                if grid[i][j] == 1:
                    max_area = max(max_area,island(i,j,0))
        
        return max_area
                   
                