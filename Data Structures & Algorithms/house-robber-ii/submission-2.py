class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        dp1, dp2 = [0] * len(nums), [0] * len(nums)
        dp1[0], dp1[1] = nums[0], max(nums[0], nums[1])
        dp2[0], dp2[1] = 0, nums[1]

        for i in range(2,len(nums)):
            if i != len(nums)-1:
                dp1[i] = max(nums[i] + dp1[i-2], dp1[i-1])
            dp2[i] = max(nums[i] + dp2[i-2], dp2[i-1])
        
        return max(dp1[-2], dp2[-1])