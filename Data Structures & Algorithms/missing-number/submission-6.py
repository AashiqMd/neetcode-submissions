class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # Calculate the sum of every index in the range 
        # Subtract every element in nums
        tSum = len(nums)
        for idx,num in enumerate(nums):
            tSum = tSum + idx - num
        return tSum

        
        
        
        # n = len(nums)
        # tSum = int(n*(n+1)/2)
        # curSum = 0
        # for num in nums:
        #     curSum += num
        
        # return tSum - curSum