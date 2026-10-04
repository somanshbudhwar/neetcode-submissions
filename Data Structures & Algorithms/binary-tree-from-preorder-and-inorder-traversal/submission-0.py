# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if preorder==[]:
            return None
        node=TreeNode()
        node.val=preorder[0]
        node_index=inorder.index(node.val)

        left_inorder=inorder[:node_index]
        node.left=self.buildTree(preorder[1:len(left_inorder)+1],left_inorder)

        right_inorder=inorder[node_index+1:]
        node.right=self.buildTree(preorder[len(left_inorder)+1:],right_inorder)

        return node

        