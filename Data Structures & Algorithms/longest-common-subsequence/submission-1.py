class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # res = ""
        memo = {}

        def helper(i,j):
            if i>=len(text1) or j>=len(text2):
                return 0
            
            if text1[i] == text2[j]:
                if (i+1,j+1) not in memo:
                    memo[(i+1,j+1)] = helper(i+1,j+1)
                return 1 + memo[(i+1,j+1)]

            else:
                if (i+1,j) not in memo:
                    memo[(i+1,j)] = helper(i+1,j)
                if (i,j+1) not in memo:
                    memo[(i,j+1)] = helper(i,j+1)

                return max( memo[(i+1,j)], memo[(i,j+1)])
        
        return helper(0,0)