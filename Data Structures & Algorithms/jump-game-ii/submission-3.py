class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        l = r = 0
        res = 0

        while r < n-1:
            # Fartest index I can reach
            farthest = 0
            for i in range(l,r+1):
                farthest = max(farthest, i+nums[i])
            l = r+1
            r = farthest
            res+=1
        return res

        # n = len(nums)
        # dp = [n] * n
        # dp[-1] = 0

        # for i in range(n-2,-1,-1):
        #     end = min(i+1+nums[i], n)
        #     for j in range(i+1,end):
        #         dp[i] = min(dp[i], 1+dp[j])

        # return dp[0]