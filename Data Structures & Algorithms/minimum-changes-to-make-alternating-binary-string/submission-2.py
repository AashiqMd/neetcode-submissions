class Solution:
    def minOperations(self, s: str) -> int:
        ops = 0
        
        # Start with 1
        prev = 0
        for i in range(len(s)):
            if int(s[i]) == prev:
                ops+=1
            prev = 1 - prev

        # Sum of ops if start is 0 and start is 1 must be len(s)
        return min(ops, len(s) - ops)
        
        # # Start with 0
        # ops = 0
        # prev = 1
        # for i in range(len(s)):
        #     if int(s[i]) == prev:
        #         ops+=1
        #     prev = 1 - prev
        
        # return min(minops, ops)