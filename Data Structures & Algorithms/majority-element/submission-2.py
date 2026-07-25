class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counts = defaultdict(int)
        maxCount = 0
        majorityElement = 0

        for num in nums:
            counts[num] += 1
            if counts[num] > maxCount:
                maxCount = counts[num]
                majorityElement = num
        
        return majorityElement