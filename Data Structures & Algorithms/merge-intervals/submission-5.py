class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        def list_to_interval(s):
            res = [[s[0]]]
            prev=s[0]
            for i, element in enumerate(s[1:]):
                print(res,prev,i,element)
                if element==prev+1:
                    prev=element
                    if i==len(s[1:])-1:
                        if len(res[-1])==1:
                            res[-1].append(element+1)
                    continue
                else:
                    res[-1].append(prev+1)
                    res.append([element])
                    prev=element
                    if i==len(s[1:])-1:
                        if len(res[-1])==1:
                            res[-1].append(element+1)
                    continue
            return res
        
        s = set()
        remaining = []
        commons = set([i[0] for i in intervals if i[0]!=i[1]]+[i[1] for i in intervals if i[0]!=i[1]])
        print(commons)
        for interval in intervals:
            if interval[0]!=interval[1]:
                s=s.union(set([i for i in range(interval[0],interval[1])]))
            else:
                if interval[0] not in commons:
                    remaining.append(interval)
        
        print(s)

        print(remaining)
        res =  list_to_interval(sorted(list(s)))
        res+=remaining
        res.sort(key=lambda x: x[0])
        return res




        