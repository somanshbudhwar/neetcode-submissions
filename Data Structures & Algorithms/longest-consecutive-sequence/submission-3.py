class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums = list(set(nums))
        nums.sort()
        max_len = 1
        series_len = 1
        # print(nums)

        for i, num in enumerate(nums):
            if i==len(nums)-1:
                break
            if nums[i+1]==num+1:
                series_len+=1
            else:
                series_len=1
            
            if series_len>max_len:
                max_len=series_len
            
        return max_len

        