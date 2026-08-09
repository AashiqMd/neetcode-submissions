"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals.sort(key = lambda x: x.start)
        minheap = [] # Track the end times for intervals

        for interval in intervals:
            s,e = interval.start, interval.end
            if minheap and minheap[0] <= s:
                heapq.heappop(minheap)
            heapq.heappush(minheap, e)
        
        return len(minheap)