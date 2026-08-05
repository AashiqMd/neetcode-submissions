class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        best = nums[0]
        curMax, curMin = nums[0], nums[0]
        for num in nums[1:]:
            temp = [num * curMax, num * curMin, num]
            curMax = max(temp[0], temp[1], temp[2])
            curMin = min(temp[0], temp[1], temp[2])
            best = max(curMax, best)
        return best