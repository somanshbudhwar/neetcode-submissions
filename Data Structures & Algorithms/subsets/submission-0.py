class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res=[[]]

        for num in nums:
            new_elements=[]
            for r in res:
                new_elements.append(r+[num])
            res+=new_elements
            # print(res)
        return res
        
        