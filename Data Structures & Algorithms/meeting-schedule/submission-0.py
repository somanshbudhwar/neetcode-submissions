"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        s = set()
        for interval in intervals:
            k = set([i for i in range(interval.start, interval.end)])
            if s.intersection(k):
                return False
            s = s.union(set(k))
            # print(set(s))
        return True

