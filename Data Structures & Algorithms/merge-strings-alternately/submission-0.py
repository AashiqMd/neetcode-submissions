class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        n1, n2 = len(word1), len(word2)
        res = ""

        for i in range(min(n1,n2)):
            res += word1[i] + word2[i]
        
        res += word1[min(n1,n2):]
        res += word2[min(n1,n2):]
        return res