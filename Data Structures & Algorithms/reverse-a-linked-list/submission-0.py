# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        stack = []
        curr = head
        while curr is not None:
            stack.append(curr)
            curr=curr.next
        if stack==[]:
            return None

        head=stack[-1]
        curr=head

        for s in stack[-2::-1]:
            curr.next=s
            curr=curr.next
        
        curr.next=None
        return head
        


        

        