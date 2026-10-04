class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            # CRITICAL
            res+=str(len(s))+"#"+s
        # print(res)
        return res


    def decode(self, s: str) -> List[str]:
        strs=[]
        i=0
        while i<len(s):
            j=i
            while s[j]!="#":
                j+=1
            # print(s[i:j])
            length=int(s[i:j])
            strs.append(s[j+1:j+length+1])
            # print(strs)
            i=j+length+1
            
                
        return strs
            
        
