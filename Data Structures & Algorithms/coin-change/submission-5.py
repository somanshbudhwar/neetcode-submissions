class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp={0:0}

        for i in range(1,amount+1):
            min_coins=100000
            for coin in coins:
                # print(coin, i)
                num_coins=None
                if i-coin in dp:
                    num_coins=1+dp[i-coin]
                    # print(num_coins)
                if num_coins and num_coins<min_coins:
                    min_coins=num_coins

            if min_coins==100000:
                dp[i]=-1
            else:
                dp[i]=min_coins
        print(dp)
        return dp[amount]

                    

        