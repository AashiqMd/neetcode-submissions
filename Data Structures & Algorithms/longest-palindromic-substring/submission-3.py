class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        def lphelper(i,j):
            while i>=0 and j<len(s) and s[i] == s[j]:
                i-=1
                j+=1
            return i+1,j-1

        maxLen = 0
        pal = ""
        for i in range(len(s)):
            s1,e1 = lphelper(i,i)
            s2,e2 = lphelper(i,i+1)
            
            start,end = s1, e1
            if e2-s2 > e1-s1:
                start,end = s2,e2
            
            if end-start+1 > maxLen:
                maxLen = max(maxLen, end-start+1)
                pal = s[start:end+1]
        
        return pal