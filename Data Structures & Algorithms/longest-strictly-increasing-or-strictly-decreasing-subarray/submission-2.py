class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 1

        maxLength = 1
        curIncLength = 1
        curDecLength = 1

        for i in range(1,len(nums)):
            if nums[i] > nums[i-1]:
                curIncLength += 1
            else:
                curIncLength = 1
            
            if nums[i] < nums[i-1]:
                curDecLength += 1
            else:
                curDecLength = 1
            maxLength = max(maxLength, curIncLength, curDecLength)

        return maxLength
