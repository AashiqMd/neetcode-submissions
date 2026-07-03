class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = {}
        l = 0
        maxLen = 0
        
        ridx = 0
        maxFreq = 0
        while ridx<k:
            if s[ridx] in freq: 
                freq[s[ridx]] += 1
            else:
                freq[s[ridx]] = 1
            maxFreq = max(maxFreq, freq[s[ridx]])
            ridx+=1

        
        for r in range(ridx, len(s)):
            if s[r] in freq:
                freq[s[r]] += 1
            else:
                freq[s[r]] = 1
            maxFreq = max(maxFreq, freq[s[r]])
            
            while ((r-l+1) - maxFreq) > k:
                freq[s[l]] -= 1
                l+=1
            
            maxLen = max(maxLen, r-l+1)
        return maxLen
            

            