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
        minheap_endings = []

        for interval in intervals:
            if minheap_endings and minheap_endings[0] <= interval.start:
                heapq.heappop(minheap_endings)
            heapq.heappush(minheap_endings, interval.end)
        
        return len(minheap_endings)
                
        # start = sorted([i.start for i in intervals])
        # end = sorted([i.end for i in intervals])
        # res = count = 0

        # s = e = 0
        # while s < len(start):
        #     if start[s] < end[e]:
        #         count += 1
        #         s+=1 
        #     else:
        #         count -= 1
        #         e+=1
        #     res = max(res, count)
        
        # return res
        