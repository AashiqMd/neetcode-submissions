class Solution:
    def isValid(self, s: str) -> bool:
        dictA = {
            ')': '(',
            '}': '{',
            ']': '['
        }
        stk = []
        for i in range(len(s)):
            if s[i] in dictA:
                if stk and stk[-1] == dictA[s[i]]:
                    stk.pop()
                else:
                    return False
            else:
                stk.append(s[i])
        
        return len(stk)==0