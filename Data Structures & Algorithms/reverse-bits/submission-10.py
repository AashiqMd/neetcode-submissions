class Solution:
    def reverseBits(self, n: int) -> int:
        num = 0
        for i in range(32):
            LSB = n>>i & 1
            num += LSB << (31-i)
        return num
            