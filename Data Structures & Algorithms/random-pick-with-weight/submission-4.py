class Solution:

    def __init__(self, w: List[int]):
        self.w = w

    def pickIndex(self) -> int:
        maxVal = 0
        res = 0
        for idx,num in enumerate(self.w):
            if num > maxVal:
                maxVal = num
                res = idx
        return res


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()