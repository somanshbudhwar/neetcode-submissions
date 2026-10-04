class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums)==1:
            return 0
        
        def dfs(idx,steps):
            if idx>=len(nums)-1:
                return steps
            if nums[idx]==0:
                return 9999
            start = [i+idx+1 for i in range(nums[idx])]

            res=9999
            while start:
                index=start.pop(0)
                res=min(res,dfs(index,1+steps))
                print(idx,res)
            return res
        return dfs(0,0)

        