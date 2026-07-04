class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        sum = 0
        n = len(nums)
        for i in range(len(nums)):
            sum += nums[i]
        return ((n*(n+1))//2) - sum
        # val = len(nums)

        # for i in range(len(nums)):
        #     val = (val^i)^nums[i]
        # return val