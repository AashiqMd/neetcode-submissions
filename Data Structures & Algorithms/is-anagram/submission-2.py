class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        countDict = defaultdict(int)
        for i in range(len(s)):
            countDict[s[i]] += 1
            countDict[t[i]] -= 1

        for k,v in countDict.items():
            if v != 0:
                return False
        return True