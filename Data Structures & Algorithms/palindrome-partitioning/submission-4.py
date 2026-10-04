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
            
            for j in range(i+1,len(s)+1):
                if palindrome(s[i:j]):
                    subset.append(s[i:j])
                    dfs(j,subset)
                    subset.pop()

        
        dfs(0,[])
        return res
