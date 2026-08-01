class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)

        maxLen = 0
        for num in numSet:
            if (num-1) not in numSet:
                len = 1
                temp = num+1
                while temp in numSet:
                    len+=1
                    temp+=1
                maxLen = max(maxLen, len)
        return maxLen