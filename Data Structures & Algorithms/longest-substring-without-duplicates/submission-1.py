class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longestLength = 0
        l,r = 0,0
        lastPosition = defaultdict(int)

        while r<len(s):
            char = s[r]
            if char in lastPosition and lastPosition[char] >= l:
                l = lastPosition[char] + 1

            longestLength = max(longestLength, r-l+1)
            lastPosition[char] = r
            r+=1
            
        return longestLength