class Solution:

    def __init__(self, w: List[int]):
        self.w = w
        self.prefixSum = [0] * len(w)
        self.prefixSum[0] = w[0]
        for i in range(1,len(w)):
            self.prefixSum[i] = w[i] + self.prefixSum[i-1]

    def pickIndex(self) -> int:
        maxVal = 0
        randomTarget = random.random() * self.prefixSum[-1]

        for idx,num in enumerate(self.w):
            if self.prefixSum[idx] >= randomTarget:
                return idx
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()