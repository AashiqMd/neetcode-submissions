class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        start, end = 0, n-1

        while start <= end:
            middle = (start + end)//2
            # Non-rotated
            if nums[start] <= nums[end]:
                return nums[start]
            # Dip is on the left side
            if nums[start] > nums[middle]:
                end = middle
            else:
                start = middle + 1