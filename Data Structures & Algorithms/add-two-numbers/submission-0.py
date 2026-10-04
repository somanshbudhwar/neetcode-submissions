# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        s1=""
        while l1:
            s1=str(l1.val)+s1
            l1=l1.next
        
        s2=""
        while l2:
            s2=str(l2.val)+s2
            l2=l2.next

        s3 = str(int(s1)+int(s2))
        print(s3)

        if s3=='':
            return None

        l3=ListNode(int(s3[-1]))
        head=l3

        for s in reversed(s3[:-1]):
            l3.next=ListNode(int(s))
            l3=l3.next

        return head     


        