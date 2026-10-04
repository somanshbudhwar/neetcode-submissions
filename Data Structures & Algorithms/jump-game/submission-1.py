class Solution:
    def canJump(self, nums: List[int]) -> bool:
        def dfs(idx):
            print("Index: ",idx)
            if idx==len(nums)-1:
                return True

            if nums[idx]==0:
                return False
            
            # CRITICAL
            start = [i for i in range(idx+1,nums[idx]+idx+1)]
            print(start)

            while start:
                index=start.pop(0)
                
                if dfs(index):
                    return True
            return False
        return dfs(0)
                
        