class Solution:
    def longestPalindrome(self, s: str) -> str:
        def helper(left, right):
            while left>=0 and right<len(s) and s[left] == s[right]:
                left-=1
                right+=1
            return left+1, right-1

        l, r = 0, 0

        for i in range(len(s)):
            l1, r1 = helper(i,i)
            l2, r2 = helper(i-1, i)

            if r1-l1 > r-l:
                l,r = l1,r1
            if r2-l2 > r-l:
                l,r = l2,r2
        
        return s[l:r+1]