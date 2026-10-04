class Solution:
    # Stack solution
    def isValid(self, s: str) -> bool:
        if len(s)%2!=0:
            return False
        opps = {")":"(","}":"{","]":"["}
        stack=[]
        for i in s:
            print("Stack: ",stack)
            if i in ['(','{','[']:
                stack.append(i)
            else:
                if stack==[]:
                    return False
                if opps[i]==stack[-1]:
                    stack.pop()
                else:
                    return False
        return stack==[]

        