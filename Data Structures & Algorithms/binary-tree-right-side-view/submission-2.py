# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        l=[root,"#"]
        res=[]

        while len(l)>0:
            node=l.pop(0)
            if node=='#':
                if l==[]:
                    res.append('#')
                    break
                else:
                    res.append('#')
                    l.append('#')
                    continue

            res.append(node)
            if node.left:
                l.append(node.left)
            if node.right:
                l.append(node.right)
        print(res)
        final=[]
        for i,node in enumerate(res):
            if node=='#':
                final.append(res[i-1].val)

        return final

            

        