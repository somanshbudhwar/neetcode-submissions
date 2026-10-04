class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        maximum = max(nums)
        mini = min(0,min(nums))
        index = [0 for i in range(mini,maximum+1)]

        for num in nums:
            index[abs(mini)+num]+=1
        

        res = index.index(1)+mini
        
        return res