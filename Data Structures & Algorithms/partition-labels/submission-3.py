class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last_index={}
        for i,c in enumerate(s):
            last_index[c]=i
        
        size=0
        end=0
        res=[]

        for i,c in enumerate(s):
            size+=1
            end=max(end,last_index[c])

            # CRITICAL IDEA
            if i==end:
                res.append(size)
                size=0
        return res


                


            





        

        

        