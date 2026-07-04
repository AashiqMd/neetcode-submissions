class Solution:
    def countBits(self, n: int) -> List[int]:
        # output = [0] * (n+1)

        # for num in range(n+1):
        #     ones = 0
        #     for i in range(10):
        #         if (num>>i) & 1 == 1:
        #             ones+=1
        #     output[num] = ones
        # return output

        # Optimal and complicated solution
        # Create a dp array where dp[i] is number of 1's for i. 
        # for a number, the count of 1's = 1 + dp[n  - offset]
        # The one is the count of the MSB. And the number of 1's in the remaining lower bits
        # has already been calculated before. We need to identify the correct offset. 

        dp = [0] * (n+1)
        offset = 1
        for i in range(1,n+1):
            if offset * 2 == i:
                offset = i
            dp[i] = 1 + dp[i-offset]

        return dp

