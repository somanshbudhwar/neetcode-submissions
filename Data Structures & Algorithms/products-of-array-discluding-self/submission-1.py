class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product=1
        zeroes=0
        for i in nums:
            if i!=0:
                product*=i
            else:
                zeroes+=1
            if zeroes>1:
                return [0 for n in nums]

        print(product,zeroes)
        if zeroes:
            l = [0 for i in nums]
            z_loc = nums.index(0)
            l[z_loc]=product
            return l
        res = []
        for i in nums:
            res.append(int(product/i))
        return res

            
        