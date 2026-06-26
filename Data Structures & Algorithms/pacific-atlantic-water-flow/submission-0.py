class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        n_row = len(heights)
        n_col = len(heights[0])

        P_source = deque()
        A_source = deque()
        P_reach = set()
        A_reach = set()

        for i in range(n_row):
            P_reach.add((i,0))
            P_source.append((i,0))
            A_reach.add((i,n_col-1))
            A_source.append((i,n_col-1))
        for j in range(0,n_col):
            if j >= 1:
                P_reach.add((0,j))
                P_source.append((0,j))
            if j < n_col - 1:
                A_reach.add((n_row-1,j))
                A_source.append((n_row-1,j))

        def reach(i,j,ori,ocean):
            if i < 0 or i >= n_row or j < 0 or j >= n_col:
                return
            if heights[i][j] >= ori:
                if ocean == 'P' and (i,j) not in P_reach:
                    P_reach.add((i,j))
                    P_source.append((i,j))
                if ocean == 'A' and (i,j) not in A_reach:
                    A_reach.add((i,j))
                    A_source.append((i,j))
        
        while P_source or A_source:
            for _ in range(len(P_source)):
                i,j = P_source.popleft()
                ori_height = heights[i][j]
                reach(i+1,j,ori_height,'P')
                reach(i-1,j,ori_height,'P')
                reach(i,j+1,ori_height,'P')
                reach(i,j-1,ori_height,'P')
            for _ in range(len(A_source)):
                i,j = A_source.popleft()
                ori_height = heights[i][j]
                reach(i+1,j,ori_height,'A')
                reach(i-1,j,ori_height,'A')
                reach(i,j+1,ori_height,'A')
                reach(i,j-1,ori_height,'A')

        return [[i,j] for i,j in A_reach & P_reach]


