class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefixSumFreq = defaultdict(int)
        prefixSumFreq[0] = 1

        count = 0
        curSum = 0

        for num in nums:
            curSum += num
            diff = curSum - k

            count += prefixSumFreq[diff]
            prefixSumFreq[curSum] += 1
        
        return count
