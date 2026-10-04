class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res=[]
        
        for i, num in enumerate(nums):
            if num>0:
                break

            l=i+1
            r=len(nums)-1
            # print(nums)
            while l<r:
                total=num+nums[l]+nums[r]
                # if l==i or r==i:
                #     break
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

# class Solution:
#     def threeSum(self, nums: List[int]) -> List[List[int]]:
#         res = []
#         nums.sort()

#         for i, a in enumerate(nums):
#             if a > 0:
#                 break

#             if i > 0 and a == nums[i - 1]:
#                 continue
#             print(nums)
#             l, r = i + 1, len(nums) - 1
#             print(l,r)
#             while l < r:
#                 print(nums[l],a,nums[r])
#                 threeSum = a + nums[l] + nums[r]
#                 if threeSum > 0:
#                     r -= 1
#                 elif threeSum < 0:
#                     l += 1
#                 else:
#                     res.append([a, nums[l], nums[r]])
#                     l += 1
#                     r -= 1
#                     while nums[l] == nums[l - 1] and l < r:
#                         l += 1

#         return res

        

        