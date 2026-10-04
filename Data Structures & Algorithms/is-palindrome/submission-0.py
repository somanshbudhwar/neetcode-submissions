class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.lower()

        alphanumeric='abcdefghijklmnopqrstuvwxyz1234567890'
        res = [i for i in s if i in alphanumeric]
        s = res
        l=0
        r=len(s)-1

        while l<r:
            if s[l]!=s[r]:
                return False
            l+=1
            r-=1
        return True