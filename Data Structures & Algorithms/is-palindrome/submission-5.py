class Solution:
    def isPalindrome(self, s: str) -> bool:
        newStr = ''
        for c in s:
            if c.isalnum():
                newStr += c.lower()
        
        l,r = 0, len(newStr) - 1
        while l < r:
            if newStr[l] != newStr[r]:
                return False
            l+=1
            r-=1
        return True


        # arr = s.strip().split(' ')
        # s = "".join(arr)
        
        # l, r = 0, len(s)-1
        # print(s)
        # while l<r:
        #     while l<r and not s[l].isalnum():
        #         l+=1
        #     while l<r and not s[r].isalnum():
        #         r-=1
        #     if s[l].lower() != s[r].lower():
        #         return False
        #     l+=1
        #     r-=1
        # return True