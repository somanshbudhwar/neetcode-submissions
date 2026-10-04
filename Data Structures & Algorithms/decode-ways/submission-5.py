class Solution:
    def numDecodings(self, s: str) -> int:
        n=len(s)
        dp=[0]*n

        for i in range(n-1,-1,-1):
            if s[i]=='0':
                dp[i]=0
            else:
                # CRITICAL BLOCK
                if i+1<n:
                    dp[i]=dp[i+1]
                    if s[i]=='1' or (s[i]=='2' and s[i+1] in '0123456'):
                        dp[i]+=dp[i+2] if i+2<n else 1
                else:
                    dp[i]=1
        print(dp)
        return dp[0]
                    

            
            
            