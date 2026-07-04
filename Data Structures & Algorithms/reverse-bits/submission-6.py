class Solution:
    def reverseBits(self, n: int) -> int:
        res = ""
        for i in range(32):
            bit = (n >> i) & 1
            res += str(bit)
        return int(res,2)