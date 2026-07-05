class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        sNew, eNew = newInterval[0], newInterval[1]
        n = len(intervals)
        result = []

        # Phase 1: Add all intervals that end before newInterval starts
        i=0
        while i<n and sNew > intervals[i][1]:
            result.append(intervals[i])
            i+=1
        
        # Phase 2: Merge all overlapping intervals
        while i<n and eNew >= intervals[i][0]:
            sNew = min(sNew, intervals[i][0])
            eNew = max(eNew, intervals[i][1])
            i+=1
        result.append([sNew, eNew])

        # Phase 3: Add remaining intervals
        while i<n:
            result.append(intervals[i])
            i+=1

        return result