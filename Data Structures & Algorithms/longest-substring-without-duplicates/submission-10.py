class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
            
        start = 0
        charPos = defaultdict(int)
        maxLen = 0

        for r in range(len(s)):
            if s[r] in charPos and start <= charPos[s[r]]:
                start = charPos[s[r]] + 1
            charPos[s[r]] = r
            maxLen = max(maxLen, r-start+1)
        
        return maxLen
