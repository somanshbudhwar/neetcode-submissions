class Solution:
    def rob(self, nums: List[int]) -> int:
        def rob_rewards(houses):
            if len(houses)==0:
                return 0
            if len(houses)==1:
                return houses[0]

            rewards = [0]*len(houses)
            rewards[0] = houses[0]
            rewards[1] = max(houses[0],houses[1])
            for i in range(2,len(houses)):
                rewards[i]=max(rewards[i-1], houses[i]+rewards[i-2])
            return rewards[-1]
        
        if len(nums)==0:
            return 0
        if len(nums)==1:
            return nums[0]
        return max(rob_rewards(nums[:-1]),rob_rewards(nums[1:]))

