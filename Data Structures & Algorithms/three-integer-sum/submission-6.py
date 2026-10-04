class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res=[]

        for i, num in enumerate(nums):
            if num>0:
                return res
            
            # Skip duplicates
            if i>0:
                if nums[i]==nums[i-1]:
                    continue
            
            l=i+1
            r=len(nums)-1
            while l<r:
                tripleSum=num+nums[l]+nums[r]

                if tripleSum>0:
                    r-=1
                elif tripleSum<0:
                    l+=1
                else:
                    if [num,nums[l],nums[r]] not in res:
                        res.append([num,nums[l],nums[r]])
                    l+=1
                    r-=1
        return res

            
