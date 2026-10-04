class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res=[]
        
        for i, num in enumerate(nums):
            l=0
            r=len(nums)-1
            # print(nums)
            while l<r:
                total=num+nums[l]+nums[r]
                if l==i or r==i:
                    break
                # print([nums[l],num,nums[r]])
                if total>0:
                    r-=1
                elif total<0:
                    l+=1
                else:
                    triplet= sorted([num,nums[l],nums[r]])
                    if triplet not in res:
                        res.append(triplet)
                    l+=1
                    r-=1

                    
        return res



        

        