class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res=nums[0]
        # CRITICAL
        currMin,currMax=1,1

        for num in nums:
            # CRITICAL - tmp is needed coz we update currMax and currMin after one another
            tmp=num*currMax
            currMax=max(num*currMax,num*currMin,num)
            currMin=min(tmp,num*currMin,num)
            res=max(res,currMax)
        return res
