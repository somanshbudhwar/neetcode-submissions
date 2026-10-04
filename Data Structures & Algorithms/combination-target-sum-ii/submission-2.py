class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        nums = sorted(candidates)
        mp={}
        print(nums)
        res=[]

        def explore(i,t,subset):
            if (t,tuple(subset)) in mp:
                return
            if i==len(nums):
                return
            if t-nums[i]<0:
                return 
            elif t-nums[i]==0:
                subset.append(nums[i])
                mp[(t,tuple(subset))]=True
                # res.append(subset.copy())
                return
            else:
                explore(i+1,t-nums[i],subset+[nums[i]])
                explore(i+1,t,subset)
                if nums[i]>t:
                    return
            
            
        explore(0,target,list())
        for key in mp:
            res.append(list(key[1]))
        return res
        