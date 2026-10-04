# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        l=[root,'#']
        temp=[]
        res=[]

        while len(l)>0:
            print(l)
            node=l.pop(0)
            if node=='#':
                if l==[]:
                    res.append(temp)
                    break
                else:
                    res.append(temp)
                    temp=[]
                    l.append('#')
                    continue
            
            if node.left:
                l.append(node.left)
            if node.right:
                l.append(node.right)
            
            temp.append(node.val)
        return res


            