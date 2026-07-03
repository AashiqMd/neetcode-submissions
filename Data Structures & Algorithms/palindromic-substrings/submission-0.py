class Solution:
    def countSubstrings(self, s: str) -> int:
        pSubstrings = 0

        def numSubstrings(l, r):
            if l<0 or r>=len(s) or s[l] != s[r]:
                return 0
            
            return(1 + numSubstrings(l-1, r+1))

        for i in range(len(s)):
            pSubstrings += numSubstrings(i,i) + numSubstrings(i-1,i)
        
        return pSubstrings
        