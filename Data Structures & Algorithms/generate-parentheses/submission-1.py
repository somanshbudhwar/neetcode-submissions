class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def valid(s: str):
            open = 0

            for i in s:
                open += 1 if i=="(" else -1
                if open<0:
                    return False
            
            return not open
        
        def dfs(s):
            if n*2 == len(s):
                if valid(s):
                    res.append(s)
                return

            dfs(s+"(")
            dfs(s+")")
        
        res=[]
        dfs("")

        return res
        