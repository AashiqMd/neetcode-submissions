class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = {}
        l = 0
        maxLen = 0
        
        # ridx = 0
        # while ridx<k:
        #     if s[ridx] in freq: 
        #         freq[s[ridx]] += 1
        #     else:
        #         freq[s[ridx]] = 1
        #     ridx+=1

        for r in range(len(s)):
            if s[r] in freq:
                freq[s[r]] += 1
            else:
                freq[s[r]] = 1
            
            while ((r-l+1) - max(freq.values())) > k:
                freq[s[l]] -= 1
                l+=1
            
            maxLen = max(maxLen, r-l+1)
        return maxLen
            

            