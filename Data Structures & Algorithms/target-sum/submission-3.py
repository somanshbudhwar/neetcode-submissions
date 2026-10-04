class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo={}
        def dfs(i, total):
            if i>len(nums):
                return 0
            if i==len(nums) and total==target:
                return 1
            elif i==len(nums):
                return 0
            if (i,total) in memo:
                return memo[(i,total)]
            memo[(i+1,total+nums[i])] = dfs(i+1,total+nums[i])
            memo[(i+1,total-nums[i])] = dfs(i+1,total-nums[i])

            return memo[(i+1,total+nums[i])]+memo[(i+1,total-nums[i])]

        return dfs(0,0)
        