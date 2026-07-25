class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counts = {}
        maxCount = 0
        majorityElement = -1
        for num in nums:
            if num in counts:
                counts[num] += 1
            else:
                counts[num] = 1
            if counts[num] > maxCount:
                maxCount = counts[num]
                majorityElement = num
        
        return majorityElement