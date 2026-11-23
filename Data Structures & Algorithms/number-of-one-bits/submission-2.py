class Solution:
    def hammingWeight(self, n: int) -> int:
        i=0
        bits=0
        while n>0:
            bits += n>>i & 1
            n = n>>1
        
        return bits