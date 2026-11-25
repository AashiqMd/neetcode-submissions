class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # curMax is the max if I definitely consider the current element and possibly consider all prev elements. Similat for curMin

        best = curMax = curMin = nums[0]
        for num in nums[1:]:
            temp = [num*curMax, num*curMin, num]
            curMax = max(temp)
            curMin = min(temp)
            best = max(best, curMax)
        return best