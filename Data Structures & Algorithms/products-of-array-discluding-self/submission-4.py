class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # count_zeroes = 0
        # for num in nums:
        #     if num==0:
        #         count_zeroes+=1
        
        # if count_zeroes==0:
        #     product = 1
        #     for num in nums:
        #         product*=num
        #     return [int(product/num) for num in nums]
        # elif count_zeroes==1:
        #     # To store where zero index is
        #     zero_index=0

        #     # Calculate product of non-zero elements & loc of zero
        #     product=1
        #     for i,num in enumerate(nums):
        #         if num==0:
        #             zero_index=i
        #         else:
        #             product*=num
            
        #     # Create array and store only value for zero
        #     res = [0]*len(nums)
        #     res[zero_index]= product
            
        #     return res
        # else:
        #     return [0]*len(nums)

        # Prefix suffix approach

        n = len(nums)
        prefix_prods = [0]*n
        suffix_prods = [0]*n

        for i in range(n):
            if i==0:
                prefix_prods[i]=1
            else:
                prefix_prods[i]=nums[i-1]*prefix_prods[i-1]
        
        for i in range(n-1,-1,-1):
            if i==n-1:
                suffix_prods[i]=1
            else:
                suffix_prods[i]=suffix_prods[i+1]*nums[i+1]
        
        res = [0]*n

        for i in range(n):
            res[i]=prefix_prods[i]*suffix_prods[i]

        return res




