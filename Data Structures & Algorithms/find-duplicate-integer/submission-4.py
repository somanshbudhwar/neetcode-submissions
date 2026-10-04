class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow,fast=0,0

        while True:
            slow=nums[slow]
            fast=nums[nums[fast]]
            if slow==fast:
                break
        
        fast=0
        while True:
            slow=nums[slow]
            # CRITICAL PART - Move both pointers one at a time to find beginning of a cycle
            fast=nums[fast]

            if fast==slow:
                return slow