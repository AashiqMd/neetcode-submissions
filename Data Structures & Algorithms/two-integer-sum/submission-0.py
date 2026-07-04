class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dictA = {}
        for i, num in enumerate(nums):
            if (target - num) in dictA:
                return [dictA[target - num], i]
            else:
                dictA[num] = i