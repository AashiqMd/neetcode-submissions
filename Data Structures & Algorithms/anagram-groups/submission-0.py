class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []
        groupMap = {}
        idx = 0

        for i, string in enumerate(strs):
            key = "".join(sorted(string))
            if key not in groupMap:
                groupMap[key] = idx
                idx+=1
                res.append([string])
            else:
                res[groupMap[key]].append(string)
        
        return res