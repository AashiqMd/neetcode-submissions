class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counts = defaultdict(int)
        res = 0
        start = 0
        maxCount = 0

        for i in range(len(s)):
            counts[s[i]]+=1
            maxCount = max(maxCount, counts[s[i]])

            while i-start+1 - maxCount > k:
                counts[s[start]] -= 1
                start += 1
            
            res = max(res, i-start+1)
        return res
