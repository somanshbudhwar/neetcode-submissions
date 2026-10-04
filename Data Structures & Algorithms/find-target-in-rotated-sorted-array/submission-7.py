class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l=0
        r=len(nums)-1
        iteration = 0
        while l<=r:
            m=(l+r)//2
            print(f"{iteration} - ",l,m,r)
            iteration+=1

            if nums[m]==target:
                return m
            # if nums[l]==target:
            #     return l
            # if nums[r]==target:
            #     return r

            if nums[m]<nums[r]:
                print("Sorted array on right")
                if nums[m]<target:
                    if nums[r]<target:
                        r=m-1
                    else:
                        l=m+1
                else:
                    r=m-1
            else:
                print("Sorted array on left")
                if nums[m]>target:
                    if nums[l]>target:
                        l=m+1
                    else:
                        r=m-1
                else:
                    l=m+1

        return -1
        