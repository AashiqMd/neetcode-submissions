class Solution:
    def longestPalindrome(self, s: str) -> str:
        def calcPos(l, r):
            while l>=0 and r<len(s) and s[l] == s[r]:
                l-=1
                r+=1
            return [l+1, r-1]

        l = r = 0

        for i in range(len(s)):
            l1, r1 = calcPos(i,i)
            l2, r2 = calcPos(i-1,i)
            
            if r1-l1 > r-l:
                l, r = l1, r1
            if r2-l2 > r-l:
                l, r = l2, r2
            print(i,l,r, l2, r2)

        return s[l:r+1]