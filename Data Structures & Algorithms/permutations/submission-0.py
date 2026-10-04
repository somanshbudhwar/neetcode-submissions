class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        import math

        if not nums:
            return []
        res=[[]]
        def permutation(subset):
            if len(subset[0])==len(nums):
                return subset
            new=[]
            for s in subset:
                for num in nums:
                    if not num in s:
                        new.append(s+[num])
            subset=new
            print(subset)

            return permutation(subset)

        res=permutation([[]])
        return res