class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxLen = 0
        charPos = {}

        start = 0
        for i in range(len(s)):
            if s[i] in charPos and charPos[s[i]] >= start:
                start = charPos[s[i]] + 1
            charPos[s[i]] = i
            maxLen = max(maxLen, i-start+1)
        
        return maxLen