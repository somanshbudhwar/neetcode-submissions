class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res=[]

        def dfs(s,rem,opn):
            if len(s)==n*2:
                res.append(s)
                return
            
            if not opn:
                dfs(s+'(',rem-1,opn+1)
            else:
                if not rem:
                    dfs(s+')',rem,opn-1)
                else:
                    dfs(s+')',rem,opn-1)
                    dfs(s+'(',rem-1,opn+1)
        
        dfs("",n,0)
        return res