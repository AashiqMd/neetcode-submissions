class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0

        for i in range(len(s)):
            # Odd length
            l,r = i,i
            while l>=0 and r<len(s) and s[l]==s[r]:
                count+=1    
                l-=1
                r+=1      

            l,r = i-1,i
            # Even length
            while l>=0 and r<len(s) and s[l]==s[r]:
                count+=1
                l-=1
                r+=1
        return count
