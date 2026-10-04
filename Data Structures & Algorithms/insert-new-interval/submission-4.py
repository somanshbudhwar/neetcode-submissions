class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        def create_intervals(l):
            res = [[l[0]]]
            prev = l[0]
            for i in l[1:]:
                if i==l[-1]:
                    if i==prev+1:
                        res[-1].append(i+1)
                        continue
                    else:
                        res[-1].append(prev+1)
                        res.append([i,i+1])
                        continue

                if i==prev+1:
                    prev=i
                    continue
                else:
                    res[-1].append(prev+1)
                    prev=i
                    res.append([i])
                    continue
            return res
        
        s = set()
        for interval in intervals:
            s=s.union(set([i for i in range(interval[0],interval[1])]))
        print(s)
        if newInterval[0]!=newInterval[1]:
            s = s.union(set([i for i in range(newInterval[0],newInterval[1])]))
            s = sorted(list(s))
            res = create_intervals(s)
            return res
        else:
            intervals.append(newInterval)
            intervals.sort(key=lambda x: x[0])
            return intervals
        
                


