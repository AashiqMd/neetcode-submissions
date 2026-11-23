class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        setA = set(nums)
        return len(setA) != len(nums)