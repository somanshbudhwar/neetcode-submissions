class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        largest_prod = -9999999
        def product_array(array):
            res=1
            for a in array:
                res*=a
            return res
        for i in range(len(nums)):
            size=i+1
            for j in range(len(nums)-size+1):
                print(nums[j:j+size])
                product = product_array(nums[j:j+size])
                print(product)
                if product> largest_prod:
                    largest_prod=product
        return largest_prod
        