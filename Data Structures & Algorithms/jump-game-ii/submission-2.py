class Solution:
    def jump(self, nums: List[int]) -> int:
        # CRITICAL - GREEDY
        res=0
        l=r=0

        while r<len(nums)-1:
            farthest=0
            for i in range(l,r+1):
                print(l,r,farthest,i, nums[i])
                farthest=max(farthest,i+nums[i])
            
            # CRITICAL - L=R+1 and R=FARTHEST
            l=r+1
            r=farthest
            res+=1
        return res



        