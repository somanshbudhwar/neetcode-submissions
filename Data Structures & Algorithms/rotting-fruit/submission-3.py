class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS,COLS=len(grid),len(grid[0])
        directions=[(1,0),(0,1),(-1,0),(0,-1)]
        for g in grid:
            print(g)

        print("*"*10)

        # CRITICAL IDEA - BFS GUARANTEES SHORTEST PATH OF UNWEIGHTED GRID
        def bfs(r,c):
            q=deque([(r,c)])
            visited=[[False]*COLS for _ in range(ROWS)]
            visited[r][c]=True
            steps=10

            while q:
                for _ in range(len(q)):
                    r,c = q.popleft()
                    
                    if grid[r][c]==2:
                        return steps
                    
                    for dr,dc in directions:
                        nr,nc = r+dr,c+dc
                        if (0<=nr<ROWS and 0<=nc<COLS and
                        visited[nr][nc]!=True and
                        grid[nr][nc]!=0):
                            visited[nr][nc]=True
                            q.append((nr,nc))
                steps+=1
            return grid[r][c]
                
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c]==1:
                    grid[r][c]=bfs(r,c)
        
        max_time=0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c]==1:
                    return -1
                if grid[r][c]>=10 and max_time<grid[r][c]:
                    max_time=grid[r][c]
        
        return max_time-10 if max_time else 0
        