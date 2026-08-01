class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxLen = 0
        charPos = defaultdict(int)

        start = 0
        for i in range(len(s)):
            if s[i] in charPos:
                if charPos[s[i]] < start:
                    charPos[s[i]] = i
                else:
                    start = charPos[s[i]] + 1
                    charPos[s[i]] = i
            else:
                charPos[s[i]] = i
            maxLen = max(maxLen, i-start+1)
            # print(i, start, maxLen)
        
        return maxLen