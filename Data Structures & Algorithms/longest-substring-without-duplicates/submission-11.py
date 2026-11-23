class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        l = r = 0
        dictA = defaultdict(int)

        while r < len(s):
            if s[r] in dictA and l < dictA[s[r]] + 1:
                l = dictA[s[r]] + 1
            dictA[s[r]] = r

            longest = max(longest, r-l+1)
            r+=1
        return longest