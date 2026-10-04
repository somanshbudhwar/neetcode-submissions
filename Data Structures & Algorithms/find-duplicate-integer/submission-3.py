class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow,fast=0,0

        while True:
            slow=nums[slow]
            fast=nums[nums[fast]]
            if slow==fast:
                break
        print(slow,fast)
        
        fast=0
        while True:
            slow=nums[slow]
            # CRITICAL PART
            fast=nums[fast]
            if fast==slow:
                return slow