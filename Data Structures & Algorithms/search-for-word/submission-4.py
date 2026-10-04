class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        directions=[[0,1],[1,0],[-1,0],[0,-1]]
        ROWS,COLS = len(board),len(board[0])
        visited=set()

        def dfs(s,row,col):
            
            if not s:
                return True
            if min(row,col)<0 or row>=ROWS or col>=COLS:
                return False
            if (row,col) in visited:
                return False
            
            if s[0]!=board[row][col]:
                return False
            
            print(s,row,col)
            
            visited.add((row,col))

            for dr,dc in directions:
                if dfs(s[1:],row+dr,col+dc):
                    return True
            visited.remove((row,col))
            
        
        for r in range(ROWS):
            for c in range(COLS):
                visited=set()
                if dfs(word,r,c):
                    return True
        return False



        