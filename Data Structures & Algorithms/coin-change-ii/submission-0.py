class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        coins.sort()
        memo={}

        def dfs(i,a):
            if a==0:
                return 1
            if i>=len(coins):
                return 0
            if (i,a) in memo:
                return memo[(i,a)]
            
            res=0
            if a>=coins[i]:
                memo[(i+1,a)]=dfs(i+1,a)
                res=memo[(i+1,a)]
                memo[(i,a-coins[i])]=dfs(i,a-coins[i])
                res+=memo[(i,a-coins[i])]
                
            return res
        return dfs(0,amount)