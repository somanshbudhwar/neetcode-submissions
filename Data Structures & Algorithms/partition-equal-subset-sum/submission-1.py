class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2:
            return False
        
        def dfs(index, target):
            if index>=len(nums):
                return target==0
            if index<0:
                return False
            
            return dfs(index+1,target) or dfs(index+1,target-nums[index])

        return dfs(0,sum(nums)//2)
        