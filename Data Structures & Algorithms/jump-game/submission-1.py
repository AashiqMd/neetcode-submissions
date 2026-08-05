class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # A dp solution would take O(n2)
        n = len(nums)
        # dp = [False] * n
        # dp[n-1] = True

        goal = n-1

        for i in range(n-2,-1,-1):
            if i + nums[i] >= goal:
                # dp[i] = True
                goal = i
            # else:
                # dp[i] = False
        return goal == 0