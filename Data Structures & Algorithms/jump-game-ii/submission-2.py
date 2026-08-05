class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [n] * n
        dp[-1] = 0

        for i in range(n-2,-1,-1):
            end = min(i+1+nums[i], n)
            for j in range(i+1,end):
                dp[i] = min(dp[i], 1+dp[j])

        return dp[0]