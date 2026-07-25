class Solution:
    def longestPalindrome(self, s: str) -> str:
        def helper(left,right):
            while left>=0 and right<len(s) and s[left] == s[right]:
                left-=1
                right+=1
            return left+1, right-1

        maxLen = 0
        l,r = 0,0

        for i in range(len(s)):
            lidx, ridx = helper(i,i)
            if ridx - lidx + 1 > maxLen:
                maxLen = ridx - lidx + 1
                l,r = lidx, ridx

            # if i>0: Not needed since helper handles it
            lidx, ridx = helper(i-1,i)
            if ridx - lidx + 1 > maxLen:
                maxLen = ridx - lidx + 1
                l,r = lidx, ridx
        
        return s[l:r+1]