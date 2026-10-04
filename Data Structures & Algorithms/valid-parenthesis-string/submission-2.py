class Solution:
    def checkValidString(self, s: str) -> bool:
        # CRITICAL IDEA - TWO ARRAYS
        left=[]
        star=[]

        for i, c in enumerate(s):
            if c=='(':
                left.append(i)
            elif c=='*':
                star.append(i)
            else:
                if not left and not star:
                    return False
                if left:
                    left.pop()
                else:
                    star.pop()
        
        while left and star:
            # CRITICAL IDEA - LEFT CANT BE > STAR INDEX COZ IT LEAVES IT OPEN
            if left.pop()>star.pop():
                return False
        return not left
        