class Solution:
    def numDecodings(self, s: str) -> int:
        n=len(s)
        if n==0:
            return 1
        dp=[0]*len(s)

        for i in range(n-1,-1,-1):
            if s[i]=='0':
                dp[i]=0
            else:
                if i+1<n:
                    dp[i]=dp[i+1]
                else:
                    dp[i]=1
            
            if i+1<n:
                if i+2<n:
                    if s[i]=='1' or (s[i]=='2' and s[i+1] in '0123456'):
                        dp[i]+=dp[i+2]
                else:
                    if s[i]=='1' or (s[i]=='2' and s[i+1] in '0123456'):
                        dp[i]+=1

        return dp[0]       