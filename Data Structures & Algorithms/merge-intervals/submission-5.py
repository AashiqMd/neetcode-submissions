class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x: x[0])
        merged = []

        mergedS, mergedE = intervals[0][0], intervals[0][1]

        for i in range(1,len(intervals)):
            s,e = intervals[i][0], intervals[i][1]
            if s <= mergedE:
                mergedE = max(e, mergedE)
            else:
                merged.append([mergedS, mergedE])
                mergedS, mergedE = s,e
                
        merged.append([mergedS, mergedE])
        return merged