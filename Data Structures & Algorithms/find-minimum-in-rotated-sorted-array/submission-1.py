class Solution:
    def findMin(self, nums: List[int]) -> int:
        l=0
        r=len(nums)-1

        min_element = int(10000)

        while l<r:
            mid = int((l+r+1)/2)
            print(f"L={l}, R={r} mid={mid} Min={min_element}")

            if nums[mid]>nums[r]:
                if nums[r]<min_element:
                    min_element=nums[r]
                l=mid+1
            # Cant be equal because numbers are unique
            elif nums[mid]<nums[l]:
                if nums[mid]<min_element:
                    min_element=nums[mid]
                r=mid-1
            elif nums[mid]>nums[l]:
                if nums[l]<min_element:
                    min_element=nums[l]
                r=mid-1

        if l==r:
            return min(nums[l],min_element)
            
        return min_element







        