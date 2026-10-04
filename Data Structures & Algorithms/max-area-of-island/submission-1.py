class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        directions=[[-1,0],[1,0],[0,1],[0,-1]]
        ROWS, COLS = len(grid), len(grid[0])

        max_area=0
        curr_area=0

        def dfs(r,c):
            nonlocal curr_area
            if (min(r,c) <0 or
                r>=ROWS or c>=COLS) or grid[r][c]==0:
                return
            if grid[r][c]==1:
                curr_area+=1
                grid[r][c]=0
            
            for direction in directions:
                dfs(r+direction[0],c+direction[1])
            return



        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c]==1:
                    dfs(r,c)
                    if curr_area>max_area:
                        max_area=curr_area
                    curr_area=0
        
        return max_area
        