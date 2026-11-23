class Solution:
    def hammingWeight(self, n: int) -> int:
        bits=0
        for i in range(32):
            bits += n>>i & 1
        return bits