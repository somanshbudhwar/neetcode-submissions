"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def __init__(self):
        self.map={}
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        if head in self.map:
            # self.map[head]=head.random
            return

        new_node=Node(head.val)
        self.map[head]=new_node
        new_node.next=self.copyRandomList(head.next)
        # CRITICAL PART
        new_node.random=self.map.get(head.random)
        return new_node


        