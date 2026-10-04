class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp={0:0}

        for i in range(1,amount+1):
            min_coins=100000
            for coin in coins:
                num_coins=min_coins
                # CRITICAL PART - If num_coins exists only then update the min_coins
                if i-coin in dp:
                    num_coins=1+dp[i-coin]
                if num_coins>0:
                    min_coins=min(min_coins,num_coins)
                
                
            if min_coins==100000:
                dp[i]=-1
            else:
                dp[i]=min_coins

        return dp[amount]

                    

        