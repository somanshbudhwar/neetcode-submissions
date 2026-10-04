class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        desired_nums=dict()

        for idx,num in enumerate(nums):
            if num in desired_nums:
                return [desired_nums[num],idx]
            else:
                desired_nums[target-num]=idx
        
        return None
        