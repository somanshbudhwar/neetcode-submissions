class Solution:
    def findMin(self, nums: List[int]) -> int:
        l=0
        r=len(nums)-1

        res=nums[l]

        while l<=r:
            # CRITICAL PART
            if nums[l]<nums[r]:
                res=min(res,nums[l])
                break
            m=(l+r)//2

            if nums[m]<nums[l]:
                # Sorted array on the right so min on left
                r=m-1
            else:
                # Sorted array on the left so min on the right
                l=m+1
            res=min(nums[m],res)
        return res

        







        