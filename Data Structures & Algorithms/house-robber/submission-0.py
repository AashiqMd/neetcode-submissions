class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n==1:
            return nums[0]
        
        dp = [0] * (n+1)
        dp[n-1], dp[n-2] = nums[n-1], nums[n-2]
        for i in range(n-3,-1,-1):
            dp[i] = nums[i] + max(dp[i+2], dp[i+3])
        
        # print(dp)
        return max(dp[0],dp[1])