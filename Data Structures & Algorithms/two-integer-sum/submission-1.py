class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indexMap = {}
        for idx, num in enumerate(nums):
            complement = target - num
            if complement in indexMap:
                return [indexMap[complement], idx]
            indexMap[num] = idx