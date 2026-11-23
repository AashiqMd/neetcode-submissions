class Solution:
    def climbStairs(self, n: int) -> int:
        if n==1:
            return 1
        dp_1, dp_2 = 1,2
        for i in range(3,n+1):
            dp_1, dp_2 = dp_2, dp_1 + dp_2
        return dp_2