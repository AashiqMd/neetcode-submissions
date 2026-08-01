class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)

        maxLen = 0
        for num in numSet:
            len = 0
            if (num-1) not in numSet:
                temp = num
                while temp in numSet:
                    len+=1
                    temp+=1
                maxLen = max(maxLen, len)
        return maxLen