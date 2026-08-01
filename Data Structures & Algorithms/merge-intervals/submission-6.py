class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x: x[0])
        res = []
        s,e = intervals[0][0], intervals[0][1]

        for interval in intervals[1:]:
            if interval[0] <= e:
                e = max(e,interval[1])
            else:
                res.append([s,e])
                s,e = interval[0], interval[1]
        res.append([s,e])
        return res