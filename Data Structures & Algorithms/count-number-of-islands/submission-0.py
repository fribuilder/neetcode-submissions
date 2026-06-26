class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n_row = len(grid)
        n_col = len(grid[0])
        groups = 0
        
        def search(i,j):
            group = False
            if i < 0 or i >= n_row:
                return
            if j <0 or j >= n_col:
                return
            if grid[i][j] == '1':
                grid[i][j] = '#'
                search(i-1,j)
                search(i+1,j)
                search(i,j-1)
                search(i,j+1)
                group = True
            return group 

        for i in range(n_row):
            for j in range(n_col):
                if grid[i][j] == '#':
                    continue
                if search(i,j):
                    groups += 1

        return groups
