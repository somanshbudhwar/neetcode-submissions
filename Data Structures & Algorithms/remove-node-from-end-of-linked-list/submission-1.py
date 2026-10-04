# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        count=0
        node=head
        while node:
            count+=1
            node=node.next
        target=count-n

        curr=0
        node=head
        prev=None

        if target==0:
            return head.next

        while curr!=target:
            prev=node
            node=node.next
            curr+=1
        prev.next=node.next

        return head