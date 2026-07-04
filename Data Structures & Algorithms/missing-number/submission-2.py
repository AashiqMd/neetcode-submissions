class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        val = len(nums)

        for i in range(len(nums)):
            val = (val^i)^nums[i]
        return val