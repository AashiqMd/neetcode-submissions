class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        curr = []
        nums.sort()

        def dfs(startIdx, curSum, curr):
            if curSum > target:
                return
            elif curSum == target:
                res.append(curr.copy())
                return
            
            for i in range(startIdx, len(nums)):
                curr.append(nums[i])
                dfs(i, curSum+nums[i] ,curr)
                curr.pop()

        dfs(0, 0 ,[])

        return res