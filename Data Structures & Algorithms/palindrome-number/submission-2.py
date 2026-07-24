class Solution:
    def isPalindrome(self, x: int) -> bool:
        strNum = str(x)
        length = len(strNum)
        for i in range(length//2):
            if strNum[i] != strNum[length-1-i]:
                return False
        return True