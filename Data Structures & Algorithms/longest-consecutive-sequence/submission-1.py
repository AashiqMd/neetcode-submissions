class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        distinctNums = set(nums)

        longest, curLongest = 0,0
        for num in distinctNums:
            if num - 1 not in distinctNums:
                curLongest = 1
                temp = num+1
                while temp in distinctNums:
                    curLongest+=1
                    temp+=1
                longest = max(longest, curLongest)
        return longest
