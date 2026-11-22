class Solution:
    def isValid(self, s: str) -> bool:
        stk = []
        pDict = {
            ')' : '(',
            '}' : '{',
            ']' : '['
        }

        for char in s:
            if char in pDict:
                if stk and stk[-1] == pDict[char]:
                    stk.pop()
                else:
                    return False
            else:
               stk.append(char) 
        
        return len(stk)==0