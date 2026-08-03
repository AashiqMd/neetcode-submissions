class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def helper(s: str, openB, closeB):
            if closeB > openB or openB > n or closeB > n:
                return
            if closeB == openB == n:
                res.append(s)
                return
            
            # print(s, openB, closeB)
            # openB >= closeB and openB and closeB < n
            helper(s+"(", openB+1, closeB)
            helper(s+")", openB, closeB+1)

        helper("",0,0)    
        return res