class Solution:
    def isValid(self, s: str) -> bool:
        stk = []
        pDict = {
            ')' : '(',
            '}' : '{',
            ']' : '['
        }

        for i in range(len(s)):
            char = s[i]
            if char in pDict:
                if stk and stk[-1] == pDict[char]:
                    stk.pop()
                else:
                    return False
            else:
               stk.append(char) 
        
        return len(stk)==0