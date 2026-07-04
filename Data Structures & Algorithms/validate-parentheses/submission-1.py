class Solution:
    def isValid(self, s: str) -> bool:
        dictA = {
            ')': '(',
            '}': '{',
            ']': '['
        }
        stk = []
        for char in s:
            if char in dictA:
                if stk and stk[-1] == dictA[char]:
                    stk.pop()
                else:
                    return False
            else:
                stk.append(char)
        
        return len(stk)==0