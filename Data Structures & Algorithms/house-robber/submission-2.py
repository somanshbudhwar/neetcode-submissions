class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums)==1:
            return nums[0]
        rewards = {0:nums[0],1:nums[1]}
        for i in range(2,len(nums)):
            max_reward=0
            for j in range(0,i-1):
                if rewards[j]>max_reward:
                    max_reward=rewards[j]

            rewards[i]=max_reward+nums[i]
        
        return max(rewards.values())


        