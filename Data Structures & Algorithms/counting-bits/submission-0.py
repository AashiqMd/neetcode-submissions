class Solution:
    def countBits(self, n: int) -> List[int]:
        output = [0] * (n+1)

        for num in range(n+1):
            ones = 0
            for i in range(12):
                if (num>>i) & 1 == 1:
                    ones+=1
            output[num] = ones
        return output
