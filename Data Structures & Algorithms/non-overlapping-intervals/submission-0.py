class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # sort array based on the end time
        intervals.sort(key=lambda interval: interval[1])

        prevEnd = float("-inf")
        remove = 0

        for start,end in intervals:
            if start < prevEnd:
                remove+=1
            else:
                prevEnd = end
        
        return remove