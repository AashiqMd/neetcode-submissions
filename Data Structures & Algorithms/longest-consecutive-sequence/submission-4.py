class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        setA = set(nums)
        longest = 0

        for num in setA:
            if num - 1 not in setA:
                count = 1
                temp = num + 1
                while temp in setA:
                    count+=1
                    temp+=1
                longest = max(longest, count)
        return longest