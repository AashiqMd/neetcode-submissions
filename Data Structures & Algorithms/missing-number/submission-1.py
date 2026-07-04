class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        val = n

        for i in range(n):
            val = (val^i)^nums[i]
        return val