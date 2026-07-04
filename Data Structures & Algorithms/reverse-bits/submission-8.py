class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        for i in range(32):
            # Get last bit
            bit = (n >> i) & 1
            # Move bit to front
            res += (bit << (31-i))
        return res