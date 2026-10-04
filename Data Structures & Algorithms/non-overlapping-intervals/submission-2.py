class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1])
        print(intervals)
        last = intervals[0][1]
        res=0

        for i in range(1,len(intervals)):
            if last>intervals[i][0]:
                res+=1
                # last=intervals[i][1]
            else:
                last=intervals[i][1]

        return res
        