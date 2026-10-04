class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n=len(nums)
        if n==0:
            return 0
        dp=[1]*n

        for i in range(n-2,-1,-1):
            for j in range(i,n):
                if nums[i]<nums[j] and dp[i]<dp[j]+1:
                    dp[i]=dp[j]+1
        
        return max(dp)


        