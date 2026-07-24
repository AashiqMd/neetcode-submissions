class Solution:
    def isValid(self, s: str) -> bool:
        dictA = {
            ')': '(',
            '}': '{',
            ']': '['
        }
        stk = []
        for i in range(len(s)):
            if stk and s[i] in dictA:
                if stk[-1] != dictA[s[i]]:
                    return False
                else:
                    stk.pop()
            else:
                stk.append(s[i])
        
        return len(stk)==0