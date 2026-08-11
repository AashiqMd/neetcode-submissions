class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counts = defaultdict(int)
        res = 0
        start = 0
        maxCount = 0

        for i in range(len(s)):
            counts[s[i]]+=1
            maxCount = max(maxCount, counts[s[i]])

            # we only decrement the window size by 1, which will automatically make it <= k
            # and then the next iteration of i, will increment counts with the new char, and only if that resulted in a new maxCount, does our result change. 
            # If it does not, the window length is just shifted from the end of the previous iteration.
            if i-start+1 - maxCount > k:
                counts[s[start]] -= 1
                start += 1
            
            res = max(res, i-start+1)
        return res
