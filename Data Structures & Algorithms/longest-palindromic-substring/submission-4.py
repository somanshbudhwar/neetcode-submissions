class Solution:
    def longestPalindrome(self, s: str) -> str:
        def is_palindrome(a):
            l=0
            r=len(a)-1
            while l<=r:
                if a[l]!=a[r]:
                    return False
                l+=1
                r-=1
            return True
        
        if len(s)==0:
            return ''
        if len(s)==1:
            return s[0]

        max_len=0
        res=[]
        for i in range(1,len(s)+1):
            for j in range(0,len(s)-i+1,1):
                # print(s[j:j+i])
                if is_palindrome(s[j:j+i]):
                    max_len=i
                    res.append(s[j:j+i])
                    # print(res)
        return res[-1]
        
                    






        