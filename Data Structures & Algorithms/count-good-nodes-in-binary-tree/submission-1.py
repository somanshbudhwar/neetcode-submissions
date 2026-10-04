# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        dfs_stack=[(root,root.val)]
        count_good={'total':0}

        def dfs():
            while dfs_stack:
                node, max_known = dfs_stack[-1]
                if node.left:
                    dfs_stack.append((node.left,max(max_known,node.val)))
                    dfs()
                if node.right:
                    dfs_stack.append((node.right,max(max_known,node.val)))
                    dfs()
                
                if node.val>=max_known:
                    count_good['total']+=1
                    pass
                dfs_stack.pop()
                return
        dfs()
        return count_good['total']

                
                


        