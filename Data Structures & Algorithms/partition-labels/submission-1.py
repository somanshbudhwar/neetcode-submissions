class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        count=Counter(s)
        res=[]
        tmp=set()
        i=0
        last=0

        while i<len(s):
            print(i,s[i],tmp,res)
            count[s[i]]-=1
            if count[s[i]]==0 and tmp==set():
                res.append(s[last:i+1])
                last=i+1
                i+=1
            elif count[s[i]]!=0:
                tmp.add(s[i])
                i+=1
                continue
            elif count[s[i]]==0 and tmp:
                if s[i] in tmp:
                    tmp.remove(s[i])
                if tmp:
                    i+=1
                    continue
                else:
                    res.append(s[last:i+1])
                    last=i+1
                    i+=1

        return [len(i) for i in res]



                


            





        

        

        