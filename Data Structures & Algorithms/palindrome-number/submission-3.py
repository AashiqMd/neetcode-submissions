class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        strNum = str(x)
        length = len(strNum)
        for i in range(length//2):
            if strNum[i] != strNum[length-1-i]:
                return False
        return True