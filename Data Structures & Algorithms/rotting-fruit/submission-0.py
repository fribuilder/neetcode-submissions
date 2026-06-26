class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        n_row = len(grid)
        n_col = len(grid[0])

        fresh = []
        rotten = deque()

        for i in range(n_row):
            for j in range(n_col):
                if grid[i][j] == 1:
                    fresh.append((i,j))
                if grid[i][j] == 2:
                    rotten.append((i,j))
        
        def rot(i,j):
            if (i,j) in fresh:
                fresh.remove((i,j))
                rotten.append((i,j))
                return 
        
        minutes = 0
        while fresh:
            L = len(fresh)
            for _ in range(len(rotten)):
                i, j = rotten.popleft()
                rot(i - 1, j)
                rot(i + 1, j)
                rot(i, j - 1)
                rot(i, j + 1)
            minutes += 1
            if len(fresh) == L:
                return -1 

        return minutes 
              