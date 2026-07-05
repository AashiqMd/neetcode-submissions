class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x: x[0])
        prevInterval = intervals[0]
        ans = []

        for i in range(1,len(intervals)):
            s,e = intervals[i][0], intervals[i][1]
            if s <= prevInterval[1]:
                # prevInterval[0] = e
                prevInterval[1] = max(prevInterval[1], e)
            else:
                ans.append(prevInterval)
                prevInterval = [s,e]
        ans.append(prevInterval)
        return ans