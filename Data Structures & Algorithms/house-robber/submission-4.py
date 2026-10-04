class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums)==1:
            return nums[0]
        
        # rewards = [0]*len(nums)
        # rewards[0] = nums[0]
        # rewards[1] = max(nums[0],nums[1])
        # for i in range(2,len(nums)):
        #     rewards[i]=max(rewards[i-1],nums[i]+rewards[i-2])
        # return rewards[-1]
        rewards=[0]*(len(nums)+2)
        for i in range(len(nums)):
            rewards[i+2]=max(rewards[i+1],nums[i]+rewards[i])
        return rewards[-1]
        

        