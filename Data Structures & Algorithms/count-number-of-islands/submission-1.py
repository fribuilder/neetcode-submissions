class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n, m = len(grid), len(grid[0])
        def island(i, j):
            directions = [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]
            if grid[i][j] == '1':
                grid[i][j] = '0'
                for h, l in directions:
                    if 0 <= h < n and 0 <= l < m:
                        island(h, l)
        
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    count += 1
                    island(i, j)
        return count

