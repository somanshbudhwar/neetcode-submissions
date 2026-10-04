class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        count_zeroes = 0
        for num in nums:
            if num==0:
                count_zeroes+=1
        
        if count_zeroes==0:
            product = 1
            for num in nums:
                product*=num
            return [int(product/num) for num in nums]
        elif count_zeroes==1:
            # To store where zero index is
            zero_index=0

            # Calculate product of non-zero elements & loc of zero
            product=1
            for i,num in enumerate(nums):
                if num==0:
                    zero_index=i
                else:
                    product*=num
            
            # Create array and store only value for zero
            res = [0]*len(nums)
            res[zero_index]= product
            
            return res
        else:
            return [0]*len(nums)
