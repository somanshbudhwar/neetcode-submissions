class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        # Backtracking
        res=[[]]
        nums.sort()
        mp={}

        def explore(i):
            nonlocal res
            print(res)
            if i==len(nums):
                return
            new_res=[]
            for r in res:
                entity=tuple(r+[nums[i]])
                if entity not in mp:
                    new_res.append(r+[nums[i]])
                    mp[entity]=True
                new_res.append(r)
            res=new_res.copy()
            explore(i+1)
                

        explore(0)
        print(mp)
        return res
        