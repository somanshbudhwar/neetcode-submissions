class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if len(nums)==0:
            return 0
        dp=[1]*len(nums)


        for i in range(len(nums)-2,-1,-1):
            for j in range(i,len(nums)):
                if nums[i]<nums[j] and dp[i]<dp[j]+1:
                        print("Comparing: ",nums[i],nums[j])
                        dp[i]=dp[j]+1
                        print(dp)

        return max(dp)


        