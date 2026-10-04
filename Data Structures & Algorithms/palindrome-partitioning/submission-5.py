class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res=[]

        def palindrome(p):
            l=0
            r=len(p)-1

            while l<=r:
                if p[l]!=p[r]:
                    return False
                l+=1
                r-=1
            return True
        
        def dfs(i,subset):
            print(i,subset)
            if i==len(s):
                res.append(subset.copy())
                return
            
            j=i
            while j<len(s):
                if palindrome(s[i:j+1]):
                    subset.append(s[i:j+1])
                    dfs(j+1,subset)
                    subset.pop()
                j+=1

        
        dfs(0,[])
        return res
