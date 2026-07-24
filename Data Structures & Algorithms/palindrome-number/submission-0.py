class Solution:
    def isPalindrome(self, x: int) -> bool:
        strNum = str(x)
        return strNum == strNum[::-1]