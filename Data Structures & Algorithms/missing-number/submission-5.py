class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        tSum = int(n*(n+1)/2)
        curSum = 0
        for num in nums:
            curSum += num
        
        return tSum - curSum