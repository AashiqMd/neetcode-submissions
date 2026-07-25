class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        n1, n2 = len(word1), len(word2)
        res = ""
        n = min(n1,n2)

        for i in range(n):
            res += word1[i] + word2[i]
        
        res += word1[n:]
        res += word2[n:]
        return res