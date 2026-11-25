class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0

        def countPal(l, r):
            cnt = 0
            while l>=0 and r<len(s) and s[l]==s[r]:
                cnt+=1    
                l-=1
                r+=1   
            return cnt

        for i in range(len(s)):
            # Odd length
            count += countPal(i,i)

            # Even length
            count += countPal(i-1,i)

        return count
