"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if len(intervals) <= 1:
            return True
        intervals.sort(key = lambda x: x.end)
        
        prevEnd = intervals[0].end
        for interval in intervals[1:]:
            if interval.start < prevEnd:
                return False
            prevEnd = interval.end
            # print(interval.start,interval.end)

        return True