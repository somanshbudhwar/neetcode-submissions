# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head:
            return 
        
        if not head.next:
            return 
        
        if not head.next.next:
            return
        
        node=head
        next=head.next
        prev=head
        tail=head

        while node.next:
            prev=node
            node=node.next

        tail=node
        print(head.val,next.val,prev.val,tail.val)
        
        head.next=tail
        tail.next=next
        prev.next=None

        self.reorderList(next)







        