# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        def inorder_traversal(node):
            if not node:
                return []
            temp=[node]
            if node.left:
                temp=inorder_traversal(node.left)+temp
            if node.right:
                temp=temp+inorder_traversal(node.right)
            
            return temp
        
        return inorder_traversal(root)[k-1].val


        