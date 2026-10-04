class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res=[]
        nums.sort()

        def dfs(i,subset,total):
            if i>=len(nums):
                return
            if total==target:
                res.append(subset.copy())
                return
            for j in range(i,len(nums)):
                if nums[j]+total>target:
                    return
                subset.append(nums[j])
                dfs(j,subset,total+nums[j])
                subset.pop()
            pass
        
        dfs(0,[],0)
        return res
        