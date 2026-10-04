class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # if not nums:
        #     return 0
        # nums = list(set(nums))
        # nums.sort()
        # max_len = 1
        # series_len = 1
        # # print(nums)

        # for i, num in enumerate(nums):
        #     if i==len(nums)-1:
        #         break
        #     if nums[i+1]==num+1:
        #         series_len+=1
        #     else:
        #         series_len=1
            
        #     if series_len>max_len:
        #         max_len=series_len
            
        # return max_len

        # Hashing solution

        series_map = {}

        for num in nums:
            if num not in series_map:
                series_map[num]=None
            if num-1 in series_map:
                series_map[num-1]=num

        keys_to_visit = list(series_map.keys())

        max_len = 0
        for key, item in series_map.items():
            if item is None:
                series_len=1
                prev = key-1

                while prev in series_map:
                    series_len+=1
                    prev-=1
                if series_len>max_len:
                    max_len=series_len

        return max_len

            

            
            



        