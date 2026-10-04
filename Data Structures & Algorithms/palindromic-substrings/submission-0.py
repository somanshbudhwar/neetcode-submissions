class Solution:
    def countSubstrings(self, s: str) -> int:
        n=len(s)
        if n==0:
            return 0
        if n==1:
            return 1


        dp = [[False]*n for _ in range(n)]
        count=0

        for i in range(n-1,-1,-1):
            for j in range(i,n):
                if s[i]==s[j] and (j-i<=2 or dp[i+1][j-1]):
                    dp[i][j]=True
                    count+=1
        return count

        