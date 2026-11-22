class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dictA = defaultdict(int)
        for i in range(len(nums)):
            num = nums[i]
            complement = target - num
            if complement in dictA:
                return [dictA[complement],i]
            dictA[num] = i
        
        return []