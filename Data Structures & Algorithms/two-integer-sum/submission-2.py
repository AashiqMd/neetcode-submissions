class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dictA = defaultdict(int)
        for i in range(len(nums)):
            num = nums[i]
            if num in dictA:
                return [dictA[num],i]
            else:
                dictA[target - num] = i
        
        return -1