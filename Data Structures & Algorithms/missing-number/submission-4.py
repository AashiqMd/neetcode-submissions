class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        sum = len(nums)
        for i in range(len(nums)):
            sum += i - nums[i]
        return sum
        # val = len(nums)

        # for i in range(len(nums)):
        #     val = (val^i)^nums[i]
        # return val