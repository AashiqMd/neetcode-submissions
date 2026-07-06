class Solution:
    def rob(self, nums: List[int]) -> int:
        # n = len(nums)
        # if n==1:
        #     return nums[0]
        # dp = [-1] * n

        # def dfs(i):
        #     if i>=n:
        #         return 0
        #     if dp[i] != -1:
        #         return dp[i]
        #     dp[i] = max(dfs(i+1), nums[i]+dfs(i+2))  
        #     return dp[i]
        # return dfs(0)  

        n = len(nums)
        if n==1:
            return nums[0]
        
        dp = [0] * n
        dp[n-1], dp[n-2] = nums[n-1], max(nums[n-1], nums[n-2])
        
        for i in range(n-3,-1,-1):
            dp[i] = max(nums[i] + dp[i+2], dp[i+1])
        
        return dp[0]