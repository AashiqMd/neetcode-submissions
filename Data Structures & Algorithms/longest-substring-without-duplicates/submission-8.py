class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0

        charIndex = defaultdict(int)
        start = 0 
        maxLen = 0
        for i in range(len(s)):
            char = s[i]
            # Duplicate
            if char in charIndex and charIndex[char] >= start:
                start = charIndex[char] + 1
                
            charIndex[char] = i
            length = i - start + 1
            maxLen = max(maxLen, length)
        
        return maxLen