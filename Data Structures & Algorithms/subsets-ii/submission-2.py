class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res=[[]]
        mp=set()

        def dfs(i):
            nonlocal res,mp
            if i==len(nums):
                return
            
            subset=[]

            for r in res:
                tmp=sorted(r+[nums[i]])
                if tuple(tmp) not in mp:
                    mp.add(tuple(tmp))
                    subset.append(tmp)

            res=res.copy()+subset.copy()

            dfs(i+1)
 


        dfs(0)
        return res
        