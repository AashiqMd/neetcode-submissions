class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        # dp = [False] * n
        # dp[n-1] = True

        lastTrueIdx = n-1

        for i in range(n-2,-1,-1):
            if i + nums[i] >= lastTrueIdx:
                # dp[i] = True
                lastTrueIdx = i
            # else:
                # dp[i] = False
        return lastTrueIdx == 0